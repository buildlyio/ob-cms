from django.db import models
from datetime import timedelta
from decimal import Decimal
import uuid

from django.contrib import admin
from django.utils import timezone

from wagtail.core.models import Page

from modelcluster.fields import ParentalKey


class HomePage(Page):
    pass

class AboutPage(Page):
    pass

class Foundry(Page):
    pass

class Contact(Page):
    pass

class Community(Page):
    pass

class BlankPage(Page):
    pass

class DevelopersPage(Page):
    pass

class Bounty(Page):
    pass

class Faq(Page):
    pass

class Products(Page):
    pass

class Privacy(Page):
    pass

class Eula(Page):
    pass

class PartnerAgreement(Page):
    pass

class PartnerPage(Page):
    pass

class PartnerSurvey(Page):
    pass

class Tos(Page):
    pass

class Enterprise(Page):
    pass

class Contract(models.Model):
    party_one = models.CharField(max_length=255, null=True, blank=True)
    party_two = models.CharField(max_length=255, null=True, blank=True)
    hash = models.CharField(max_length=255, null=True, blank=True)
    file = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name


    def save(self, *args, **kwargs):
        # onsave add create date or update edit date
        if self.create_date == None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(Contract, self).save(*args, **kwargs)


class ContractAdmin(admin.ModelAdmin):
    list_display = ('party_one','party_two','create_date','edit_date')
    search_fields = ('party_one','party_two')
    list_filter = ('party_one',)
    display = 'Contract'

class ContactMail(models.Model):
    name = models.CharField(max_length=255, blank=True)
    inquiry = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    email = models.CharField(max_length=255, blank=True)
    file = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, blank=True)
    read = models.BooleanField(default=False)
    spam = models.BooleanField(default=False)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def clean_email(self):
        original_email = self.cleaned_data.get('email')

        if "@" not in original_email:
            raise ValidationError("Invalid Email address")

        if "." not in original_email:
            raise ValidationError("Invalid Email address")

        return original_email

    def save(self, *args, **kwargs):
        # onsave add create date or update edit date
        if self.create_date == None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(ContactMail, self).save(*args, **kwargs)


class ContactMailAdmin(admin.ModelAdmin):
    list_display = ('name','email','url','read','spam','create_date','edit_date')
    search_fields = ('name','email')
    list_filter = ('name',)
    display = 'Contact Form'
