from django.shortcuts import render, redirect
from django.views import View
from user.models import User
from scripts.smsapi import smsAlerts
from scripts.geolocation import getNearbyPlaces
from disaster.models import Disaster


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

        return render(
            request, self.template_name, {'members': members, 'success': None})

    def post(self, request):
        success = False
        data = request.POST
        members = User.objects.filter(incharge=request.user.username)

        if data.get('msg') == 'go_here':
            success = self.go_here(data.get('location'), members)
        elif data.get('msg') == 'safety':
            success = self.safety(data.get('event'), members)
        elif data.get('msg') == 'custom_msg':
            success = self.custom_msg(data.get('message'), members)

        return render(
            request, self.template_name,
            {'members': members, 'success': success})

    def go_here(self, location, members):
        """When the message is to meet somewhere
        Example - nearest field, school etc.
        """

        name, lat, lon, dist = getNearbyPlaces(location)

        message = """
        Soteria Disaster Platform
        Volunteer: {0}
        Move towards following coordinates:
        Place: {1}
        Latitude: {2}
        Longitude: {3}
        """.format(members[0].incharge, name, lat, lon)

        try:
            for mem in members:
                smsAlerts(message, str(mem.phone_number))
        except Exception as e:
            print(e)
            return False

        return True

    def safety(self, event, members):
        """To send safety instructions for particular events
        """

        try:
            disaster = Disaster.objects.get(name=event)
        except:
            return False

        message = """
        Soteria Disaster Platform
        Volunteer: {0}
        Safety instructions for {1}:
        {2}
        """.format(members[0].incharge, disaster.name, disaster.prevention)

        try:
            for mem in members:
                smsAlerts(message, str(mem.phone_number))
        except Exception as e:
            print(e)
            return False

        return True

    def custom_msg(self, message, members):
        """To send custom messages
        """

        try:
            for mem in members:
                smsAlerts(message, str(mem.phone_number))
        except Exception as e:
            print(e)
            return False

        return True
