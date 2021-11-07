from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView
from .forms import LoginForm, UserForm, UpdateUserForm, AddProduct
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from cart.models import Address
from onlineshop.models import Product
User = get_user_model()

class CrearUsuario(FormView):
    template_name = 'register.html'
    fields = '__all__'
    success_url = '/register/login/'

    def get(self, request, *args, **kwargs):
        form = UserForm()
        context = {"form":form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #post.slug = slugify(post.title)
            form.save()

        context = {"form":form}
        return render(request, self.template_name, context)
    #form_class = UserForm
    #template_name = 'register.html'
    #success_url =  '/register/'

    #def form_valid(self, form):
    #    form.save()
    #    return super(CrearUsuario, self).form_valid(form)



class IndexView(FormView):
    model = User
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/register/login/'

    def form_valid(self, form):
        user = authenticate(request = self.request,username = form.cleaned_data['username'],
        password = form.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
        return super(IndexView, self).form_valid(form)


@login_required(login_url='/register/login/')
def profile(request):
    if request.method == 'POST':
        #user_form = UpdateUserForm(request.POST, instance=request.user)
        userform = UpdateUserForm(request.POST, request.FILES,instance=request.user)
        user_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid() and userform.is_valid():
            userform.save()
            user = user_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Tu información fue actualizada correctamente')
            return redirect('/register/update')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        userform = UpdateUserForm(instance=request.user)
        user_form = PasswordChangeForm(request.user)
    return render(request, 'update.html', {'user_form': user_form,'userform': userform})

def LogOut(request):
    logout(request)
    return redirect('/')
#def register(request):

 #   return render(request, "usuarios/register.html")
@login_required(login_url='/register/login/')
def reporte(request):
    data1 = Address.objects.filter(tienda__startswith='M')
    data2 = Address.objects.filter(tienda__startswith='T')
    data3 = Address.objects.filter(tienda__startswith='E')
    data = Address.objects.all()
    stu = {
    "student_number": data,
    "student_number1": data1,
    "student_number2": data2,
    "student_number3": data3
    }
    return render(request, 'reporte.html', stu)

#@login_required(login_url='/register/login/')
class add_product(FormView):
    template_name = 'productos.html'
    fields = '__all__'
    success_url = '/register/productos/'

    def get(self, request, *args, **kwargs):
        form = AddProduct()
        context = {"form":form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #post.slug = slugify(post.title)
            form.save()

        context = {"form":form}
        return render(request, self.template_name, context)

@login_required(login_url='/register/login/')
def inventario(request):
    data1 = Product.objects.filter(tienda__startswith='M')
    data2 = Product.objects.filter(tienda__startswith='T')
    data3 = Product.objects.filter(tienda__startswith='E')
    data = Product.objects.all()
    stu = {
    "student_number": data,
    "student_number1": data1,
    "student_number2": data2,
    "student_number3": data3
    }
    return render(request, 'inventario.html', stu)