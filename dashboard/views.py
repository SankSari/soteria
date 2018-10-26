from django.shortcuts import render
from django.views import View
from scripts.alerts import predictEvent, predictCalamity


class IndexView(View):
    """Dashboard as a view
    """

    template_name = 'dashboard/index.html'

    def get(self, request):
        # Get terrorists alerts
        terrorAlerts = predictEvent('terrorist')[1]

        # Get earthquake alerts
        earthquakes = predictCalamity('earthquake')[1]

        # Get hurricane alerts
        hurricanes = predictCalamity('hurricanes')[1]

        # Get tsunami alerts
        tsunami = predictCalamity('tsunami')[1]

        return render(request, self.template_name, {'terror': terrorAlerts, 'earthquakes': earthquakes, 'hurricanes': hurricanes, 'tsunami': tsunami})
