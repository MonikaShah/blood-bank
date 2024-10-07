from django import forms
from .models import Students,Institutions

from django import forms
from .models import Students  # Make sure to import your Students model

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = [
            'first_name', 'middle_name', 'surname', 'mobile', 'email', 
            'institution_type', 'institution', 'pincode', 'dob', 
            'blood_group', 'gender', 'year', 'stream', 'grade'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Middle Name', 'required': False}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Surname'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'institution_type': forms.Select(attrs={'class': 'form-control', 'id': 'institution-type'}),
            'institution': forms.Select(attrs={'class': 'form-control', 'id': 'institution-select'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pincode'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'blood_group': forms.Select(choices=Students.BLOOD_GROUP_CHOICES, attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=Students.GENDER_CHOICES, attrs={'class': 'form-control'}),
            'year': forms.Select(choices=Students.YEAR_CHOICES, attrs={'class': 'form-control', 'id': 'year-field', 'style': 'display:none;'}),
            'stream': forms.Select(choices=Students.STREAM_CHOICES, attrs={'class': 'form-control', 'id': 'stream-field', 'style': 'display:none;'}),
            'grade': forms.Select(choices=Students.GRADE_CHOICES, attrs={'class': 'form-control', 'id': 'grade-field', 'style': 'display:none;'}),
        }
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['institution'].queryset = Institutions.objects.none()

        if 'institution_type' in self.data:
            institution_type = self.data.get('institution_type')
            self.fields['institution'].queryset = Institutions.objects.filter(type=institution_type)
        elif self.instance.pk:
            self.fields['institution'].queryset = Institutions.objects.filter(type=self.instance.institution_type)



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
