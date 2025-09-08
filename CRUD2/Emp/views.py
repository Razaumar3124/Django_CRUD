from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Emp.models import Emp
from Emp.forms import EmpForm, loginForm

# Create your views here.
def emp_list(request):
    data = Emp.objects.all()
    return render(request, 'Emp_list.html', { 'data' : data })

def emp_form(request):
    form = EmpForm()
    msg = ''
    if request.method == 'POST':
        form = EmpForm(request.POST)
        email = request.POST.get('email')
        if Emp.objects.filter(email=email).exists():
            msg = 'Email Already exists *'
        else:
            form.save()
            return redirect('emp_list')

    else:
        form = EmpForm()

    return render(request, 'Emp_form.html', { 'form' : form , 'msg': msg })


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

def login(request):
    # email = request.POST.get('email')
    # password = request.POST.get('password')
    form = loginForm()
    msg = ''
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if Emp.objects.filter(email=email).exists() and Emp.objects.filter(password=password).exists():
                request.session['email'] = email
                return redirect('logout')
            else:
                msg = 'Wrong credentials'


    return render(request, 'login.html', { 'form': form , 'msg': msg })

def logout(request):
    user = request.session.get('email')
    if request.method == 'POST':
        request.session.delete()
    return render(request, 'logout.html', { 'user': user })