from django import forms

class PredictionForm(forms.Form):
    STORY_TYPE_CHOICES = [('Bug', 'Bug'), ('Feature', 'Feature'), ('Task', 'Task')]

    story_type = forms.ChoiceField(choices=STORY_TYPE_CHOICES)
    complexity = forms.FloatField()
    team_experience = forms.FloatField()
    dependencies = forms.FloatField()
    priority = forms.FloatField()