from django import forms
from django.core.exceptions import ValidationError
from .models import Students,Institutions
from django.http import JsonResponse
from django import forms
from .models import Students  # Make sure to import your Students model

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = [
            'first_name', 'middle_name', 'surname', 'mobile', 'email',
            'institution_type','institution', 'pincode', 'dob', 'blood_group', 'gender',
            'year', 'stream', 'grade'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
        error_messages = {
            'first_name': {
                'required': 'First name is required.',
            },
            'mobile': {
                'required': 'Mobile number is required.',
            },
            'dob': {
                'required': 'Date of birth is required.',
            },
            'surname':{
                'required': 'Surname is required.',
            },
            'institution_type':{
                'required': 'Please Choose institution type.',
            },
            'institution':{
                'required': 'Please Choose institution name.',
            }
            # You can add similar custom messages for other fields as needed
        }

    def clean(self):
        cleaned_data = super().clean()
        print(f"Cleaned data: {cleaned_data}")  # Add this to inspect cleaned data
        mobile = cleaned_data.get("mobile")
        dob = cleaned_data.get("dob")

        print(f"Mobile: {mobile}, DOB: {dob}")
        # Check if a student with the same mobile and dob already exists
        if mobile and dob:
            if Students.objects.filter(mobile=mobile, dob=dob).exists():
                # self.add_error(None, "A student with this mobile number and date of birth already exists.")
                raise ValidationError("A student with this mobile number and date of birth already exists.")  # Raise validation error
                # return JsonResponse({'exists': True})  # AJAX response for duplicates
            
    
        return cleaned_data
    
class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institutions  # The model to be used for this form
        fields = ['institution_name', 'institution_type', 'address', 'city', 'email', 'phone_number', 'contact_person_name']  # List of fields to be included in the form

        # You can also add custom widgets or labels if needed
        widgets = {
            'institution_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Institution Name'}),
            'institution_type': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Full Address', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'contact_person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Person Name'}),
        }
        
        labels = {
            'institution_name': 'Institution Name',
            'institution_type': 'Type of Institution',
            'address': 'Address',
            'city': 'City',
            'email': 'Email Address',
            'phone_number': 'Phone Number (optional)',
            'contact_person_name': 'Contact Person Name (optional)',
        }
