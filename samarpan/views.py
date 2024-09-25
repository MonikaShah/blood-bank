from django.shortcuts import render

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