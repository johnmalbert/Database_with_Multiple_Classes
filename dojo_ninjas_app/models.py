from django.db import models

# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255, default="Old Dojo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #ninjas- a list of ninjas associated with given Dojo

class Ninjas(models.Model):
    dojo_id = models.ForeignKey(Dojos, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)