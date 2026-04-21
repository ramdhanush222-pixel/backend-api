from django.contrib import admin
from .models import User, Appointment
from .models import Payment

admin.site.register(User)
admin.site.register(Appointment)
admin.site.register(Payment)