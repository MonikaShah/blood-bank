from django.db import models

# Create your models here.
class Institutions(models.Model):
    # Choices for types of institutions
       
    INSTITUTION_TYPE_CHOICES = [
        ('School', 'School'),
        ('College', 'College'),
    ]
    
    # Fields
    institution_name = models.CharField(max_length=255, verbose_name="Institution Name")
    institution_type = models.CharField(max_length=7, choices=INSTITUTION_TYPE_CHOICES, verbose_name="Institution Type")
    address = models.TextField(verbose_name="Address")
    city = models.CharField(max_length=100, verbose_name="City")
    email = models.EmailField(verbose_name="Email")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number", blank=True, null=True)
    contact_person_name = models.CharField(max_length=100, verbose_name="Contact Person", blank=True, null=True)
    
    # Metadata
    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"
        ordering = ['institution_name']
    
    # String representation of the model
    def __str__(self):
        return f"{self.institution_name} ({self.city})"
    

class Students(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    YEAR_CHOICES = [
        ('1st', '1st Year'),
        ('2nd', '2nd Year'),
        ('3rd', '3rd Year'),
        ('4th', '4th Year'),
    ]

    STREAM_CHOICES = [
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Arts', 'Arts'),
        ('Engineering', 'Engineering'),
        ('Law', 'Law'),
    ]

    GRADE_CHOICES = [
        ('1st', '1st Standard'),
        ('2nd', '2nd Standard'),
        ('3rd', '3rd Standard'),
        ('4th', '4th Standard'),
        ('5th', '5th Standard'),
        ('6th', '6th Standard'),
        ('7th', '7th Standard'),
        ('8th', '8th Standard'),
        ('9th', '9th Standard'),
        ('10th', '10th Standard'),
        ('11th', '11th Standard'),
        ('12th', '12th Standard'),

    ]
    INSTITUTION_CHOICES = (
        ('School', 'School'),
        ('College', 'College'),
    )



    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    institution_type = models.CharField(max_length=10, choices=INSTITUTION_CHOICES)  # Institution type
    institution = models.ForeignKey(Institutions, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=6)
    dob = models.DateField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    
    # These fields will be conditional based on institution type
    year = models.CharField(max_length=10, choices=YEAR_CHOICES, blank=True, null=True)
    stream = models.CharField(max_length=50, choices=STREAM_CHOICES, blank=True, null=True)
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"