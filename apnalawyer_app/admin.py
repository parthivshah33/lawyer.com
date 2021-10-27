from django.contrib import admin
from .models import Lawyer , Contact , Appointments

# Register your models here.

admin.site.register(Lawyer)
admin.site.register(Contact)
admin.site.register(Appointments)
