from django.db import models


# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=64)
    student_sex = models.CharField(max_length=3)
    create_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.Student_name
        return self.id
