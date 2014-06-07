__author__ = 'mwas'

from django import template
from timetable.scheduler.CSP import *
import pdb


register = template.Library()



@register.assignment_tag(takes_context=False)
def format_time(time_data):
    t = time_data.split(":")
    time = Time(t[0], t[1], t[2])

    return  str(time)

