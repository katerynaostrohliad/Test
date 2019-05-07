from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class Welcome(View):

    def get(self, request):
        return HttpResponse("Hello world")

