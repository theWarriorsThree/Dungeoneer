from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from charactermanager.models import Ability, Campaign
# Create your views here.

def campaign(request, campaign_name):
    context = RequestContext(request)
    context['campaign'] = get_object_or_404(Campaign,slug=campaign_name)
    return render_to_response('dungeoneer/abilitiesTemplate.html', context)

def campaigns(request):
    context = RequestContext(request)
    return render_to_response('dungeoneer/abilitiesTemplate.html', context)

def abilities(request, campaign_name, player_name):
	context = RequestContext(request)
	context['abilities'] = Ability.objects.all().order_by('recharge')
	return render_to_response('dungeoneer/abilitiesTemplate.html', context)