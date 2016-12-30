from django.shortcuts import HttpResponse, render_to_response, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse


def index(request):
    template = loader.get_template('taxistation/homepage.html')
    return HttpResponse(template.render())