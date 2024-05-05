from django import forms
from Rentizy.models.user_image import UserImage
from Rentizy.models.user import User

class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['image', 'description']

    