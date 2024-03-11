from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm, SalaryForm,ComponentForm
from .models import Employee, Salary, StayComponent
from django.db.models import Q
from datetime import datetime

from django.http import HttpResponse
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders



# Create your views here.
def home(request):
    if request.method == 'GET':
        query_employee_id = request.GET.get('employee_id')
        query_employee_name = request.GET.get('employee_name')
        query_month = request.GET.get('month')

        employees = Employee.objects.all()

        if query_employee_id:
            employees = employees.filter(employee_id__icontains=query_employee_id)
        if query_employee_name:
            employees = employees.filter(name__icontains=query_employee_name)
        if query_month:
            employees = employees.filter(salary__join_date__month=datetime.strptime(query_month, '%B').month)

        context = {'employees': employees}
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
#def home(request):
    #return render(request, 'home.html')


def addEmployee(request):
    form = EmployeeForm
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')
    context = {'form': form}
    return render(request, 'add-employee.html', context)

def employees(request):
    form = Employee.objects.all()
    context = {'form':form}
    return render(request, 'view-employee.html', context)


def editEmployee(request, pk):
    employeesab = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employeesab)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employeesab)
        if form.is_valid():
            form.save()
            return redirect('employees')
    context = {'form': form}
    return render(request, 'edit-employee.html', context)

def deleteEmployee(request, pk):
    employee_data = Employee.objects.get(id=pk)
    employee_data.delete()
    return redirect('employees')


def addSalaryDetails(request):
    employees = Employee.objects.all()
    form = SalaryForm
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form ,'employees':employees}
    return render(request, 'add-salary.html', context)

def viewSalaryDetails(request):
    form = Salary.objects.all()
    context = {'form':form}
    return render(request, 'view-salary-details.html', context)

def editSalaryDetails(request, pk):
    salaryinfor = Salary.objects.get(id=pk)
    form = SalaryForm(instance=salaryinfor)

    if request.method == "POST":
        form = SalaryForm(request.POST, instance=salaryinfor)
        if form.is_valid():
            form.save()
            return redirect('viewSalaryDetails')
    context = {'form': form}
    return render(request, 'edit-salary-details.html', context)

def deleteSalaryDetails(request, pk):
    salary_data = Salary.objects.get(id=pk)
    salary_data.delete()
    return redirect('viewSalaryDetails')


def addComponents(request):
    salaries = Salary.objects.all()
    form = ComponentForm
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form ,'salaries':salaries}
    return render(request, 'add-stay-components.html', context)

def viewComponentDetails(request):
    form = StayComponent.objects.all()
    context = {'form':form}
    return render(request, 'view-component.html', context)

def editComponentDetails(request, pk):
    componentinfor = StayComponent.objects.get(id=pk)
    form = ComponentForm(instance=componentinfor)

    if request.method == "POST":
        form = ComponentForm(request.POST, instance=componentinfor)
        if form.is_valid():
            form.save()
            return redirect('viewComponentDetails')
    context = {'form': form}
    return render(request, 'edit-component.html', context)

def deleteComponentDetails(request, pk):
    component_data = StayComponent.objects.get(id=pk)
    component_data.delete()
    return redirect('viewComponentDetails')

def generate_salary_pdf(request, employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    salary = employee.salary_set.latest('join_date')
    stay_components = StayComponent.objects.filter(salary_detail=salary)

    basic_salary = salary.basic_salary
    gross_salary = basic_salary

    # Calculate gross salary based on deductions
    for component in stay_components:
        if component.is_deduction:
            gross_salary -= component.amount
        else:
            gross_salary += component.amount

    context = {
        'employee': employee,
        'salary': salary,
        'stay_components': stay_components,
        'gross_salary': gross_salary,
    }

    template_path = 'salary_pdf_template.html'
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="salary_calculation_{employee_id}.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('PDF generation failed')

    return response