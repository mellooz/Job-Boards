from django.shortcuts import render ,redirect
# paginator
from django.core.paginator import Paginator
from .models import Job
from .form import ApplyForm , JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

# Create your views here.


def job_list(request):
    # called models query set api used to get data from db {  ClassName.objects.all()  }
    job_list = Job.objects.all()

    ## Filters ##
    myfilter = JobFilter(request.GET , queryset=job_list)
    job_list = myfilter.qs

    # paginator
    paginator = Paginator(job_list, 3)  # Show 3 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    # return paginator and Filter in context
    return render(request , 'job/job_list.html' , {'jobs' : page_obj , 'myfilter':myfilter} )


def job_details(request , slug):
    # called (models query set api) used to get data from db {  ClassName.objects.get(ColumnName = param)  }
    job_detail = Job.objects.get(slug=slug)
    
    if request.method == 'POST' :
       form = ApplyForm(request.POST , request.FILES)
       if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else :
        form =ApplyForm()
    return render(request , 'job/job_detail.html' , {'job' : job_detail , 'form' : ApplyForm} )


# decorators : u have function and u want it to pass some constraint to start it
# so when u r logged in add_job function will start
@login_required
def add_job(request):
    if request.method == 'POST' : 
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            # (request.user) refer to the current user
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else :
        form =JobForm()

    return render(request , 'job/add_job.html' , {'form' : form})
