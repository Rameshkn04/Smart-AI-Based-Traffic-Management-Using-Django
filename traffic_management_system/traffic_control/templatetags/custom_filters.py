# traffic_control/templatetags/custom_filters.py
from django import template

register = template.Library()

from django import template

register = template.Library()

@register.filter
def range_filter(value):
    return range(int(value))
from django import template

register = template.Library()

@register.filter
def officer(value):
    # Your filter logic here
    return value.name  # Or any other logic you need for 'officer'


@register.filter
def remaining_stars(value):
    """Returns the remaining stars to be filled (5 - rating)."""
    return range(5 - value)  # Returns remaining stars to fill to 5

from django import template

register = template.Library()

@register.filter
def range_filter(value):
    """Returns a range for star rating based on the value."""
    return range(value)

