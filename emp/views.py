from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import *


# Create your views here.
class RegisterView(FormView):

    def get(self, request):
        content = {}
        content['form'] = RegistrationForm(initial={'reporting':request.user.username})
        return render(request, 'emp/reg_form.html', content)


    def post(self, request):
        content = {}
        form = RegistrationForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.created_by = request.user.username
            user.save()
            # return redirect('add-salary',user.id)
            return render(request, 'emp/add_salary.html',{'user':user})
        content['form'] = form
        template = 'emp/reg_form.html'
        return render(request, template, content)


# LOGIN
class LoginView(FormView):
    content = {}
    content['form'] = LoginForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            return redirect(reverse('dashboard-view'))
        content['form'] = LoginForm
        return render(request, 'emp/login.html', content)

    def post(self, request):
        content = {}
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = authenticate(request, username=email, password=password)
            login(request, user)
            return redirect(reverse('dashboard-view'))
        except Exception as e:
            messages.error(request,  "can't login use this credential. Try again ")
            return HttpResponseRedirect(reverse_lazy('login-view'))

# LOGOUT
class LogoutView(FormView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('login-view'))

@login_required
def UserDashboard(request):
    users = User.objects.all()
    return render(request,  'emp/dashboard.html',context={'users':users})

    
@login_required
def user_details(request,id):
    user = User.objects.get(id=id)
    return render(request,'emp/user_detail.html',{'user':user})

@login_required
def user_delete(request,id):
    user = User.objects.get(id = id).delete()
    return redirect('dashboard-view')

@login_required
def users_update(request,id): 
    user = User.objects.get(id = id)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if form.clean['first_name']:
                user.first_name =form.clean['first_name']

            if form.clean['last_name']:
                user.last_name =form.clean['last_name']

            if form.clean['mobile_no']:
                user.mobile_no =form.clean['mobile_no']
            user.save()
            return redirect('dashboard-view')
    else:
        form = UserForm(instance=user)
        return render(request,'emp/update.html',{'form':form})