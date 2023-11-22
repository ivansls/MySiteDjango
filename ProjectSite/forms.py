from django import forms

from .models import *


class CardForm(forms.ModelForm):
    class Meta:
        model = Product
        #fields = ['name', 'price']
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(
                attrs={
                    "style":"background-color: #FFFFFF; margin:10px"
                }
            ),
            'description': forms.Textarea(
                attrs={
                    "style":"background-color: #FFFFFF; margin:10px"
                }
            )
        }


class BasketForm(forms.ModelForm):
    class Meta:
        model = Order_item
        #fields = ['name', 'price']
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(
                attrs={
                    "style":"background-color: #FFFFFF; margin:10px"
                }
            ),
            'description': forms.Textarea(
                attrs={
                    "style":"background-color: #FFFFFF; margin:10px"
                }
            )
        }


class CardFormTag(forms.ModelForm):
    class Meta:
        model = Tag
        #fields = ['name', 'price']
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(
                attrs={
                    "style":"background-color: #FFFFFF; margin:10px"
                }
            ),
            'description': forms.Textarea(
                attrs={
                    "style":"background-color: #FFFFFF; margin:10px"
                }
            )
        }
class ApiAddCardForm(forms.ModelForm):
    class Meta:
        model = Category
        #fields = ['name', 'price']
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(
                attrs={
                    "style":"background-color: #FFFFFF; margin:10px"
                }
            ),
            'description': forms.Textarea(
                attrs={
                    "style":"background-color: #FFFFFF; margin:10px"
                }
            )
        }
