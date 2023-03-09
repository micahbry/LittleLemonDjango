from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import ListView, DeleteView

from .forms import BookingForm
from .models import Menu

from django.template.defaultfilters import stringfilter
from urllib.parse import unquote


@stringfilter
def unquote_raw(value):
    return unquote(value)


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)


class Menu(ListView):
    model = Menu
    template_name = "menu_item.html"


class MenuIem(DeleteView):
    model = Menu
    template_name = "menu_item.html"
