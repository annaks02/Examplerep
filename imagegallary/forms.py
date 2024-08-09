from django import forms
from .models import ImageGallary
class ImageForm(forms.ModelForm):
    class Meta:
        model=ImageGallary
        fields=('caption','image')
        #ella fields ill varan __all__ use cheyum particular fields nu vendi aa fields name add cheya as above, 
        # spelling correct aayi models ill kodutha pole koduka