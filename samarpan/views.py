from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from .forms import InstitutionForm,StudentForm
from .models import Institutions
import json

# Create your views here.
def home(request):
    return render(request, 'samarpan/index.html')

def about(request):
    return render(request, 'samarpan/about_us.html')

def product(request):
    return render(request, 'samarpan/Product.html')

def organizer(request):
    return render(request, 'samarpan/organizer.html')

def services(request):
    return render(request, 'samarpan/services.html')

def donor(request):
    return render(request, 'samarpan/donor.html')

def other_activities(request):
    return render(request, 'samarpan/other_activities.html')

def gallery(request):
    return render(request, 'samarpan/gallery.html')

def thalassemia(request):
    return render(request, 'samarpan/thalassemia.html')

def contact(request):
    return render(request, 'samarpan/contact.html')

def donation(request):
    return render(request, 'samarpan/donation.html')

def add_institution(request):
    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the form data into the Institution model
            return redirect('institution_success')  # Redirect after successful form submission
    else:
        form = InstitutionForm()  # Render an empty form for GET request
    
    return render(request, 'samarpan/add_institution.html', {'form': form})

def institution_success(request):
    return render(request, 'samarpan/institution_success.html')  # Create this template

def add_student(request):
    # print("Form submitted")
    if request.method == 'POST':
        form = StudentForm(request.POST)
        print(request.POST)
        institution_type = request.POST.get('institution_type')  # Get institution type from POST
        institution_name = request.POST.get('institution')  # Get institution from POST
        
        if form.is_valid():
            
            # Save the form data
            form.save()
            messages.success(request, 'Student details added successfully.')
            return redirect('student_success')  # Redirect to prevent resubmission
        # print(form.errors)
        else:
            # Check for specific error messages
            print(form.errors)
            for error in form.non_field_errors():
                messages.error(request, error)

            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            
    else:
        form = StudentForm()
        
    institutions = Institutions.objects.all()
    print("Institutions:", institutions)  # Debug print
    return render(request, 'samarpan/add_student.html', {
        'form': form, 
        'institutions': institutions,
        # 'institution_type': institution_type,  # Pass selected institution type
        # 'institution_name': institution_name,
          })
    
def student_success(request):
    return render(request, 'samarpan/student_success.html')  # Create this template

# def check_student_uniqueness(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         mobile = data.get("mobile")
#         dob = data.get("dob")

#         # Check if student with same mobile and DOB exists
#         exists = Students.objects.filter(mobile=mobile, dob=dob).exists()
        
#         return JsonResponse({"exists": exists})
#     return JsonResponse({"error": "Invalid request"}, status=400)

def load_institutions(request):
    # Get the institution_type from the request
    institution_type = request.GET.get('institution_type')
    

    if not institution_type:
        return JsonResponse({'error': 'institution_type not provided'}, status=400)

    try:
        # Fetch institutions matching the given institution_type
        institutions = Institutions.objects.filter(institution_type=institution_type)

        # Convert the queryset to a list of dictionaries
        institution_list = [{'id': inst.id, 'name': inst.institution_name} for inst in institutions]

        return JsonResponse(institution_list, safe=False)

    except Exception as e:
        # Log the error and return a server error response
        print(f"Error: {e}")
        return JsonResponse({'error': 'An error occurred while fetching institutions'}, status=500)