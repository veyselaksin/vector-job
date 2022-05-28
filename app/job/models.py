from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):

    JOB_TAG = (
        ('Django', 'Django'),
        ('Nodejs', 'Nodejs'),
        ('Python', 'Python'),
        ('C#', 'C#'),
        ('Java', 'Java'),
        ('C++', 'C++')
    )

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="jobs", on_delete=models.CASCADE)
    job_tag = models.CharField(max_length=100, choices=JOB_TAG, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    
    

    def __str__(self) -> str:
        return self.title