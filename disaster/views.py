from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404, Http404
from django.views import View
from .models import Disaster


class SearchView(View):
    """Search as view
    """
    template_name = 'disaster/search.html'

    def get(self, request):
        q = request.GET['q'].lower()
        disaster = None
        err = None

        try:
            disaster = get_object_or_404(Disaster, name=q)
        except Http404:
            err = Disaster.objects.all()

        return render(request, self.template_name, {'disaster': disaster, 'err': err})
