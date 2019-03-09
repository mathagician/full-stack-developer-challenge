# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.paginator import Paginator
from .models import Story
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required

class BlogsListView(generic.ListView):

    template_name = 'stories/storis_list.html'
    context_object_name = 'stories_list'
    paginate_by = 10

    def get_queryset(self):
        """Return all the objects."""

        return Story.objects.all()