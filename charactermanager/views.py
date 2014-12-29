from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from charactermanager.models import Ability, Campaign
# Create your views here.

class Counter:
    count = 0
    
    def __unicode__(self):
        return count

    def increment(self):
        self.count += 1
        return self.count

    def decrement(self):
        self.count -= 1
        return self.count

def campaign(request, campaign_name):
    context = RequestContext(request)
    context['campaign'] = get_object_or_404(Campaign,slug=campaign_name)
    return render_to_response('dungeoneer/campaignTemplate.html', context)

def campaigns(request):
    context = RequestContext(request)
    context['campaigns'] = Campaign.objects.all().order_by('name')
    return render_to_response('dungeoneer/campaignListTemplate.html', context)

def abilities(request, campaign_name, player_name):
    context = RequestContext(request)
    context['counter'] = Counter()
    context['abilities'] = Ability.objects.filter(character__slug=player_name).order_by('recharge')
    return render_to_response('dungeoneer/abilitiesTemplate.html', context)