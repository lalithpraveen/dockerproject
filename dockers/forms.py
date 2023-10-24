from django import forms
from .models import DocketEntry

class UploadFileForm(forms.Form):
    file = forms.FileField()

class DocketEntryForm(forms.ModelForm):
    class Meta:
        model = DocketEntry
        fields = ['name', 'start_time', 'end_time', 'hours_worked', 'rate_per_hour', 'supplier', 'purchase_order']
        widgets = {
            'start_time': forms.TextInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.TextInput(attrs={'type': 'datetime-local'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields[
                'purchase_order'].queryset = PurchaseOrder.objects.none()  # Initially, no options in the purchase order dropdown
            if 'supplier' in self.data:
                try:
                    supplier_id = int(self.data.get('supplier'))
                    self.fields['purchase_order'].queryset = PurchaseOrder.objects.filter(supplier_id=supplier_id)
                except (ValueError, TypeError):
                    pass  # Handle the case when supplier ID is not valid or not provided
            elif self.instance.pk:
                self.fields['purchase_order'].queryset = self.instance.supplier.purchaseorder_set.all()

