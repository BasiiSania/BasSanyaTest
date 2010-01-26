from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import modelformset_factory
from django import forms

from mysite.books.forms import EditorForm
from mysite.books.models import Author


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            authors = Author.objects.filter(first_name__icontains=q)
            return render_to_response('search_results.html',
            {'Authors': authors, 'query': q})
    return render_to_response('search_form.html', {'error': error})


def editor(request):
    data = Author.objects.get(pk=1)
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
#
            cd = form.cleaned_data
            data.first_name = cd['first_name']
            data.last_name = cd['last_name']
            data.birth_day = cd['birth_day']
            data.bio = cd['bio']
            data.contacts = cd['contacts']
            data.save()
            return HttpResponseRedirect('/')
    form = EditorForm(
        initial={
        'first_name': data.first_name,
        'last_name': data.last_name,
        'birth_day': data.birth_day,
        'bio': data.bio,
        'contacts': data.contacts, })
    print form.media 
    return render_to_response('editor_form.html',
                    {'form': form},
                    context_instance = RequestContext(request))
