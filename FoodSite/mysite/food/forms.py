from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
        widgets = {
            'item_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter item name'
            }),
            'item_desc': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 4,
                'placeholder': 'Enter item description'
            }),
            'item_price': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter price'
            }),
            'item_image': forms.URLInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'https://example.com/image.jpg'
            }),
        }
    def clean_item_price(self):
        price= self.cleaned_data['item_price']
        if price<0:
            raise forms.ValidationError("Price cant be negative")
        return price    
    

    def clean(self):
        cleaned = super().clean()
        item_name = cleaned.get('item_name')
        item_desc = cleaned.get('item_desc')

        if item_name and item_desc and item_name.lower() == item_desc.lower():
            self.add_error('item_desc','Item description must not be same as item name')
            
        return cleaned
    
        
