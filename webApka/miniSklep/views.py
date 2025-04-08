from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
        labels = {
            'name': 'Nazwa produktu',
            'price': 'Cena (PLN)'
        }

def user_login(request):
    if request.user.is_authenticated:
        return redirect('list')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                login(request, user)
                return redirect('list')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def product_list(request):
    products = Product.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    return render(request, 'products/list.html', {'products': products, 'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')