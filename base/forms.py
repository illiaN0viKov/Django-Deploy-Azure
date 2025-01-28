from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Item


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'text-gray-800 bg-white border border-gray-300 w-full text-sm px-4 py-3 rounded-md outline-blue-500',
                'placeholder': 'Enter Username'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'text-gray-800 bg-white border border-gray-300 w-full text-sm px-4 py-3 rounded-md outline-blue-500',
            'placeholder': 'Enter Password'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'text-gray-800 bg-white border border-gray-300 w-full text-sm px-4 py-3 rounded-md outline-blue-500',
            'placeholder': 'Confirm Password'
        })


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'text-gray-800 bg-white border border-gray-300 w-full text-sm px-4 py-3 rounded-md outline-blue-500',
            'placeholder': 'Enter Password'
        })
        
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'text-gray-800 bg-white border border-gray-300 w-full text-sm px-4 py-3 rounded-md outline-blue-500',
            'placeholder': 'Enter Username'
        })


from .models import Item

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price',  'condition']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'text-gray-800 bg-white border border-gray-300 w-full text-sm px-4 py-3 rounded-md outline-blue-500',
                'placeholder': 'Name'
            }),

            'price': forms.NumberInput(attrs={ 
                'class': 'text-gray-800 bg-white border border-gray-300 w-full text-sm px-4 py-3 rounded-md outline-blue-500',
                'placeholder': 'Price'
            }),

            'picture': forms.FileInput(attrs={
                'class': '',
            }),

            'condition': forms.Select(  
                attrs={
                    'class': 'h-12 border border-gray-300 text-gray-600 text-base rounded-lg block w-full py-2.5 px-4 focus:outline-none',
                }
            ),
        }

