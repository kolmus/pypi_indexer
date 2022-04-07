from django.shortcuts import render
from django.views import View
from django.db.models import Q
# from django.core.paginator import Paginator

from .models import Item


def search(values) -> set:
    """Search for every word in values in database

    Args:
        values (str): words to search separated with space ' '

    Returns:
        set: matched objects of Item model
    """    
    search_values = values.split(" ")
    result = set()

    for value in search_values:
        for item in Item.objects.filter(
            Q(title__icontains=value)
            | Q(version__icontains=value)
            | Q(link__icontains=value)
            | Q(guid__icontains=value)
            | Q(description__icontains=value)
            | Q(author_name__icontains=value)
            | Q(author_email__icontains=value)
        ):
            result.add(item)

    return result


class SearchViev(View):
    def get(self, request):
        """
        Main View to show all packages on '/' path

        """        
        return render(request, "pypi_app/base.html", {"result": Item.objects.all()})

    def post(self, request):
        """ 
        View to show search results

        Args:
            search (request data): str separated with spaces with words to search

        Returns:
            result: Set with Item objects
        """        
        search_data = request.POST["search"]
        result = search(values=search_data)
        return render(request, "pypi_app/base.html", {"result": result})


# class SearchViev(View):
#     def get(self, request):
#         items = Item.objects.all()
#         paginator = Paginator(items, per_page=12)
#         page = request.GET.get('page')
#         items = paginator.get_page(page)
#         return render(request, "pypi_app/base.html", {"result": items})

#     def post(self, request):
#         search_data = request.POST["search"]
#         result = search(values=search_data)
#         paginator = Paginator(result, per_page=9)
#         page = request.GET.get('page')
#         result = paginator.get_page(page)
#         return render(request, "pypi_app/base.html", {"result": result})