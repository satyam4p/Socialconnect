from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views import generic

from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.
from . import models

class creategroup(LoginRequiredMixin,generic.CreateView):
    fields=('name','description')
    model=models.group

class singlegroup(generic.DetailView):
    model=models.group

class listgroup(generic.ListView):
    model=models.group

class joinfroup(LoginRequiredMixin,generic.RedirectView):


    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    def get(self,request,*args,**kwargs):
        Group=get_object_or_404(models.group,slug=self.kwargs.get('slug'))

        try:
            models.groupmember.objects.create(user=self.request.user,group=Group)

        except:
            messages.warning(self.request,'warning alrady a member!')
        else:messages.success(self.request,"you are now a member!")


        return super().get(request,*args,**kwargs)

class leavegroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        try:
            membership=models.groupmember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()
        except models.groupmember.DoesNotExist:
            messages.warning(self.request,"sorry you are not in this group")
        else:
            membership.delete()
            messages.success(self.request,"you have left the group")
        return super().get(request,*args,**kwargs)









