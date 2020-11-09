from django.db import models
from django.urls import reverse
from django.conf import settings
# import misaka
from groups.models import group
# Create your models here.
from django.contrib.auth import get_user_model

user=get_user_model()

class posts(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,related_name='posts')
    created_at=models.DateTimeField(auto_now=True)
    message=models.TextField()
    message_html=models.TextField(editable=False)
    group=models.ForeignKey(group,on_delete=models.CASCADE,related_name='posts',null=True,blank=True)

    def __str__(self):
        return self.message
    def save(self,*args,**kwargs):
        self.message_html=misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})
    class Meta():
        ordering=['-created_at']
        unique_together=['user','message']


