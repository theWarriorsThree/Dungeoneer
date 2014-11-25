from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from charactermanager.models import Ability
# Create your views here.

def abilities(request):
	context = RequestContext(request)
	context['abilites'] = Ability.objects.all().order_by('priority')
	return render_to_response('dungeoneer/abilitiesTemplate.html', context)