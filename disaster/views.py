from django.shortcuts import redirect
from django.views import View


class SearchView(View):
    """Search as view
    """

    def get(self, request):
        return redirect('/')
