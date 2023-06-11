from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            "message": forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Message"}),
        }
