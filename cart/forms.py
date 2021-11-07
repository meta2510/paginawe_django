from django import forms
from .models import Address, Payment
from django.forms import ModelForm



PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,21)]
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput())

class CheckOutForm(forms.ModelForm):
    METODO_PAGO = (
    ('Efectivo', 'Efectivo'),
    ('POS MOVIL', 'POS MOVIL')
)

    TIENDAS = (
        ('Miraflores', 'Miraflores'),
        ('Tikal Futura', 'Tikal Futura'),
        ('Eskala Roosevelt', 'Eskala Roosevelt'),
    )
    nombre_completo = forms.CharField(max_length=50,required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(max_length=100)
    municipio = forms.CharField(max_length=100)
    departamento = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=8)
    metodo_pago = forms.TypedChoiceField(choices=METODO_PAGO)
    tienda = forms.TypedChoiceField(choices=TIENDAS)
   # inventory = forms.IntegerField(default=0)

    class Meta:
        model = Address
        fields = ('nombre_completo','direccion','municipio','departamento','phone_number','metodo_pago','tienda',)

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ('productos','cantidad','total',)