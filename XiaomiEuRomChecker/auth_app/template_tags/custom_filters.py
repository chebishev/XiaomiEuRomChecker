from django import template

register = template.Library()


@register.filter
def placeholder(input_field, text):
    input_field.field.widget.attrs['placeholder'] = text
    return input_field
