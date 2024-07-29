from typing import Any
from django.shortcuts import render, redirect
from stopwatch.models import Stopwatch, Lap
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views import View
from django.utils import timezone
from datetime import timedelta
# Create your views here.

class IndexView(TemplateView):
    template_name = 'stopwatch/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stopwatch = Stopwatch.objects.get(id=1)
        context['stopwatch'] = stopwatch
        context['laps'] = Lap.objects.filter(stopwatch=stopwatch)
        return context

class StartView(View):
    template_name = "stopwatch/start.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        stopwatch = Stopwatch.objects.get(id=1)
        if not stopwatch.is_running:
            stopwatch.start_time = timezone.now()
            stopwatch.is_running = True
        stopwatch.save()
        return redirect('index')
    
class PauseView(View):
    template_name = "stopwatch/pause.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        stopwatch = Stopwatch.objects.get(id=1)
        if stopwatch.is_running:
            elapsed_time = timezone.now() - stopwatch.start_time
            stopwatch.elapsed_time += elapsed_time
            stopwatch.is_running = False
        stopwatch.save()
        return redirect('index')
    
class ResetView(View):
    template_name = "stopwatch/reset.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        stopwatch = Stopwatch.objects.get(id=1)
        stopwatch.start_time = None
        stopwatch.elapsed_time = timedelta(0)
        stopwatch.is_running = False
        stopwatch.save()
        Lap.objects.filter(stopwatch=stopwatch).delete()
        return redirect('index')
    

class RecordLapView(View):
    template_name = "stopwatch/lap.html"
    
    def post(self, request, *args, **kwargs):
        stopwatch = Stopwatch.objects.get(id=1)
        if stopwatch.is_running:
            elapsed_time = timezone.now() - stopwatch.start_time + stopwatch.elapsed_time
            Lap.objects.create(stopwatch=stopwatch, lap_time=elapsed_time)
        return redirect('index')