from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from customer_feedback import models, Form

__author__ = 'mwas'


def view(request):
    all_companies = models.Company.objects.all()
    return render_to_response('company.html',
                              {'companies':all_companies},
                              context_instance=RequestContext(request)
                              )


def add(request):
    if not request.session.get('admin',False):
        return HttpResponseRedirect(reverse('admin_login'))
    add_company_form = Form.AddCompanyForm()
    if request.method == 'POST':
        add_company_form = Form.AddCompanyForm(request.POST, request.FILES)
        if add_company_form.is_valid():
            add_company_form.save()
            return HttpResponseRedirect(reverse('view_company'))
    return render_to_response('addCompany.html', {'add_company_form':add_company_form},
                              context_instance = RequestContext(request)
                              )

def edit(request, pk):
    if not request.session.get('admin',False):
        return HttpResponseRedirect(reverse('admin_login'))
    company = models.Company.objects.get(pk=pk)
    edit_company_form = Form.AddCompanyForm(instance=company)
    if request.method == 'POST':
        edit_company_form = Form.AddCompanyForm(request.POST,instance=company)
        if edit_company_form.is_valid():
            edit_company_form.save()
            return HttpResponseRedirect(reverse('view_company'))
    return render_to_response('editCompany.html',
                              {'edit_company_form':edit_company_form, 'companyId':pk},
                              context_instance = RequestContext(request)
                              )

def assign(request, pk):
    if not request.session.get('admin',False):
        return HttpResponseRedirect(reverse('admin_login'))
    companyName = models.Company.objects.get(pk=pk)

    assign_form = Form.AssignEmployee()

    #assign_form = Form.AssingForm(companyId=pk)
    if request.method == 'POST':
        #data = request.POST.copy()
        #data['companyId'] = pk
        #assign_form = Form.AssingForm(data)
        assign_form = Form.AssignEmployee(request.POST)


        if assign_form.is_valid():
            company_instance=models.Company.objects.get(pk=pk)
            employee_instance=models.Employee.objects.get(pk=request.POST['choose_employee'])
            models.Assigned(companyName=company_instance, employee=employee_instance).save()

            return HttpResponseRedirect(reverse('view_company'))
    return render_to_response('assignCompany.html', {'assign_form':assign_form,
                                                     'companyId':pk},
                              context_instance=RequestContext(request)
                              )

def delete(request, pk):
    if not request.session.get('admin',False):
        return HttpResponseRedirect(reverse('admin_login'))
    models.Company.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('view_company'))

def feedback(request, company_id):
    feedback= models.Feedback.objects.filter(company_id=company_id)
    company = models.Company.objects.get(pk=company_id)

    return render_to_response('companyAdminFeedback.html',{'feedback':feedback, 'company':company},
                              context_instance = RequestContext(request),
                              )
