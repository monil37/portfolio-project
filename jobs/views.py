# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from .models import Job

# Create your views here.
def home(request):
    jobs=Job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})

def details(request,job_id):
    job_detail=get_object_or_404(Job,pk=job_id)
    return render(request,'jobs/detail.html',{'job':job_detail})