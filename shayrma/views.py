from itertools import product
from django.http import JsonResponse
import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Types, Kebab, Saved, Drink, Orders, Card, Saved_invite
from django.db.models import Sum, IntegerField
from django.db.models.functions import Cast
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    kebab_type = Types.objects.get(Name = "Кебаб")
    kebab = Kebab.objects.filter(types = kebab_type)
    kebab_type_one = Types.objects.get(Name = "Мини_кебаб")
    kebabi = Kebab.objects.filter(types = kebab_type_one)
    kebab_type_two = Types.objects.get(Name="Кебаб_сосиской")
    kebabik = Kebab.objects.filter(types= kebab_type_two)
    kebab_type_three = Types.objects.get(Name="Картошка")
    potatos = Drink.objects.filter(types=kebab_type_three)
    kebab_type_four = Types.objects.get(Name="Напитки")
    drink = Drink.objects.filter(types=kebab_type_four)
    if request.method == "POST":
        drinksss = request.POST.get('drink')
        if drinksss:
            dri = Drink.objects.get(id=drinksss)
            Saved.objects.create(
                Name=dri.Name,
                types=dri.types,
                Price=dri.price,
                mas=dri.mass,
                col =dri.col,
                kebab_url=dri.drink_url,
            )
            Saved_invite.objects.create(
                Name=dri.Name,
                types=dri.types,
                Price=dri.price,
                mas=dri.mass,
                col=dri.col,
                kebab_url=dri.drink_url,
            )
            return redirect('card')
        else:
            data = json.loads(request.body)
            mass= data.get('mass')
            product_id = data.get('product_id')
            product = Kebab.objects.get(id=product_id)
            product_price = {300: 8, 400: 12.5, 500: 14, 650: 16.5}
            product.Price = product_price[mass]
            product.mas = mass
            product.save()
    return render(request, 'index.html', {'kebab':kebab, 'kebabi':kebabi, 'kebabik':kebabik, 'potatos':potatos, 'drink':drink})

def pred_card (request, kebab_url):
    product = Kebab.objects.get(id = kebab_url)
    if request.method == "POST":
        products_add = request.POST.getlist('produts_add')
        w = len(products_add)
        options_string = ', '.join(products_add)
        ids = request.POST.get('com_id')
        product.dop_text = options_string
        product.price = product.Price + (1.20 * w)
        Saved.objects.create(
            Name = product.Name,
            types = product.types,
            Price = product.price,
            text = product.text,
            dop_text = options_string,
            mas = product.mas,
            kebab_url = product.kebab_url,
            col = product.col
        )
        Saved_invite.objects.create(
            Name=product.Name,
            types=product.types,
            Price=product.price,
            text=product.text,
            dop_text=options_string,
            mas=product.mas,
            kebab_url=product.kebab_url,
            col=product.col
        )
        return redirect('card')
    return render(request, 'pred_card.html', {'product':product})


def kebab (request):
    kebab_type = Types.objects.get(Name="Кебаб")
    kebab = Kebab.objects.filter(types=kebab_type)
    if request.method == "POST":
        data = json.loads(request.body)
        mass = data.get('mass')
        product_id = data.get('product_id')
        product = Kebab.objects.get(id=product_id)
        product_price = {300: 8, 400: 12.5, 500: 14, 650: 16.5}
        product.Price = product_price[mass]
        product.mas = mass
        product.save()
    return render(request, 'kebab.html', {'kebab':kebab})

def Mini_kebab (request):
    kebab_type_one = Types.objects.get(Name="Мини_кебаб")
    kebabi = Kebab.objects.filter(types=kebab_type_one)
    return render(request, 'Mini_kebab.html', {'kebabi':kebabi})

def kebab_sos (request):
    kebab_type_two = Types.objects.get(Name="Кебаб_сосиской")
    kebabik = Kebab.objects.filter(types=kebab_type_two)
    return render(request, 'kebab_sos.html', {'kebabik':kebabik})

def potatos (request):
    kebab_type_three = Types.objects.get(Name="Картошка")
    potatos = Drink.objects.filter(types=kebab_type_three)
    return render(request, 'potatos.html', {'potatos':potatos})

def drink (request):
    kebab_type_four = Types.objects.get(Name="Напитки")
    drink = Drink.objects.filter(types=kebab_type_four)
    return render(request, 'drink.html', {'drink':drink})


def card(request):
    products = Saved.objects.all()
    if request.method ==  'POST':
        data = json.loads(request.body)
        if 'quantity' in data:
            col = data.get('quantity')
            product_id = data.get('products_id')
            kebab_saved = Saved.objects.get(id = product_id)
            kebab_saved.col = col
            kebab_saved.save()
            kebab_saved_invite = Saved_invite.objects.get(id=product_id)
            kebab_saved_invite.col = col
            kebab_saved_invite.save()
        else:
            kebab_delete = data.get('delete_id')
            card_delete = Saved.objects.get(id = kebab_delete)
            card_delete.delete()
            card_delete_invite = Saved_invite.objects.get(id=kebab_delete)
            card_delete_invite.delete()
    return render(request, 'card.html', {'products':products})

def order(request):
    products = Saved_invite.objects.all()
    Save = Saved.objects.all()
    orders = Orders.objects.all()
    total_price = 0
    name = ''
    phone = ''
    email = ''
    text = ''
    if request.method ==  'POST':
        name = request.POST.get('Name')
        phone = request.POST.get('telephone')
        email = request.POST.get('email')
        text = request.POST.get('dop_text')
        order = Orders.objects.create(
            Name=name,
            Phone=phone,
            email=email
        )
        total_price = sum((product.Price * (product.col if product.col else 1))for product in products)
        for product in products:
            quantity = product.col if product.col else 1
            item_total = product.Price * quantity
            Card.objects.create(
                Order = order,
                Kebab = product,
                TotalPrice = total_price,
                dop_text = text,
            )
        Save.delete()
        return redirect('end')

    return render(request, 'order.html')


def end(request):
    products_card = Card.objects.last()
    if not products_card:
        return redirect('home')
    return render(request, 'end.html', {'products_card':products_card})

def config(request):
    return render(request, 'config.html')




































































































































