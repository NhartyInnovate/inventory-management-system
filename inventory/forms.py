from django import forms
from .models import InventoryItem
from .models import StockTransaction
from .models import AssetAssignment


class InventoryItemForm(forms.ModelForm):

    class Meta:
        model = InventoryItem

        fields = [
            'category',
            'asset_code',
            'name',
            'description',
            'serial_number',
            'quantity',
            'unit_cost',
            'status',
            'purchase_date',
            'supplier'
        ]



class StockInForm(forms.Form):

    quantity = forms.IntegerField(
        min_value=1,
        label="Quantity to Add"
    )


class AssetAssignmentForm(forms.ModelForm):

    class Meta:
        model = AssetAssignment

        fields = [
            'assigned_to',
            'return_date',
            'condition',
            'department',
            'purpose'
        ]

