from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserType(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)

User.usertype = property(lambda u:UserType.objects.get_or_create(user=u)[0])
