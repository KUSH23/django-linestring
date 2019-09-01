from django import forms

from polygen.models import TwoPoints

class PostForm(forms.ModelForm):

    class Meta:
        model = TwoPoints
        fields=[
            '_lat',
            '_long',
            '_lat1',
            '_long1',
        ]