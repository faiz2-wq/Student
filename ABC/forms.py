from ABC.models import *
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder']='Enter' + field.label + '*'
            field.widget.attrs['class']='forms-control'    
        
class PaymentDetailsForm(forms.ModelForm):
    class Meta:
        model=PaymentDetails
        fields='__all__'

