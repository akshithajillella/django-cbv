from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models

# Create your views here.
# FBV
# def index(request):
#     return render(request, 'index.html')
# CBV
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("class based view")

# FBV
# def index(request):
#     return render(request, 'index.html')
# CBV
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context

# listview, detailview
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # returns school(model name in lower case) + '_list' by default as context dictionary

class SchoolDetailView(DetailView):
    # set custom name for context dictionary
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
    # returns school(model name in lower case) by default as context dictionary