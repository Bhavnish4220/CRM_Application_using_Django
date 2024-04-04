from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CreateUserForm,LoginForm,CreateRecordForm,UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from . models import Record
from django.contrib import messages

#home

def home(request):
    return render(request,'webapp/index.html')

# register
def register(request):
    form =CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('login_page')
    
    context={'form':form}
    return render(request,'webapp/register.html',context=context)

#login
def my_login(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
    context={'form':form}
    return render(request,'webapp/login_page.html',context=context)

#LOGOUT
def user_logout(request):
    auth.logout(request)
    messages.success(request,'Logout successfully')
    return redirect('login_page')

#dashboard

@login_required(login_url='Login')
def dashboard(request):
    my_records=Record.objects.all()
    context={'records':my_records}
    return render(request,'webapp/dashboard.html',context=context)

#create record
@login_required(login_url='Login')
def create_record(request):
    form=CreateRecordForm
    if request.method=="POST":
        form=CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('dashboard')
    context={'form':form}
    return render(request,'webapp/create_rec.html',context=context)

#UPDATE RECORD

@login_required(login_url='Login')
def update_record(request,pk):
    record=Record.objects.get(id=pk)
    form=UpdateRecordForm(instance=record)
    if request.method=='POST':
        form=UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated successfully')
            return redirect('dashboard')
    context={'form':form}
    return render(request,'webapp/update_rec.html',context=context)

#view a single record

@login_required(login_url='Login')
def single_record(request,pk):
    all_records=Record.objects.get(id=pk)
    context={'record':all_records}
    return render(request,'webapp/view_rec.html',context=context)


#delete record
@login_required(login_url='Login')
def delete_record(request,pk):
    record=Record.objects.get(id=pk)
    record.delete()
    messages.success(request,'Record deleted successfully')
    return redirect('dashboard')