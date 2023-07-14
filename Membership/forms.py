from django import forms
from .models import Application


# class from django import forms

# class BankForm(forms.ModelForm):
#     class Meta:
#         model =Bank
#         fields =[
#             "bank_name",
#             "image",
#             "interest_rate", 
#         ]


class ApplicationForm(forms.ModelForm):
    
    
    class Meta:
        model = Application
        fields = "__all__" 