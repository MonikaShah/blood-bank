from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .forms import InstitutionForm,StudentForm
from .models import Institutions

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
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or back to the form
    else:
        form = StudentForm()

    return render(request, 'samarpan/add_student.html', {'form': form})

    # if request.method == 'POST':
    #     form = StudentForm(request.POST)
    #     if form.is_valid():
    #         form.save()  # Process your form data
    #         return redirect('student_success')  # Redirect after successful submission
    # else:
    #     form = StudentForm()
    
    # # Populate the institution field with all institutions
    # form.fields['institution'].queryset = Institutions.objects.all()

    # return render(request, 'samarpan/add_student.html', {'form': form})

def student_success(request):
    return render(request, 'samarpan/student_success.html')  # Create this template

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