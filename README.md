# Cotidia testimonial

A plugin to manage testimonials. This is primarily used for a brochure
site to display a list of testimonials.

```console
$ pip install -e git+git@code.cotidia.com:cotidia/testimonial.git#egg=cotidia-testimonial
```

## Settings

Add `cotidia.testimonial` to your INSTALLED_APPS:

```python
INSTALLED_APPS=[
    ...
    "cotidia.testimonial",

]
```

## Template tags

In order to retrieve all the testimonials on a page, you can use the
template tag `get_testimonials`.

It will return all the active testimonials in order of order id.

```html
{% load testimonial_tags %}
{% get_testimonials as testimonials %}

{% for testimonial in testimonials %}
    {{testimonial}}
{% endfor %}
```
