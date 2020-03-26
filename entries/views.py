from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Entry
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages


class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = "blog_entries"


class EntryView(DetailView):
    model = Entry
    template_name = 'entries/post.html'


class AboutView(TemplateView):
    model = Entry
    template_name = "entries/about.html"


def contact(request):
    template_name = "entries/contact.html"
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your password was updated successfully!')
            return HttpResponseRedirect('/contact.html')
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, template_name, context)
