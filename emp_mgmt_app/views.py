from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from django.db import models
from . add_emp_form import EmployeeForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'index.html')

def view_emp(request):
    emps = Employee.objects.all()

    context = {
        'emps':emps
    }

    #print(context)

    return render(request,'view_emp.html',context)

def add_emp(request):
    #fields_count = len(Employee._meta.get_fields())-1
    if request.method == 'POST':
        # form = request.POST.dict()
        # print(form.get('firstname'))
        form = EmployeeForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            dept = form.cleaned_data['department']
            salary = form.cleaned_data['salary']
            bonus = form.cleaned_data['bonus']
            role = form.cleaned_data['role']
            phone = form.cleaned_data['phone']
            hire_date = EmployeeForm.hire_date

            emp = Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,
            bonus=bonus,role_id=role,phone=phone,hire_date=hire_date)
            print(emp)
            emp.save()

            return HttpResponseRedirect('/view_emp')

    else:
        form = EmployeeForm()

    return render(request,'add_emp.html',{'form':form})

def remove_emp(request,id=0):
    if id:
        try:
            emp_to_be_removed = Employee.objects.get(id=id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee removed successfully!')

        except:
            return HttpResponse('iD not valid!')

    emps  = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        emps  = Employee.objects.all()
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
        context = {
            'emps':emps
        }
        return render(request,'view_emp.html',context)
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('exception occured!')

@login_required(login_url='/admin')
def update_emp(request):
    return render(request, 'update_emp.html',{})
