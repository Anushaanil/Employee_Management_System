from django import forms
from .models import Department,Role
from datetime import datetime

class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    #dept_choices = Department.objects.all() #(('1','one'),('2','two'))
    #dept_choices = (('HR','one'),('Finance','two'))
    department = forms.IntegerField()

    salary = forms.IntegerField()
    bonus = forms.IntegerField()

    #role_choices = Role.objects.all()
    #role_choices = (('1','one'),('2','two'))
    role = forms.IntegerField()
    phone = forms.IntegerField()
    hire_date = datetime.now()
