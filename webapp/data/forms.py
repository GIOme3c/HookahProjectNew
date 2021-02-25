from django.forms import ModelForm
from .models import Place, Session, StartSession, AddToSession

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['title', 'adres', 'preview']

class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ['place']

class StratSessionForm(ModelForm):
    class Meta:
        model = StartSession
        fields = ['count']

class AddToSessionForm(ModelForm):
    class Meta:
        model = AddToSession
        fields = ['item', 'count']