from django.db import models
import uuid

# Create your models here.
# models.py
class Elder(models.Model):
    first_name = models.CharField(max_length=60)
    second_name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=12)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.first_name + '' + self.second_name

class Son(models.Model):
    first_name = models.CharField(max_length=60)
    second_name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=12)
    age = models.IntegerField()
    elder = models.ManyToManyField('Elder')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.first_name + '' + self.second_name

class Proffesion(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return title

class Pro(models.Model):
    first_name = models.CharField(max_length=60)
    second_name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=12)
    profession = models.ManyToManyField('Proffesion')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.first_name + '' + self.second_name

class Call(models.Model):
    elder = models.ForeignKey('Elder', on_delete=models.CASCADE)
    son = models.ForeignKey('Son', on_delete=models.CASCADE)
    pro = models.ForeignKey('Pro', on_delete=models.CASCADE)
    is_open = models.BooleanField(False)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return 'Call for: ' + self.elder.first_name + ' in ' + self.elder.city