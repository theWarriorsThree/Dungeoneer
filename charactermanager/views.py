from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from charactermanager.models import Ability, Campaign
# Create your views here.

def campaign(request, slug):
    context = RequestContext(request)
    context['campaign'] = get_object_or_404(Campaign,slug=slug)
    return render_to_response('dungeoneer/abilitiesTemplate.html', context)

def campaigns(request):
    context = RequestContext(request)
    return render_to_response('dungeoneer/abilitiesTemplate.html', context)

def abilities(request):
	context = RequestContext(request)
	context['abilites'] = Ability.objects.all().order_by('priority')
	return render_to_response('dungeoneer/abilitiesTemplate.html', context)