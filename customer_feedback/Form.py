__author__ = 'mwas'
__author__ = 'mwas'
from django import forms
from customer_feedback import models

class admin_login_form(forms.Form):

    password = forms.CharField(required=False,
                               label="Password",
                               max_length=255,
                               widget=forms.PasswordInput,

                               )
    def clean(self):
        clean_data = super(admin_login_form, self).clean()
        try:
            current_password =models.Admin.objects.get(admin_name="admin_name").password
        except models.Admin.DoesNotExist:
            current_password = ''

        #if current_password == None:
        #    #models.Admin(admin_name='admin_name', passwod = None).save()
        #    models.Admin.objects.create(admin_name="admin_name", password='password')
        try:
            if clean_data['password']!= current_password:
                self.errors['password'] = ["invalid password try again"]

        except KeyError:
            raise KeyError
        
class change_password_form(forms.Form):
     current_password = forms.CharField(required=False,
                               label="Current password",
                               max_length=255,
                               widget=forms.PasswordInput,
                               )
     new_password = forms.CharField(required=True,
                               label="New password",
                               max_length=255,
                               widget=forms.PasswordInput,
                               )

     def clean(self):
         clean_data = super(change_password_form, self).clean()

         try:
             current_password =models.Admin.objects.get(admin_name="admin_name").password
         except models.Admin.DoesNotExist:
             current_password = ''

         try:
             if clean_data['current_password'] != current_password:
                 self.errors['current_password'] = ["The password is not the same to the current password"]


         except KeyError:
             raise KeyError

class AddEmployeeForm(forms.ModelForm):

    class Meta:
        model = models.Employee

class AddCompanyForm(forms.ModelForm):

    #logo = forms.CharField(label="Logo",
                           #widget=forms.ImageField)
    description = forms.CharField(label="Description", required=True,
                                  widget=forms.Textarea)
    class Meta:
        model = models.Company

class AssignEmployee(forms.Form):
    all_employees = models.Employee.objects.all()

    choice = []
    for i in all_employees:
        choice.append([i.pk, i.fname])

    choose_employee = forms.ChoiceField(choices=choice)
    #choose_employee =forms.ModelChoiceField(models.Employee.objects.all())

class AssingForm(forms.Form):
    def __init__(self,companyId,*args, **kwargs):
        self.company_id = companyId
        super(AssingForm, self).__init__(*args, **kwargs)

        #employees that are not assigned

        self.fields['choose_employee'] = forms.ModelChoiceField(models.Employee.objects.exclude(assigned__companyName_id = self.company_id))


    #choose_employee =forms.ModelChoiceField(models.Employee.objects.exclude(assigned__companyName_id = self.company_id))



class EmployeeLoginForm(forms.Form):
    fname = forms.CharField(max_length=255,
                            required=True, label='First name')
    lname = forms.CharField(max_length=255,
                            required=True, label='Last name')
    password = forms.CharField(max_length=255,
                               required=True, label="Password",
                               widget=forms.PasswordInput)
    def clean(self):
        if any(self.errors):
            return
        clean_data= super(EmployeeLoginForm, self).clean()
        record_exists=a = models.Employee.objects.\
            filter(fname=clean_data['fname'], lname=clean_data['lname'],
                   password=clean_data['password']).exists()

        #since the fname and lname are unique in Employee if t
        #they exit then its only one record and the login is valid
        if not record_exists:
            if not models.Employee.objects.\
                filter(fname=clean_data['fname']).exists():
                self.errors['fname'] = ["Invalid first name"]

            elif not models.Employee.objects.filter(lname=clean_data['lname']).\
                exists():
                self.errors['lname'] = ["Invalid last name"]

            elif not models.Employee.objects.filter(password=clean_data['password']).\
                exists():
                self.errors['password'] = ["Invalid password"]

class AddFeedbackForm(forms.Form):
    fname = forms.CharField(label="First name", max_length=255, required=True)
    lname = forms.CharField(label="Last name", max_length=255, required=True)
    phoneNumber = forms.CharField(label="Phone number", max_length=255, required=True)
    comment = forms.CharField(label="Comment", required=True, widget=forms.Textarea)



























