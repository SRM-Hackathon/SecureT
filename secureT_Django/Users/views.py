from django.shortcuts import render , redirect, HttpResponseRedirect
from .models import User

# Create your views here.

def signup(request):
	if request.method == 'POST':
		users = User(username=request.POST['username'], mobile_number=request.POST['mobile'], password=request.POST['password'])
		users.save()
		return redirect('/')
	else:
		return render(request,'Users/signup.html')
def login(request):
	return render(request, 'Users/login.html')

def hello(request):
	if request.method == 'POST':
		if User.objects.filter()(mobile_number=request.POST['mobile_number'], password=request.POST['password']).exists():
			users = User.objects.get(mobile_number=request.POST['mobile_number'], password=request.POST['password'])
			return render(request, 'Users/hello.html')
		else:
			context = {'msg':'Invalid username or password'}
			return render(request, 'Users/login.html', context)

