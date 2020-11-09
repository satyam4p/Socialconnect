from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.http import Http404
from django.views import generic
# Create your views here.
from django.contrib import messages
from braces.views import SelectRelatedMixin

from . import models
from . import forms

from django.contrib.auth import get_user_model
user=get_user_model()

class postlist(SelectRelatedMixin,generic.ListView):
    model=models.posts
    select_related=('user','group')

class userpost(generic.ListView):

    model=models.posts
    template_name = 'posts/user_post_list.html'


    def get_queryset(self):
        try:
            self.post_user=user.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))

        except user.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user']=self.post_user
        return context

class postdetail(SelectRelatedMixin,generic.DeleteView):
    model=models.posts
    select_related = ('user','group')


    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))



class createpost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields=('message','group')
    model=models.posts

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return super().form_valid(form)


class deletepost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model=models.posts
    select_related=('user','group')

    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)






