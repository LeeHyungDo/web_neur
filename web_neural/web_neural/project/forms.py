# -*- coding: utf-8 -*-
from django import forms

class SubjectForm(forms.Form):
    subjectfile = forms.ImageField(
            label = 'Select Subject image'
    )
class StyleForm(forms.Form):
    stylefile = forms.ImageField(
            label = 'Select Style image'
    )
    

