from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView


class AboutUsView(View):

    def get(self,request):
        return render(request, "about/about_us.html", {})