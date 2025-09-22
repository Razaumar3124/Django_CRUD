from django.shortcuts import render, redirect, get_object_or_404
from Emp.models import Emp
from Emp.forms import EmpForm, LoginForm

# Create your views here.
def emp_list(request):
    data = Emp.objects.all()
    return render(request, 'emp_list.html', { 'data': data })

def emp_form(request):
    form = EmpForm()
    msg = ''

    if request.method == 'POST':
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        if Emp.objects.filter(mobile=mobile).exists():
            msg = 'Mobile no. already exists'

        elif Emp.objects.filter(email=email).exists():
            msg = 'Email already exists'

        else:
            form = EmpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('emp_list')
    else:
        form = EmpForm()

    return render(request, 'emp_form.html', {'form': form, 'msg': msg})

def emp_update(request, pk):
    user = get_object_or_404(Emp, pk=pk)
    if request.method == 'POST':
        form = EmpForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('emp_list')

    else:
        form = EmpForm(instance=user)

    return render(request, 'emp_form.html', { 'form': form })

def emp_delete(request, pk):
    user = get_object_or_404(Emp, pk=pk)
    user.delete()
    return redirect('emp_list')

def login(request):
    form = LoginForm()
    msg = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if Emp.objects.filter(email=email).exists() and Emp.objects.filter(password=password).exists():
                request.session['email'] = email
                return redirect('logout')
            else:
                msg = 'Invalid Credentials'

    return render(request, 'loginPage.html', { 'form': form, 'msg': msg })

def logout(request):
    user = request.session.get('email')
    if request.method == 'POST':
        request.session.delete()

    return render(request, 'logout.html', { 'user': user })