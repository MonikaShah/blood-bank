# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter

def add_class(field, css_class):
    """Add a class to a form field."""
    return field.as_widget(attrs={'class': css_class})

@register.filter(name='has_group')  # Registering the filter
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
