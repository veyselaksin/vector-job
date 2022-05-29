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

job_tags= [c[0] for c in Job.job_tag.field.choices]

class ApplyJob(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    content = models.TextField(null=True)
    experience = models.TextField(null=True)
    created_by = models.ForeignKey(User, related_name='apply_job', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)