from django.shortcuts import render
from django.views import View
from .models import Login

class LoginView(View):
    def get(self,request):
        return render(request,'input.html');
    
    def post(self,request):
        newUserName=request.POST.get('username')
        password=request.POST.get('password')
        if Login.objects.filter(userName=newUserName).exists():
           Output='User Already exists'
        else:
           Login.objects.create(userName=newUserName,password=password)
           Output='New User Created'
        
        return render(request,'output.html',{'Output': Output})
        
