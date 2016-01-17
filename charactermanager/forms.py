from charactermanager import models as m
from django import forms

class CharacterModelForm(forms.ModelForm):
    class Meta:
        model = m.Character
