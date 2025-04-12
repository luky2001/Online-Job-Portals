from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import *

def dashboard(request):
    if request.user.is_authenticated:
        recruiter = Recruiter.objects.filter(user=request.user).first()
        return render(request,'dashboard.html',{"stu": recruiter})
    return render(request,'dashboard.html')
def register(request):
    if request.method=="POST":
        data=request.POST
        first=data.get('first_name')
        last=data.get('last_name')
        username=data.get('username')
        password=data.get('password')
        user= User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'User already exist')
            return redirect('/register/')
        user=User.objects.create(
            first_name=first,
            last_name=last,
            username=username
                 )
        user.set_password(password)
        user.save()
        return redirect('/dashboard/')
    return render(request,'register.html')
def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid User')
            return redirect('/login_page/')
        user=authenticate(request,username=username , password=password)
        if user is None:
            messages.error(request,'Invalid User')
            return redirect('/login_page/')
        else:
            login(request,user)
            messages.success(request,'Logged In Successfully')
            return redirect('/dashboard/')
    return render(request,'login.html')
def logout_page(request):
    logout(request)
    return redirect ('/')
@login_required(login_url='/login_page/')
def rec_profile(request):
    recruiter = Recruiter.objects.filter(user=request.user).first()
    if recruiter:
        return redirect('/view_profile/')
    if request.method == "POST":
        data = request.POST
        c_logo = request.FILES.get('logo')
        recruiter = Recruiter.objects.create(
            user=request.user, 
            company_name=data.get('c_name'),
            company_logo=c_logo,
            com_location=data.get('c_location'), 
            com_industry=data.get('c_industry'),  
            com_description=data.get('c_description') 
        )
        return redirect('/view_profile/')
    return render(request, 'rec_profile.html')
@login_required(login_url='/login_page/')
def view_profile(request):
    queryset=Recruiter.objects.filter(user=request.user).first()
    if not queryset:
        return redirect('/rec_profile/')
    return render(request,'view_profile.html',{'stu':queryset})
def update_rec_profile(request, id):
    queryset = get_object_or_404(Recruiter, id=id)
    if request.method == 'POST':
        data = request.POST
        c_logo = request.FILES.get('logo')
        queryset.company_name = data.get('c_name', queryset.company_name)
        queryset.com_location = data.get('c_location', queryset.com_location)
        queryset.com_industry = data.get('c_industry', queryset.com_industry)
        queryset.com_description = data.get('c_description', queryset.com_description)
        if c_logo:
            queryset.company_logo = c_logo 
        queryset.save()
        return redirect('/rec_profile/')
    return render(request, 'update_rec_profile.html', {'queryset': queryset})
@login_required(login_url='/login_page/')
def job(request):
    recruiter = Recruiter.objects.filter(user=request.user).first()
    if request.method=="POST":
        job_position = request.POST.get('job_position')
        job_description = request.POST.get('job_description')
        job_category = request.POST.get('job_category')
        job_location = request.POST.get('job_location')
        job_salary = request.POST.get('job_salary')
        job_experience = request.POST.get('job_experience')
        qualifications = request.POST.get('qualifications')
        job_type = request.POST.get('job_type')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status')
        Job.objects.create(
            recruiter=request.user.recruiter, 
            job_position=job_position,
            job_description=job_description,
            job_category=job_category,
            job_location=job_location,
            job_salary=job_salary,
            job_experience=job_experience,
            qualifications=qualifications,
            job_type=job_type,
            deadline=deadline if deadline else None,
            status=status
        )
        return redirect('/show/')
    return render(request,'job.html',{'stu':recruiter})
@login_required(login_url='/login_page/')
def show(request):
    recruiter = request.user.recruiter
    jobs = Job.objects.filter(recruiter=recruiter)
    recruiter = Recruiter.objects.filter(user=request.user).first()
    return render(request,'show.html',{'jobs':jobs,'stu':recruiter})
def job_update(request,id):
    queryset = get_object_or_404(Job, id=id)
    recruiter = Recruiter.objects.filter(user=request.user).first()
    if request.method=="POST":
        queryset.job_position = request.POST.get('job_position')
        queryset.job_description = request.POST.get('job_description')
        queryset.job_category = request.POST.get('job_category')
        queryset.job_location = request.POST.get('job_location')
        queryset.job_salary = request.POST.get('job_salary')
        queryset.job_experience = request.POST.get('job_experience')
        queryset.qualifications = request.POST.get('qualifications')
        queryset.job_type = request.POST.get('job_type')
        queryset.deadline = request.POST.get('deadline') or None
        queryset.status = request.POST.get('status')
        queryset.save()
        return redirect('/show/')
    print(queryset.job_position)
    return render(request,'job_update.html',{'queryset':queryset,'stu':recruiter})
def job_delete(request,id):
    queryset=get_object_or_404(Job,id=id)
    queryset.delete()
    return redirect('/show/')
def condidate_register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Condidate Already exist')
            return redirect('/condidate_login/')
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        return redirect('/home_dashboard/')
    return render(request,'condidate_register.html')
def condidate_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Condidate')
            return redirect('/condidate_register/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid Condidate')
            return redirect('/condidate_login/')
        else:
            login(request,user)
            return redirect('/condidate_dashboard/')
    return render(request,'condidate_login.html')
def condidate_logout(request):
    logout(request)
    return redirect('/home_dashboard/')
def condidate_dashboard(request):
    return render(request,'condidate_dashboard.html')
def home_dashboard(request):
    return render(request,'home_dashboard.html')
def show_jobs(request)