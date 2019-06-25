from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
import subprocess
import datetime

class HomePageView(TemplateView):
    template_name = "index.html"
    #def get(self, request, **kwargs):
    #    return render(request, 'index.html', context=None)

class MetricsPageView(TemplateView):
    template_name = "metrics.html"

    def post(self, request, *args, **kwargs):
        test = request.POST.get('fitbit')

        data = [
            'fitbit: '+str(test)
        ]

        scriptData = [
        ]

        return render(request, 'results.html', {'test':fitbit})

class ResultsPageView(TemplateView):
    template_name = "results.html"
