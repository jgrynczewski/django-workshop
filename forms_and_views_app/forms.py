from django import forms

from forms_and_views_app.models import Message, Person


# Django form
class MessageForm(forms.Form):
    CHOICES = [
        ("", "---------"),
        ("question", "Pytanie"),
        ("other", "Inne")
    ]

    name = forms.CharField(label="Imię")
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(choices=CHOICES, label="Kategoria")
    subject = forms.CharField(label="Tytuł")
    body = forms.CharField(label="Treść", widget=forms.Textarea)
    date = forms.DateField(label="Ulubiona data", widget=forms.widgets.NumberInput(attrs={'type': 'date'}))
    time = forms.TimeField(label="Ulubiony czas", widget=forms.widgets.NumberInput(attrs={'type': 'time'}))


# Model form
class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        labels = {
            "name": "Imię",
            "email": "Email",
            "category": "Kategoria",
            "subject": "Tytuł",
            "body": "Treść",
            "date": "Ulubiona data",
            "time": "Ulubiony czas"
        }
        widgets = {
            "date": forms.widgets.NumberInput(attrs={'type': 'date'}),
            "time": forms.widgets.NumberInput(attrs={'type': 'time'})
        }

# django-cripsy-form

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
