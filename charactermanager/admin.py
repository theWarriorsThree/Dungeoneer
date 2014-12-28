from django.contrib import admin
from charactermanager.models import Campaign, Character, Ability, AbilityKeyword

class CampaignAdmin(admin.ModelAdmin):
    filter_horizontal = ('characters', )

class CharacterAdmin(admin.ModelAdmin):
    filter_horizontal = ('abilities', )
    
class AbilityAdmin(admin.ModelAdmin):
    filter_horizontal = ('keywords', )

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(AbilityKeyword)