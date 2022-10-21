from django import forms
from .models import Ranking, Partida


class RankingForm(forms.ModelForm):
    class Meta:
        model = Ranking
        fields = ()
