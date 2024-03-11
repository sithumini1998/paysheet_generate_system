from django.db import models


# Create your models here.
class Employee(models.Model):

    employee_id = models.CharField(max_length=20, unique=True,default="")
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Salary(models.Model):
    salary_id=models.CharField(max_length=20, unique=True,default="")
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    join_date = models.DateField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"Salary details for {self.employee.name}"

class StayComponent(models.Model):
    component_id=models.CharField(max_length=20, unique=True,default="")
    salary_detail=models.ForeignKey(Salary, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    is_deduction = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"StayComponent details for {self.salary_detail.salary_id}"