from django import forms

from .models import Contact as ContactModel


class Contact(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                }),
            "phone": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "type": "tel",
                }),
            "birthday": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }),
            "gender": forms.Select(
                attrs={
                    "class": "form-control",
                }),
            "picture": forms.FileInput(
                attrs={
                    "class": "form-control",
                }),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                }),
        }
