from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from crud1.models import Hackening
from crud1.forms import HackeningForm
from django.contrib import messages


def hackenings(request):
    return render_to_response("hackenings.html", {"hackenings": Hackening.objects.all(), "messages": messages.get_messages(request)})

def add_hackening(request):
    form = HackeningForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Hackening guardado!")
            return HttpResponseRedirect("/crud1/hackenings/list/")

    return render(request, 'form_hackenings.html', {'form': form})

def update_hackening(request, hackeningid):
    instance = get_object_or_404(Hackening, id=hackeningid)
    form = HackeningForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Hackening actualizado!")
            return HttpResponseRedirect("/crud1/hackenings/list/")

    return render(request, 'form_hackenings.html', {'form': form})

def delete_hackening(request, hackeningid):
    instance = get_object_or_404(Hackening, id=hackeningid)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "Hackening %s eliminado!" % hackeningid)
    return HttpResponseRedirect("/crud1/hackenings/list/")

