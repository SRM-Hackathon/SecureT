from django.shortcuts import redirect
from . import views

def signup_redirect(request):
	return redirect('/Users/')