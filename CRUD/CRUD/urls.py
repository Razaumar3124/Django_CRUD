from django.contrib import admin
from django.urls import path
from Employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.employee_form, name='employee_insert'),
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('list/', views.employee_list, name='employee_list'),
    path('delete/<int:id>', views.employee_delete, name="employee_delete")
]
