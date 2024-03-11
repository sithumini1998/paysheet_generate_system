from django.forms import ModelForm
from .models import Employee,Salary,StayComponent
from django import forms

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class SalaryForm(ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'


class ComponentForm(ModelForm):
    class Meta:
        model = StayComponent
        fields = '__all__'