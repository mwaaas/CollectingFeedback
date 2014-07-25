__author__ = 'mwas'
from django.conf.urls import patterns, url, include


urlpatterns = patterns('customer_feedback.controllers.home',
                       url(r'', 'home'),
                       url(r'^home/', 'home', name='home'),
                       )

urlpatterns += patterns('customer_feedback.controllers.admin',
                        url(r'^admin/login/', 'login', name='admin_login'),
                        url(r'^admin/logout/', 'logout', name='admin_logout'),
                        url(r'^admin/change/password/', 'change_password', name='change_admin_password'),
                        )

urlpatterns += patterns('customer_feedback.controllers.company',

                        url(r'^company/add/', 'add', name='add_company'),
                        url(r'^company/edit/(?P<pk>\d+)/', 'edit', name='edit_company'),
                        url(r'^company/delete/(?P<pk>\d+)/', 'delete', name='delete_company'),
                        url(r'^company/assign/(?P<pk>\d+)/', 'assign', name='assign_company_employee'),
                        url(r'^company/view/$', 'view', name='view_company'),
                        url(r'^company/view/feedback/(?P<company_id>\d+)/', 'feedback',
                            name='view_company_feedback'),



                        )
urlpatterns += patterns('customer_feedback.controllers.employee',
                        url(r'^employee/login/','login', name='employee_login'),
                        url(r'^employee/logout/', 'logout', name='employee_logout'),
                        url(r'^employee/view/', 'view', name='view_employee'),
                        url(r'^employee/add/', 'add', name='add_employee'),
                        url(r'^employee/edit/(?P<pk>\d+)/', 'edit', name='edit_employee'),
                        url(r'^employee/delete/(?P<pk>\d+)/', 'delete', name='delete_employee'),
                        url(r'^employee/company/feedback/(?P<companyId>\d+)/(?P<employeeId>\d+)/', 'feedback',name='company_employee_feedback'),
                        url(r'^employee/assigned/company/(?P<employeeId>\d+)/', 'assigned', name='employeeAssignedCompany'),
                        )
urlpatterns += patterns('customer_feedback.controllers.customer',
                        url(r'^customer/give/feedback/(?P<pk>\d+)/','give_feedback',
                            name='customer_give_feedback')
                        )

