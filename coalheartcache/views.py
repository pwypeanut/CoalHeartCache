from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from models import Category, Story, Commitment, Donor, Charity
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, "index.html", {})

@login_required
def change_name(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    request.user.first_name = name
    request.user.email = email
    request.user.save()
    return HttpResponse()

@login_required
def change_password(request):
    old_password = request.POST.get("old_password")
    password = request.POST.get("password")
    if not request.user.check_password(old_password):
        return HttpResponse("failed")
    else:
        request.user.set_password(password)
        request.user.save()
        return HttpResponse()
    

@login_required
def main_page(request):
    return render(request, "main.html", {
        'categories': Category.objects.all(),
        'category': "All Categories",
        'displays': Category.objects.all(),
    })

@login_required
def category_list(request, name):
    name = name.replace("_", " ")
    try:
        category = Category.objects.get(name = name)
    except Category.DoesNotExist:
        return HttpResponseRedirect("/people/")
    return render(request, "main.html", {
        'categories': Category.objects.all(),
        'category': name,
        'displays': Story.objects.filter(category = category),
    })

@login_required
def story(request, name):
    name = name.replace("_", " ")
    try:
        story = Story.objects.get(name = name)
    except Story.DoesNotExist:
        return HttpResponseRedirect("/people/")
    money = 0
    commitments = Commitment.objects.filter(beneficiary = story)
    for commit in commitments:
        money += commit.monthly_amount
    money /= 100
    if story.monthly_goal == 0:
        percent = 100
    elif story.monthly_goal < money:
        percent = 100
    else:
        percent = 1.00*money/story.monthly_goal*100
    try:
        commitment = Commitment.objects.get(donor = request.user, beneficiary = story)
        commit = commitment.monthly_amount/100
    except Commitment.DoesNotExist:
        commit = 0
    return render(request, "charity.html", {
        'categories': Category.objects.all(),
        'source_category': story.category.name,
        'source_charity': story.charity.abbreviation,
        'story': story,
        'current_money': money,
        'current_commitment': commit,
        'percent': percent,
    })

@login_required
def charity(request, name):
    name = name.replace("_", " ")
    try:
        charity = Charity.objects.get(abbreviation = name)
    except Charity.DoesNotExist:
        return HttpResponseRedirect("/charity/")
    return render(request, "charityinfo.html", {
        'categories': Category.objects.all(),
        'source_charity': charity.full_name,
        'pictureurl': charity.icon.url,
        'abbreviation': name,
        'location': charity.location,
        'description': charity.description,
    })

@login_required
def charity_list(request):
    return render(request, "main.html", {
        'categories': Category.objects.all(),
        'category': "All Charities",
        'displays': Charity.objects.all(),
    })

@login_required
def personal(request):
    donor = Donor.objects.get(person = request.user)
    commitments = []
    commits = Commitment.objects.filter(donor = donor)
    total_money = 0
    for commit in commits:
        if commit.monthly_amount == 0:
            continue
        commit_arr = {}
        commit_arr["name"] = commit.beneficiary.name
        commit_arr["amount"] = "$" + ("%.2lf" % (commit.monthly_amount/100))
        commit_arr["charity"] = commit.beneficiary.charity.full_name
        commitments.append(commit_arr)
        total_money += commit.monthly_amount
    return render(request, "profile.html", {
        'name': request.user.first_name,
        'email': request.user.email,
        'image_url': donor.icon.url,
        'commitments': commitments,
        'total': "$" + ("%.2lf" % (total_money/100)),
    })
        
@login_required
def donate(request, name):
    amount = request.POST.get("amount")
    amt = float(amount)
    name = name.replace("_", " ")
    try:
        beneficiary = Story.objects.get(name = name)
    except Story.DoesNotExist:
        return HttpResponseRedirect("/people/")
    try:
        if amt*100 < 0:
            return HttpResponse()
        if amt*100 > 0 and amt*100 < 100: #Don't allow donors to donate less than $1, but allow them to donate $0 to reset
            return HttpResponse()
        commitment = Commitment.objects.get(donor = request.user, beneficiary = beneficiary)
        commitment.monthly_amount = amt*100
        commitment.save()
    except Commitment.DoesNotExist:
        donor = Donor.objects.get(person = request.user)
        commit = Commitment(donor = donor, beneficiary = beneficiary, monthly_amount = amt*100, next_payment = datetime.now())
        commit.save()
    return HttpResponse()

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Correct.")
            else:
                return HttpResponse("Inactive.")
        else:
            return HttpResponse("Wrong.")
    else:
        return HttpResponse()

@login_required
def logout_view(request):
    logout(request)
    return HttpResponse()

def register(request):
    if request.method == "GET":
        if request.user.is_authenticated():
            return HttpResponseRedirect("/")
        else:
            return render(request, "register.html", {})
    else:
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            pass
        else:
            return HttpResponse("Your username has already been used. Please choose another username.")
        try:
            user = User.objects.get(email = email)
        except User.DoesNotExist:
            pass
        else:
            return HttpResponse("Your email has already been used. Please choose another email.")
        new_user = User(username = username, first_name = name, email = email)
        new_user.set_password(password)
        new_user.active = False
        new_user.save()
        donor = Donor(person = new_user, stored_cash = 0)
        donor.save()
        return HttpResponse("You have been registered. Please log in.")