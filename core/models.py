from django.db import models




class AboutUs(models.Model):
    description = models.TextField()
    

    def __str__(self):
        return "About Us"
    

class ContactInformation(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "Contact Information"
    