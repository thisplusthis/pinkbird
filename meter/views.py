# pinkbird/meter/views.py

import datetime

from django.shortcuts import render
from django.utils.timezone import localtime

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Reading


class ReadingsChartData(APIView):

    def get(self, request):
        dates = []
        temperature = []
        humidity = []
        fan = []

        date_from = localtime().replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(minutes=60)
        for reading in Reading.objects.filter(date__gte=date_from).order_by('date'):
            dates.append(reading.date.strftime("%H:%M:%S"))
            temperature.append(reading.temperature)
            humidity.append(reading.humidity)
            fan.append(50 if reading.fan else 0)

        return Response(
            dict(
                labels=dates,
                temperature=temperature,
                humidity=humidity,
                fan=fan
            )
        )


def home(request):
    date = request.GET.get('date', None)
    today = localtime().replace(hour=0, minute=0, second=0, microsecond=0)
    if not date:
        date = today
    return render(request, 'home.html', dict(date=date))
