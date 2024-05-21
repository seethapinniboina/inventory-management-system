from django.shortcuts import render
from django.shortcuts import redirect
#from django.http import HttpResponse
from .models import Inventory, Order, Transaction
from .forms import AddItemForm , SellItemForm , EditItemForm, OrderItemForm
from django.conf import settings
import json

managementjson = settings.MEDIA_ROOT / 'management.json'

# Create your views here.

def management(request):
    try:
        with open(managementjson) as f:
            data = json.load(f)
    except: data = {}

    jsonData = json.dumps(data)
    context = {'jsonData' : jsonData, 'data' : data}
    context.update(data)
    return render(request, 'IMS/management.html', context)


def home(request):
    list1 = sum(Inventory.objects.values_list('Profit_earned', flat=True))
    list2 = sum(Inventory.objects.values_list('Quantity', flat=True))
    list3 = Inventory.objects.order_by('-Selling_price').first()
    list4 = Inventory.objects.order_by('-Quantity_sold').first()
    list5 = Inventory.objects.order_by('-Profit_earned').first()
    list6 = Inventory.objects.filter(Quantity=0).values()
    list7 = Inventory.objects.order_by('-Item_profit').first()
    context = {'list1' : list1, 'list2' : list2, 'list3' : list3, 'list4' : list4, 'list6' : list6, 'list5' : list5, 'list7' : list7}
    return render(request, 'IMS/home.html', context)

def inventory(request):
    list = Inventory.objects.all()
    list = list.values()
    context = {'list' : list, 'title' : "Inventory Management System"}
    return render(request, 'IMS/inventory.html', context=context)
    

def additem(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventory')
    form = AddItemForm()
    context = {'form':form,'form_title':"Add Item", 'form_action':"Add Item to Inventory"}
    return render(request, 'IMS/additem.html', context=context)


def edititem(request, Id):
    list_item = Inventory.objects.get(Id=Id)
    if request.method == 'POST':
        form = EditItemForm(request.POST, instance=list_item)
        if form.is_valid():
            form.save()
            return redirect('/inventory')
    else:
        form = EditItemForm(instance=list_item)
    context = {'form': form, 'form_title':"Edit Item", 'form_action':"Edit"}
    return render(request, 'IMS/additem.html', context)


def viewitem(request,Id):
    list_item = Inventory.objects.filter(Id=Id).values()
    context = {'Id':Id,'list_item':list_item}
    return render(request, 'IMS/viewitem.html', context=context)

def orderitem(request,Id):
    list_item = Inventory.objects.get(Id=Id)
    initial_data = {
        "Name" : list_item.Name,
        "Quantity" : 1,
        "Cost" : list_item.Selling_price,
        "Item" : list_item.Id
    }
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/order_placed?Id='+str(Id))
    else:
        form = OrderItemForm(instance=list_item, initial=initial_data)
    context = {'form': form, 'list_item':list_item}
    return render(request, 'IMS/orderitem.html', context)

def orderlist(request):
    list = Order.objects.all()
    list = list.values()
    context = {'list' : list}
    return render(request, 'IMS/orderlist.html', context)

def order_placed(request):
    Id = request.GET.get('Id', None)
    list = Order.objects.filter(Item_id=Id).values().filter(Is_received = False).filter(Is_cancel = False)
    context = {'list' : list}
    return render(request, 'IMS/order_placed.html', context)

def orderstatus(request):
    status = request.GET.get('status', None)
    orderid = request.GET.get('orderid', None)
    itemid = request.GET.get('itemid', None)
    if status is not None:
        order = Order.objects.get(Id=orderid)
        print(order,"hi")
        if status == "receive":
            order.Is_received = True
            list_item = Inventory.objects.get(Id=itemid)
            quantity = order.Quantity
            list_item.Quantity = quantity + list_item.Quantity
            list_item.save()
        else:
            order.Is_cancel = True
        order.save()
    list = Order.objects.all()
    list = list.values()
    context = {'list' : list}
    return render(request, 'IMS/orderlist.html', context)

def order_received(request):
    Id = request.GET.get('Id', None)
    list = Order.objects.filter(Item_id=Id).values().filter(Is_received = True)
    context = {'list' : list}
    return render(request, 'IMS/order_received.html', context)

def order_canceled(request):
    Id = request.GET.get('Id', None)
    list = Order.objects.filter(Item_id=Id).values().filter(Is_cancel = True)
    context = {'list' : list}
    return render(request, 'IMS/order_canceled.html', context)

def transactionlist(request):
    list = Transaction.objects.all()
    list = list.values()
    context = {'list' : list}
    return render(request, 'IMS/transactionlist.html', context)

def sellitem(request,Id):
    list_item = Inventory.objects.get(Id=Id)
    initial_data = {
        "Name" : list_item.Name,
        "Quantity" : 1,
        "Stock" : list_item.Quantity,
        "Selling_price" : list_item.Selling_price,
        "Item" : list_item.Id
    }
    if request.method == 'POST':
        form = SellItemForm(request.POST)
        if form.is_valid():
            form.save()
            quantity_sold = form.cleaned_data['Quantity']
            list_item.Quantity_sold = list_item.Quantity_sold + quantity_sold
            list_item.Quantity = list_item.Quantity - quantity_sold
            list_item.Item_profit = list_item.Selling_price - list_item.Cost
            list_item.Profit_earned = list_item.Quantity_sold * list_item.Item_profit
            list_item.Revenue = list_item.Quantity_sold * list_item.Cost
            list_item.save()
            return redirect('/transactionlist')
    form = SellItemForm(initial=initial_data)
    context = {'form':form, 'Id':Id, 'list_item' : list_item}
    return render(request, 'IMS/sellitem.html', context=context)

def itemsold(request):
    Id = request.GET.get('Id', None)
    list = Transaction.objects.filter(Item_id=Id).values()
    context = {'list' : list}
    return render(request, 'IMS/itemsold.html', context)










       









