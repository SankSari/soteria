from django.shortcuts import render, redirect
from django.views import View
from user.models import User


class IndexView(View):
    """Volunteer index page as view
    """

    template_name = 'volunteer/index.html'

    def get(self, request):

        # If the user is volunteer this page is accessible
        # else user is redirected to home
        if not request.user.volunteer:
            return redirect('/')

        members = User.objects.filter(incharge=request.user.username)

        return render(request, self.template_name, {'members': members})
