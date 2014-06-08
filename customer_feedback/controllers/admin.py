import logging
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from customer_feedback import Form, models

__author__ = 'mwas'
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def login(request, message=None):
    logger.info("message:"+str(message))
    adminLoginForm = Form.admin_login_form()
    if request.method == 'GET':
        return render_to_response('adminLogin.html',
                           {'adminLoginForm':adminLoginForm},
                           context_instance=RequestContext(request),
                           )
    if request.method == 'POST':
        adminLoginForm = Form.admin_login_form(request.POST)

        #this validates and check if the password is valid
        if adminLoginForm.is_valid():
            request.session['admin']='admin'
            return HttpResponseRedirect(reverse('view_company'))

    return render_to_response('adminLogin.html',
                           {'adminLoginForm':adminLoginForm, 'message':message},
                           context_instance=RequestContext(request),

                           )

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('home'))

def change_password(request):
    if not request.session.get('admin',False):
        return HttpResponseRedirect(reverse('admin_login'))
    change_admin_password_form = Form.change_password_form()
    if request.method == 'POST':
        change_admin_password_form = Form.change_password_form(request.POST)
        if change_admin_password_form.is_valid():
            #save the new password
            try:
                admin_password = models.Admin.objects.get(admin_name='admin_name')
            except models.Admin.DoesNotExist:
                admin_password = models.Admin(admin_name='admin_name', password='')
            admin_password.password = request.POST['new_password']
            admin_password.save()

            return HttpResponseRedirect(reverse('admin_login'))

    return render_to_response('change_password.html',
                           {'change_admin_password_form':change_admin_password_form},
                           context_instance=RequestContext(request))

