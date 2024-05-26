from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from registration.models import Profile



# Create your views here.

class ProfileListView(ListView):
    model = Profile
    template_name ="profiles/profile_list.html"     

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    paginate_by = 3


    def get_object(self):
        #recuperar el objeto que se va a editar
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
        




