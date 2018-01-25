from django import template

from cotidia.testimonial.models import Testimonial

register = template.Library()


@register.simple_tag
def get_testimonials(order_by='order_id'):
    return Testimonial.objects.filter(active=True).order_by(order_by)
