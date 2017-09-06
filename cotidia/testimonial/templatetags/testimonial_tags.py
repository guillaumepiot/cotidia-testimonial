from django import template

from cotidia.testimonial.models import Testimonial

register = template.Library()


@register.assignment_tag
def get_testimonials():
    return Testimonial.objects.filter(active=True).order_by('order_id')
