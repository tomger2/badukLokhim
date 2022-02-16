from django.db import models
import uuid

# Create your models here.
# models.py
class Elder(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=120)
    floor = models.IntegerField(null=True, blank=True)
    apartment_num = models.IntegerField(null=True, blank=True)
    private_home = models.BooleanField()
    phone = models.CharField(max_length=12)
    long = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

class Son(models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)
    elder = models.ManyToManyField('Elder')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

class Profession(models.Model):
    title = models.CharField(max_length=60)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

class Pro(models.Model):
    name = models.CharField(max_length=60)
    active_cities = models.JSONField()
    phone = models.CharField(max_length=12)
    rank = models.IntegerField(null=True, blank=True)
    num_of_calls = models.IntegerField(null=True, blank=True)
    profession = models.ManyToManyField('Profession')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reviews = models.JSONField(default="[]")

    def __str__(self):
        return self.name 

class Call(models.Model):
    elder = models.ForeignKey('Elder', on_delete=models.CASCADE)
    grandson = models.ForeignKey('Son', on_delete=models.CASCADE)
    profession = models.ManyToManyField('Profession')
    is_open = models.BooleanField(False)
    is_occupied = models.BooleanField(False)
    description = models.CharField(max_length=1024)
    handy_man_pool = models.ManyToManyField('Pro')
    handy_man = models.ForeignKey('Pro', related_name='chosen', on_delete=models.CASCADE, null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    start_date = models.DateField()
    closed_date = models.DateField(null=True, blank=True)
    destination = models.JSONField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return 'Call for: ' + self.elder.name + ' in ' + self.elder.city