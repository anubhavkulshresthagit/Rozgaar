from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


CATEGORIES = [
    ('Business_type','Business_type'),
    ('Normal','Normal'),

]

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=25,validators=[RegexValidator(regex='^[a-zA-Z]{3,}$',
                                     message='Please enter a valid First name',code='Invalid')])
    last_name = forms.CharField(max_length=25,validators=[RegexValidator(regex='^[a-zA-Z]{3,}$',
                                     message='Please enter a valid Last name',code='Invalid')])
    email = forms.EmailField()
    mobile_number = forms.CharField(max_length=10,validators=[RegexValidator(regex='^[6789][0-9]{9}$',
                                     message ='Invalid mobile number entered', code='Invalid')])
    adhaar_number = forms.CharField(max_length=10, validators=[RegexValidator(regex='^[123456789][0-9]{9}$',
                                                                               message='Invalid Adhaar number entered',
                                                                               code='Invalid')])
    account_type = forms.ChoiceField(choices=CATEGORIES)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile_number', 'password1', 'password2', 'adhaar_number']