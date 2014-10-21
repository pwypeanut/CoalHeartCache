from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 20)
    icon = models.ImageField(upload_to = "/home/django/chc/coalheartcache/static/categoryicons/")
    description = models.TextField()
    def __unicode__(self):
        return self.name

class Charity(models.Model):
    manager = models.ForeignKey(User)
    full_name = models.CharField(max_length = 50)
    abbreviation = models.CharField(max_length = 10)
    location = models.CharField(max_length = 30)
    description = models.TextField()
    icon = models.ImageField(upload_to = "/home/django/chc/coalheartcache/static/charityicon/")
    stored_cash = models.IntegerField()
    def __unicode__(self):
        return self.full_name + "(" + self.abbreviation + ")"

class Story(models.Model):
    category = models.ForeignKey(Category)
    charity = models.ForeignKey(Charity)
    name = models.CharField(max_length = 50)
    icon = models.ImageField(upload_to = "/home/django/chc/coalheartcache/static/beneficiaryicon/")
    monthly_goal = models.IntegerField()
    description = models.TextField()
    def __unicode__(self):
        return self.charity.abbreviation + " - " + self.name

class Donor(models.Model):
    person = models.ForeignKey(User)
    icon = models.ImageField(upload_to = "/home/django/chc/coalheartcache/static/donoricons/", default = "/home/django/chc/coalheartcache/static/donoricons/kitty.png")
    stored_cash = models.IntegerField()
    def __unicode__(self):
        return self.person.username

class Donation(models.Model):
    donor = models.ForeignKey(Donor)
    beneficiary = models.ForeignKey(Story)
    amount = models.IntegerField()
    time = models.DateTimeField()
    def __unicode__(self):
        return self.donor.person.username + " donates US$" + str(self.amount/100) + " to " + self.beneficiary.beneficiary_name

class Commitment(models.Model):
    donor = models.ForeignKey(Donor)
    beneficiary = models.ForeignKey(Story)
    monthly_amount = models.IntegerField()
    next_payment = models.DateTimeField()
    class Meta:
        unique_together = ("donor", "beneficiary")
    def __unicode__(self):
        return self.donor.person.username + " commits US$" + str(self.monthly_amount/100) + " to " + self.beneficiary.name
        
class Comment(models.Model):
    beneficiary = models.ForeignKey(Story)
    commenter = models.ForeignKey(Donor)
    reply_to = models.ForeignKey("self")
    message = models.TextField()
    time = models.DateTimeField()
    def __unicode__(self):
        return self.message + ", commented by " + self.commenter.person.username + " in story " + self.beneficiary.beneficiary_name