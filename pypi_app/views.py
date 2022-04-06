from django.shortcuts import render
from django.views import View

from.models import Item


class SearchViev(View):
    def get(self, request):
        return render(request, 'pypi_app/base.html', {'result': Item.objects.all()})