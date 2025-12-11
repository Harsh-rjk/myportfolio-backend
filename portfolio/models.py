from django.db import models

class entry (models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()


    class Meta:
        db_table = 'entry'

     

