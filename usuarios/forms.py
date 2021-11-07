from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from onlineshop.models import Product, Category

User = get_user_model()
class UserForm(UserCreationForm):

    class Meta:
        model = User
        #fields = ('username','email','first_name','imagen','edad','privilegio')
        fields = ('username','email','first_name','last_name','imagen','edad','privilegio','tienda')
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = True


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50,
            widget = forms.TextInput(attrs = {
                'type' : 'password'
            }))

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    edad = forms.IntegerField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    imagen = forms.ImageField(required = True,widget=forms.FileInput(attrs={'class': 'form-control-file'}))


    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','edad','imagen']

class AddProduct(forms.ModelForm):
    
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.SlugField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=500,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    avaible = forms.BooleanField(required=True,
                               widget=forms.CheckboxInput(attrs={'class': 'form-control'}))

    inventory = forms.IntegerField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    image = forms.ImageField(required = True,widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Product
        fields = ['category','name', 'slug','description','price','avaible','inventory','image']
