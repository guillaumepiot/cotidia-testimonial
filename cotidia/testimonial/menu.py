from django.core.urlresolvers import reverse


def admin_menu(context):
    return [
        {
            "text": "Testimonials",
            "icon": "star",
            "url": reverse("testimonial-admin:testimonial-list"),
            "permissions": [
                "testimonial.add_testimonial",
                "testimonial.change_testimonial"
            ],
        },
    ]
