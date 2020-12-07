from django.db import models

# Create your models here.
class employees(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=10)
    user_email  = models.EmailField(max_length=70,blank=True,unique=True)
    postal_address = models.TextField()
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname