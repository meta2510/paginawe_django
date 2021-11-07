from django.shortcuts import redirect, render, get_object_or_404
from onlineshop.models import Product
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .cart import Cart
from .forms import CartAddProductForm, CheckOutForm, PaymentForm
from django.contrib import messages
from django.views.generic import FormView
# Create your views here.

@require_POST
@login_required(login_url='/register/login/')
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],overrride_quantity=cd['override'])
    return redirect('cart:cart_detail')

@login_required(login_url='/register/login/')
def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

@login_required(login_url='/register/login/')
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial=
        {'quantity':item['quantity'],
        'override':True })
    return render(request,'cart/detail.html',{'cart':cart})

""" def cart_checkout(request):
    #cart = Cart(request)

    if request.method == 'POST':
        #user_form = UpdateUserForm(request.POST, instance=request.user)
        checkout = CheckOutForm(request.POST,instance=request.user)
        #payment = PaymentForm(request.POST)

        if checkout.is_valid():
           # payment.save()
           # checkout.save(commit=False)
            checkout.save()
            messages.success(request, 'La orden fue ingresada correctamente')
            return redirect('/checkout/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        checkout = CheckOutForm(instance=request.user)
        #payment = PaymentForm(request.POST)
    return render(request, 'cart/checkout.html', {'checkout': checkout})
    #return render(request, 'cart/checkout.html', {'checkout': checkout,'payment': payment,'cart':cart}) """


class cart_checkout(FormView):
    template_name = 'cart/checkout.html'
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        form = CheckOutForm()
        context = {"form":form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CheckOutForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            messages.success(request, 'La orden fue ingresada correctamente')
            form.save()

        context = {"form":form}
        return render(request, self.template_name, context)

    



    