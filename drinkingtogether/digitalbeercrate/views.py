from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy

from . import models

def is_admin(app):
    return app.request.user.is_superuser

class BeerCrateView(TemplateView):
    template_name = 'beercrate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['beer'] = models.BeerCrate.objects.last()
        context['donation_goals'] = models.DonationGoal.objects.all()
        return context

def get_beer(request):
    beer = models.BeerCrate.objects.last()
    if not beer:
        beer = models.BeerCrate()
    else:
        if beer.lastCount < 150:
            beer.lastCount += 1
    beer.save()

    return redirect('beercrate_index')

def update_beer(request):
    last = models.BeerCrate.objects.last()
    return JsonResponse({'time': last.time.strftime("%Y-%m-%dT%H:%M:%S"), 'lastCount': last.lastCount})

class ConfigView(LoginRequiredMixin, TemplateView):
    template_name = 'config.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['donation_goals'] = models.DonationGoal.objects.all()
        return context

class ConfigEdit(UserPassesTestMixin, UpdateView):
    test_func = is_admin
    model = models.DonationGoal
    template_name = 'form.html'
    fields = ['name', 'website', 'account', 'image', 'description']
    success_url = reverse_lazy('beercrate_config')

class ConfigCreate(UserPassesTestMixin, CreateView):
    test_func = is_admin
    model = models.DonationGoal
    template_name = 'form.html'
    fields = ['name', 'website', 'account', 'image', 'description']
    success_url = reverse_lazy('beercrate_config')

class ConfigDelete(LoginRequiredMixin, DeleteView):
    template_name = 'form_confirm_delete.html'
    model = models.DonationGoal
    success_url = reverse_lazy('beercrate_config')