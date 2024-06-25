from django.db import models

# Create your models here.
class todo(models.Model):
    todo = models.CharField(max_length =100)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)