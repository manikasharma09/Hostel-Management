from django.shortcuts import render,redirect
from .forms import UserForm,RegistrationForm,LoginForm,SelectionForm
from django.http import HttpResponse, Http404
from selection.models import Student,Room,Hostel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request,'home.html')

def register(request):
    if request.method=='POST':
    	form=UserForm(request.POST)
    	if form.is_valid():
    		new_user=form.save(commit=False)
    		new_user.save()
    		Student.objects.create(user=new_user)
    		cd=form.cleaned_data
    		user=authenticate(request,username=cd['username'],password=cd['password1'])
    		if user is not None:
    			if user.is_active:
    				login(request,user)
    				return redirect('login/edit/')
    			else:
    			    return HttpResponse('Disabled account')
    		else:
    		    return HttpResponse('Invalid login')
    else:
        form=UserForm()
        args={'form':form}
        return render(request,'reg_form.html',args)
        
def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid();
            cd=form.cleaned_data 
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request,'profile.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})

@login_required
def edit(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST,instance=request.user.student)
        if form.is_valid():
            form.save()
            return render(request,'profile.html')
        else:
            form=RegistrationForm(instance=request.user.student)
            return render(request,'edit.html',{'form':form})  

@login_required
def select(request):
    if request.user.student.room:
        room_id_old=request.user.student.room_id_old
    if request.method=='POST':
        form=SelectionForm(request.POST,instance=request.user.student)
        if form.is_valid():
            if request.user.student.room_id:
                request.user.student.roo,_alloted=True
                                                                        		    	    	


