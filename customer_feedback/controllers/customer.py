from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from customer_feedback import models, Form

__author__ = 'mwas'


def give_feedback(request, pk):
    feedback = models.Feedback.objects.filter(company_id=pk)
    company = models.Company.objects.get(pk=pk)
    addFeedbackForm = Form.AddFeedbackForm()

    if request.method == 'POST':
        addFeedbackForm = Form.AddFeedbackForm(request.POST)
        if addFeedbackForm.is_valid():
            models.Feedback(company=company, fname=request.POST['fname'],
                            lname=request.POST['lname'],
                            phoneNumber=request.POST['phoneNumber'],
                            comment=request.POST['comment']
                            ).save()
            addFeedbackForm = Form.AddFeedbackForm()

    return render_to_response('companyFeedback.html',
                              {'feedback':feedback, 'company':company, 'addFeedbackForm':addFeedbackForm},
                              context_instance = RequestContext(request),
                              )

