from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.db.models import Q

from charactermanager.models import Ability, AbilityKeyword, Character, Campaign, MonsterCategory, Monster
from charactermanager.forms import CharacterModelForm

from itertools import chain


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
    get_object_or_404(Character,~Q(enabled=False),slug=player_name)
    context = RequestContext(request)
    context['counter'] = Counter()
    context['name'] = player_name
    atwills = Ability.objects.filter(character__slug=player_name, recharge="ATWILL").order_by('name')
    encounters = Ability.objects.filter(character__slug=player_name, recharge="ENCOUNTER").order_by('name')
    dailies = Ability.objects.filter(character__slug=player_name, recharge="DAILY").order_by('name')
    context['abilities'] = list( chain(atwills, encounters, dailies) )
    context['recharges'] = Ability.objects.filter(character__slug=player_name).values_list('recharge', flat=True).distinct()
    context['actionTypes'] = Ability.objects.filter(character__slug=player_name).values_list('actionType', flat=True).distinct()   
    keywordIds = Ability.objects.filter(character__slug=player_name).values_list('keywords', flat=True).distinct()
    context['keywords'] = AbilityKeyword.objects.filter(pk__in=keywordIds)
    return render_to_response('dungeoneer/abilitiesTemplate.html', context)

def edit_user(request, player_name=None):
    context = RequestContext(request)
    if(player_name != None):
        player = Character.objects.filter(slug=player_name)
    else:
        player = None

    if request.method == 'GET':
        form = CharacterModelForm()
    else:
        form = CharacterModelForm(player)

    context['player'] = player
    context['form'] = form
    return render_to_response('dungeoneer/characterFormTemplate.html', context)



def monsters(request):
    context = RequestContext(request)
    context['categories'] = MonsterCategory.objects.all().order_by('name')
#     = {}
#    for category in categories:
#        context['categories'][category.name] = {}
#        for subCategory in category.subCategories.all():
#            context['categories'][category.name][subCategory.name] = {}
#            context['categories'][category.name][subCategory.name]['monsters'] = Monster.objects.filter(category=category.id,subCategory=subCategory.id)
#        context['categories'][category.name]['monsters'] = Monster.objects.filter(category=category.id,subCategory__isnull=True)
    return render_to_response('dungeoneer/monsterListTemplate.html', context)



def handler404(request):
    response = render_to_response('dungeoneer/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('dungeoneer/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
