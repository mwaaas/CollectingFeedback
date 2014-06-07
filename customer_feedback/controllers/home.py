from django.shortcuts import render_to_response
from django.template import RequestContext
from customer_feedback import models

__author__ = 'mwas'

def home(request):
    companies = models.Company.objects.all()
    return render_to_response('home.html',{'companies':companies}, context_instance=RequestContext(request))