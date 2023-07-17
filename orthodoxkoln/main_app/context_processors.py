from main_app.models import *
from datetime import date


def my_variable(request):
    all_calendar_day = Calendar.objects.all()
    current_date = date.today()
    current_calendar_day = None
    for calendar_day in all_calendar_day:
        if (current_date == calendar_day.date):
            current_calendar_day = calendar_day
    return {'current_calendar_day': current_calendar_day}