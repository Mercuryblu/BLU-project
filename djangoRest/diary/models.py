from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)
    create_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self): 
        return self.title
        # return self.title, self.user.get_username

    