from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length= 20)
    roll = models.IntegerField(primary_key= True)
    address = models.TextField(blank=True, null=True)
    # date_time_field = models.DateTimeField(auto_now_add=True)
    # email_field = models.EmailField(default='email please')
    # text_field = models.TextField(default="type please")
    # time_field = models.TimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name