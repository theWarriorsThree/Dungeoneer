from django.contrib import admin
from charactermanager.models import Campaign, Character, Ability, AbilityKeyword, Monster, MonsterPower, MonsterCategory, MonsterSubCategory, MonsterKeyword

class CampaignAdmin(admin.ModelAdmin):
    filter_horizontal = ('characters', )

class CharacterAdmin(admin.ModelAdmin):
    save_as = True
    filter_horizontal = ('abilities', )

class AbilityAdmin(admin.ModelAdmin):
    save_as = True
    filter_horizontal = ('keywords', )

class MonsterAdmin(admin.ModelAdmin):
    save_as = True
    filter_horizontal = ('keywords','auraKeywords')

class MonsterPowerAdmin(admin.ModelAdmin):
    save_as = True
    filter_horizontal = ('keywords',)

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(AbilityKeyword)

admin.site.register(Monster, MonsterAdmin)
admin.site.register(MonsterPower, MonsterPowerAdmin)
admin.site.register(MonsterKeyword)
admin.site.register(MonsterCategory)
admin.site.register(MonsterSubCategory)
