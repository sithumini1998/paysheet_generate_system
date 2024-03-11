from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('add-employee/', views.addEmployee, name="add-emp"),
    path('view-employee/', views.employees, name="employees"),
    path('edit-employee/<str:pk>/', views.editEmployee, name="edit-emp"),
    path('delete-employee/<str:pk>/', views.deleteEmployee, name="delete-emp"),
    path('add-salary/', views.addSalaryDetails, name="add-slry"),
    path('view-salary-details/', views.viewSalaryDetails, name="viewSalaryDetails"),
    path('edit-salaryinfor/<str:pk>/', views.editSalaryDetails, name="edit-salary"),
    path('delete-salaryinfor/<str:pk>/', views.deleteSalaryDetails, name="delete-salary"),
    path('add-component/', views.addComponents, name="add-cmp"),
    path('view-component/', views.viewComponentDetails, name="viewComponentDetails"),
    path('edit-componentinfor/<str:pk>/', views.editComponentDetails, name="edit-component"),
    path('delete-componentinfor/<str:pk>/', views.deleteComponentDetails, name="delete-component"),
    path('generate-salary-pdf/<str:employee_id>/', views.generate_salary_pdf, name='generate_salary_pdf'),

]