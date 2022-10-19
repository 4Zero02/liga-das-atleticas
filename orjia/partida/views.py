from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
