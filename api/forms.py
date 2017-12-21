from django import forms
from api.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
            ),
        }

class GradableForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'gradable-text', 'required': True, 'placeholder': 'Say something...'}
            ),
        }


class SectorForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'sector-text', 'required': True, 'placeholder': 'Say something...'}
            ),
        }
