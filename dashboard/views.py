from django.shortcuts import render
from django.views import View


class IndexView(View):
    """Dashboard as a view
    """

    template_name = 'dashboard/index.html'

    def get(self, request):
        return render(request, self.template_name)
