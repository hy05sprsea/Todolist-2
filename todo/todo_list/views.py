from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('登録しました'))
            return render(request, 'home.html', {'all_items': all_items})
        else:
            print(form.errors)
            return HttpResponse(form.errors)

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("削除されました"))
    return redirect('home')

def uncleared(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def cleared(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')
