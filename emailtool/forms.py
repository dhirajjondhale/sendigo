from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
# Signup Form (User creation form)
class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Fields to show in the form
# Login Form (Authentication form)
class LoginForm(AuthenticationForm):
    pass  # No need to add extra fields, it automatically uses username and password
# forms.py
from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
# forms.py
from django import forms
class SurveyForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    feedback = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your feedback here...'}))
from django import forms
from .models import Survey
class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name', 'email', 'feedback']
# from django import forms
# from .models import AudienceMember
# class AudienceForm(forms.ModelForm):
#     class Meta:
#         model = AudienceMember
#         fields = '__all__'
from django import forms
from django.core.validators import RegexValidator
from .models import   Contact
from .models import   AddContact
class AddContactForm(forms.ModelForm):
    class Meta:
        model = AddContact
        fields = ['first_name', 'last_name', 'email', 'phone']
from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'first_name', 'last_name', 'address', 'phone_number', 'birthday', 'email_marketing']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 2}),
            'phone_number': forms.TextInput(attrs={'pattern': '[0-9]{10}', 'title': 'Please enter a valid 10-digit phone number'})
        }
# emailtool/forms.py
# emailtool/forms.py
from django import forms
class CampaignForm(forms.Form):
    # your form fields here
    campaign_name = forms.CharField(max_length=100)
    start_date = forms.DateField()
    end_date = forms.DateField()
    # Add other fields as necessary
from django import forms
from .models import EmailRecipient
class EmailRecipientForm(forms.ModelForm):
    class Meta:
        model = EmailRecipient
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }
from django import forms
from .models import LinkButton
class LinkButtonForm(forms.ModelForm):
    class Meta:
        model = LinkButton
        fields = ['type', 'url', 'new_tab']
from django import forms
from .models import Campaign
class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['title', 'status', 'date', 'type', 'folder']

        from django import forms
from .models import Feedback
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback']