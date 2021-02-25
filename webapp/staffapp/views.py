from django.shortcuts import render, redirect
from django.contrib import auth
from data.models import Place, Session, EndSession, StartSession, Item
from data.forms import SessionForm, StratSessionForm

# Create your views here.
def pg_index(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    userSessions = Session.objects.filter(staff__id=user.profile.id)

    content = {
       'user':user,
       'userSessions':userSessions
    }

    return render(request, 'staffapp/pg_index.html', content)

def pg_settings(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    content = {
       'user':user,
    }
    return render(request, 'staffapp/pg_settings.html',content)

def pg_session_add(request):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            newSession = Session(
                place = form.cleaned_data['place'],
                staff = user.profile,
                isOpen = True
            )
            newSession.save()
            return redirect('session', pk = newSession.id)

    content = {
        'places':Place.objects.all(),
        'sessionForm':SessionForm(),
        'user':user,
    }
    return render(request, 'staffapp/pg_add_session.html',content)

def pg_session_end(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    content = {
       'user':user,
    }
    return render(request, 'staffapp/pg_end_session.html',content)

def pg_session_init(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    forms = []

    curSession = Session.objects.get(id = pk)
    curPlace = curSession.place
    latestSession = Session.objects.filter(place = curPlace, isOpen=False).latest('endTime')
    items = EndSession.objects.filter(session = latestSession)

    if request.method == "POST":
        if request.POST.get('ActionType') == 'add':
            form = StratSessionForm(request.POST)
            if form.is_valid():
                newStartSession = StartSession(
                    session = curSession,
                    item = Item.objects.get(id = request.POST.get('ItemID')),
                    count = form.cleaned_data['count']
                )
                newStartSession.save()
        if request.POST.get('ActionType') == 'dec':
            startSessionItem = StartSession.objects.get(id = request.POST.get('ItemID'))
            startSessionItem.delete()

    for el in items:
        if not StartSession.objects.filter(session = curSession, item = Item.objects.get(id = el.item.id)):
            forms.append(
                {
                    'form':StratSessionForm(),
                    'item':el,
                }
            )
    
    completeItems = StartSession.objects.filter(session = curSession)

    content = {
       'user':user,
       'forms':forms,
       'complete':completeItems,
    }
    return render(request, 'staffapp/pg_init_session.html',content)

def pg_session(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    content = {
       'user':user,
       'session':Session.objects.get(id = pk),
    }
    return render(request, 'staffapp/pg_session.html',content)

def pg_session_change(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    content = {
       'user':user,
    }
    return render(request, 'staffapp/pg_change_session.html',content)

def pg_session_addorder(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    content = {
       'user':user,
    }
    return render(request, 'staffapp/pg_add_order.html',content)