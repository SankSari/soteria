from django.shortcuts import render
from django.views import View
from scripts.alerts import predictEvent, predictCalamity


class IndexView(View):
    """Dashboard as a view
    """

    template_name = 'dashboard/index.html'

    def get(self, request):
    	# Get terrorists alerts
        terrorAlerts = predictEvent('terrorist')

        # Get earthquake alerts
        earthquakes = predictCalamity('earthquake')

        # Get hurricane alerts
        hurricanes = predictCalamity('hurricanes')

        # Get tsunami alerts
        tsunami = predictCalamity('tsunami')

        return render(request, self.template_name, {'terror': terrorAlerts, 'earthquakes': earthquakes, 'hurricanes': hurricanes, 'tsunami': tsunami})
