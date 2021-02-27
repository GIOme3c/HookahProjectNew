from django.shortcuts import render, redirect
from django.contrib import auth
from data.models import Place, Session, EndSession, StartSession, Item, AddToSession, DeleteOnSession, EndSession, Order
from data.forms import SessionForm, StratSessionForm, AddToSessionForm, EndSessionForm, OrderForm

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

    curSession = Session.objects.get(id = pk)
    items = EndSession.objects.filter(session = curSession)
    forms = []

    if request.method == "POST":
        if request.POST.get('ActionType') == 'add':
            newForm = EndSessionForm(request.Post)
            if newForm.is_valid():
                newEndSession = EndSession(
                    session = curSession,
                    item = Item.objects.get(id = request.POST.get('ItemID')),
                    count = newForm.cleaned_data['count']
                )
                newEndSession.save()
        if request.POST.get('ActionType') == 'dec':
            newEndSession = EndSession.objects.get(id = request.POST.get('ItemID'))
            newEndSession.delete()

    for el in StartSession.objects.filter(session = curSession):
        if not EndSession.objects.filter(session = curSession, item = el.item):
            forms.append(
                {
                    'form':EndSessionForm(),
                    'item':el,
                }
            )
    
    completeItems = EndSession.objects.filter(session = curSession)

    content = {
       'user':user,
       'forms':forms,
       'complete':completeItems,

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

def check_acces_dec(newDec, pk):
    if not StartSession.objects.filter(session_id = pk, item = newDec.item):
        return False

    countSumm = StartSession.objects.get(session_id = pk, item = newDec.item).count
    for el in AddToSession.objects.filter(session_id = pk, item = newDec.item):
        countSumm+=el.count
    for el in DeleteOnSession.objects.filter(session_id = pk, item = newDec.item):
        countSumm-=el.count

    if countSumm<float(newDec.count):
        return False

    return True

def pg_session_change(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    if request.method == "POST":
        newForm = AddToSessionForm(request.POST)
        if newForm.is_valid():
            if request.POST.get('formType') == 'add':
                newAdd = AddToSession(
                    session = Session.objects.get(id = pk),
                    item = newForm.cleaned_data['item'],
                    count = newForm.cleaned_data['count']
                )
                newAdd.save()
            if request.POST.get('formType') == 'dec':
                newDec = DeleteOnSession(
                    session = Session.objects.get(id = pk),
                    item = newForm.cleaned_data['item'],
                    count = newForm.cleaned_data['count']
                )
                if check_acces_dec(newDec, pk):
                    newDec.save()
                else:
                    print ('NOPE')
        
    nowAdd = AddToSession.objects.filter(session__id = pk)
    nowDec = DeleteOnSession.objects.filter(session__id = pk)
    content = {
       'user':user,
       'form':AddToSessionForm(),
       'addItems':nowAdd,
       'decItems':nowDec,
    }
    return render(request, 'staffapp/pg_change_session.html',content)

def pg_session_addorder(request, pk=1):
    user = request.user

    if not user.is_authenticated:
        return redirect('autherror')

    if request.method == "POST":
        newOrderForm = OrderForm(request.POST)
        if newOrderForm.is_valid():
            newOrder = Order(
                session = Session.objects.get(id = pk),
                position = newOrderForm.cleaned_data['position'],
                comment = newOrderForm.cleaned_data['comment']
            )
            newOrder.save()

    content = {
       'user':user,
       'form':OrderForm(),
    }
    return render(request, 'staffapp/pg_add_order.html',content)