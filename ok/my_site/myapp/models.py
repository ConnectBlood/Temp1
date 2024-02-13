from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.
class Organization(models.Model):
     SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]
     

     name = models.CharField(max_length=100)
     email = models.EmailField()
     state = models.CharField(max_length=100)
     district = models.CharField(max_length=100)
     city = models.CharField(max_length=100)
     landmark = models.CharField(max_length=100)
     zipcode = models.CharField(max_length=10)
     size = models.CharField(max_length=10, choices=SIZE_CHOICES)

     def __str__(self):
        return self.name
     
class BloodDetail(models.Model):
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    amount_available = models.IntegerField()
    donation_date = models.DateField()

    def __str__(self):
        return f"{self.blood_type} - {self.amount_available} units"
    

class Transaction(models.Model):
    sender_hospital_id = models.CharField(max_length=100)
    units_of_blood = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Transaction #{self.id} - Sender: {self.sender_hospital_id}, Units: {self.units_of_blood}, Date: {self.date_time}"
    





class Location(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Distance(models.Model):
    hospital_location = models.ForeignKey(Location, related_name='hospital_location', on_delete=models.CASCADE)
    sender_location = models.ForeignKey(Location, related_name='sender_location', on_delete=models.CASCADE)
    distance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Distance between {self.hospital_location.name} and {self.sender_location.name}: {self.distance} km"
