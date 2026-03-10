from django.shortcuts import render
from .ai_modules.resume_parser import analyze_resume
from .ai_modules.interview_generator import generate_questions
from django.contrib.auth.decorators import login_required
from .ai_modules.career_roadmap import generate_roadmap
from .ai_modules.job_matcher import match_resume_job


def home(request):
    return render(request,"dashboard.html")


@login_required
def resume_analyzer(request):

    result = None

    if request.method == "POST":

        resume = request.FILES['resume']

        result = analyze_resume(resume)

    return render(request,"resume_analyzer.html",{"result":result})


@login_required
def interview_generator_view(request):

    questions = None

    if request.method == "POST":

        role = request.POST['role']

        questions = generate_questions(role)

    return render(request,"interview_generator.html",{"questions":questions})

from .models import JobApplication


@login_required
def job_tracker(request):

    if request.method == "POST":

        company = request.POST['company']
        role = request.POST['role']
        status = request.POST['status']

        JobApplication.objects.create(
            company=company,
            role=role,
            status=status
        )

    jobs = JobApplication.objects.all()

    return render(request,"job_tracker.html",{"jobs":jobs})

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


def register_user(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)

        return redirect('/login')

    return render(request,'register.html')


def login_user(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')

    return render(request,'login.html')


def logout_user(request):

    logout(request)

    return redirect('/login')

def career_roadmap(request):

    roadmap = None

    if request.method == "POST":

        role = request.POST['role']

        roadmap = generate_roadmap(role)

    return render(request,"career_roadmap.html",{"roadmap":roadmap})

def job_matcher(request):

    result = None

    if request.method == "POST":

        resume = request.FILES['resume']

        job_description = request.POST['job_description']

        result = match_resume_job(resume, job_description)

    return render(request,"job_matcher.html",{"result":result})