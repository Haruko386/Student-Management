from django.db import models


# Create your models here.

class Grade(models.Model):
    grade_name = models.CharField(max_length=50, unique=True, verbose_name="Class Name")
    grade_number = models.CharField(max_length=50, unique=True, verbose_name="Class Number")

    def __str__(self):
        return self.grade_name

    class Meta:
        db_table = 'grades'
        verbose_name = "Grade"
        verbose_name_plural = "Grade"
        ordering = ['grade_number']
