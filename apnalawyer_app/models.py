from django.db import models
import datetime

class Lawyer(models.Model):
    id = models.AutoField(primary_key=True) #aa pachhi thi add karel chhe-->primary_key
    image = models.ImageField(upload_to='lawyer_images', default="")
    name = models.CharField(max_length=40, null=False)
    address = models.CharField(max_length=150 , null=False)
    city = models.CharField(max_length=10 , null=False , default="")
    # dlocation : may be later
    degree = models.CharField(max_length=40 , null=False)
    fees = models.CharField(max_length=8, null=False)
    office_address = models.CharField(max_length=150 , null=True)
    specializatioin = models.CharField(max_length=40 , null=True)
    average_time_per_client_minute = models.CharField(max_length=4 , null=False , default="30")
    mobile_number = models.CharField(max_length=15 ,  null=False)
    telephone_number = models.CharField( max_length=15 , null=False)
    email_id = models.EmailField(max_length=30 , null=False , unique=False)
    payment_number = models.CharField(max_length=15 ,null=False)
    emergency_charge = models.CharField( max_length=15 ,null=False)
    achievements = models.CharField(max_length=300, null=True)
    username = models.CharField(max_length=18 , null=False , unique=True)
    password = models.CharField(max_length=14 , null=False , unique=False)

    def __str__(self):
        return self.name

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=40 , null=False)
    user_phone_number = models.CharField(max_length=15 , null=False)
    user_email_id = models.CharField(max_length=25 , null=False)
    user_suggestion = models.CharField(max_length=3000 , null=True)
    user_query = models.CharField(max_length=3000 , null=True)
    user_complaint =models.CharField(max_length=3000 ,null=True)

    def __str__(self):
        return self.user_name

class Appointments(models.Model):
    id = models.AutoField(primary_key=True)  # aa pachhi thi add karel chhe-->primary_key
    username = models.CharField(max_length=40 , null=False)
    name = models.CharField(max_length=40, null=False)
    age = models.PositiveIntegerField(null=False , default="18")
    gender = models.CharField(max_length=10 , null=False , unique=False)
    email_id = models.EmailField(max_length=30 , null=False , unique=False)
    phone_number = models.CharField(max_length=15 , null=False)
    emergency = models.CharField(max_length=10 , null=True)
    confirmation_code = models.CharField(max_length=10 , null=False , default="0000")
    l_id = models.CharField(max_length=10 , null=False , default="1")
    dateTime = models.CharField(max_length=40 , null=False , default=" ")
    confirm = models.BooleanField(null=False , default=False , editable=True )

    def __str__(self):
        return self.name


