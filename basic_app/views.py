from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

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

