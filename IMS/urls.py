from django.urls import path
from . views import *

urlpatterns = [
    # 1. String: Browser url :path, 2. String: Views.py def name, 3: String: Html template link name using dynamic url

    path('', home, name='home'),
    path('inventory', inventory, name='inventory'),
    path('additem', additem, name='additem'),
    path('sellitem/<int:Id>/', sellitem, name='sellitem'),
    path('edititem/<int:Id>/', edititem, name='edititem'),
    path('viewitem/<int:Id>/', viewitem, name='viewitem'),
    path('orderlist', orderlist,  name='orderlist'),
    path('orderitem/<int:Id>/', orderitem, name='orderitem'),
    path('order_placed', order_placed, name='order_placed'),
    path('orderstatus', orderstatus, name='orderstatus'),
    path('order_received', order_received, name='order_received'),
    path('order_canceled', order_canceled, name='order_canceled'),
    path('transactionlist', transactionlist, name='transactionlist'),
    path('itemsold', itemsold, name='itemsold'),
    path('management', management, name='management'),
]

app_name = 'IMS'