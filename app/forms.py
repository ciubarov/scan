from django import forms

class SaveUserData(forms.Form):
    phone = forms.CharField(label='Номер телефона', max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}))
    email = forms.CharField(label='Email адрес', max_length=30, required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email адрес'}))