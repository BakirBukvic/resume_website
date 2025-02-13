from django.shortcuts import render

# Create your views here.
from .models import Link


def welcome(request):
    context = {}
    
    try:
        linkedin = Link.objects.get(url_name='linkedin')
        context['linkedin'] = linkedin.url
    except Link.DoesNotExist:
        context['linkedin'] = '#'
        
    try:
        github = Link.objects.get(url_name='github')
        context['github'] = github.url
    except Link.DoesNotExist:
        context['github'] = '#'
        
    try:
        skool = Link.objects.get(url_name='skool')
        context['skool'] = skool.url
    except Link.DoesNotExist:
        context['skool'] = '#'
    
    return render(request, 'welcome.html', context)