from django import forms
from . import models

class CreateMessage(forms.ModelForm):
    class Meta:
        model = models.contact_form
        fields = ['name', 'email', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Simple email validation, you can add more complex checks
        if not email or '@' not in email or '.' not in email:
            raise forms.ValidationError('Please enter a valid email address.')
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or name.strip() == '':
            raise forms.ValidationError('Please enter your name.')
        return name