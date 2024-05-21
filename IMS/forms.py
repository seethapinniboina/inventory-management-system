from typing import Any
from django import forms
from .models import Inventory, Order, Transaction

class AddItemForm(forms.ModelForm):
    Name = forms.CharField(required=True)
    Cost = forms.DecimalField(required=True)
    Selling_price = forms.DecimalField(required=True)
    class Meta:
        model = Inventory
        fields = [
            "Name",
            "Cost",
            "Selling_price",
        ]

class EditItemForm(forms.ModelForm):
    Name = forms.CharField(required=True)
    Cost = forms.DecimalField(required=True)
    Selling_price = forms.DecimalField(required=True)
    class Meta:
        model = Inventory
        fields = [
            "Name",
            "Cost",
            "Selling_price",
        ]


class OrderItemForm(forms.ModelForm):
    Name = forms.CharField(required=True, widget=forms.TextInput(attrs={'readonly':'readonly'}))
    Quantity = forms.DecimalField(required=True, min_value=1)
    Cost = forms.DecimalField(required=True)
    class Meta:
        model = Order
        fields = [
            "Name",
            "Quantity",
            "Cost",
            "Item",
        ]

class SellItemForm(forms.ModelForm):
    Name = forms.CharField(required=True)
    Stock = forms.DecimalField(required=True, widget=forms.TextInput(attrs={'readonly':'readonly'}))
    Quantity = forms.DecimalField(required=True, min_value=1)
    Selling_price = forms.DecimalField(required=True)
    class Meta:
        model = Transaction
        fields = [
            "Name",
            "Quantity",
            "Selling_price",
            "Item",
        ]


