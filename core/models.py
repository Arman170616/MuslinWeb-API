from django.db import models




class AboutUs(models.Model):
    description = models.TextField()
    

    def __str__(self):
        return "About Us"