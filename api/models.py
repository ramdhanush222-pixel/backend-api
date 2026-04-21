from django.db import models

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('canceled', 'Canceled'),
    ]
    
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    doctor = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.name
    


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
class Payment(models.Model):
    appointment = models.ForeignKey(
    "Appointment",
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.FloatField()
    method = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    