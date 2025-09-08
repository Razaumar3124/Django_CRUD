from django.shortcuts import render, redirect, get_object_or_404
from Emp.models import Emp
from Emp.forms import EmpForm

# Create your views here.
def emp_list(request):
    data = Emp.objects.all()
    return render(request, 'Emp_list.html', { 'data' : data })

def emp_form(request):
    form = EmpForm()
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = EmpForm()

    return render(request, 'Emp_form.html', { 'form' : form })

def emp_update(request, pk):
    data = get_object_or_404(Emp, pk=pk)
    if request.method == "POST":
        form = EmpForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = EmpForm(instance=data)

    return render(request, 'Emp_form.html', { 'form' : form })

def emp_delete(request, pk):
    emp = Emp.objects.get(pk=pk)
    emp.delete()
    return redirect('emp_list')