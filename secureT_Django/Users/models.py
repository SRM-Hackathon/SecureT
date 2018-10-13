from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=30)
	mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	mobile_number = models.CharField(validators=[mobile_regex], max_length=17, blank=True) 
	password=models.CharField(max_length=12)
	
	
		
