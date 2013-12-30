#coding:utf-8
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label="E-mail")
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())#针对中文 len(message)
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
