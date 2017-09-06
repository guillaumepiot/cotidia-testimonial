from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50, null=True)
    comment = models.TextField(max_length=500)
    photo = models.ImageField(blank=True)
    active = models.BooleanField(default=True)

    order_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['order_id', 'name']

    def save(self, *args, **kwargs):
        """Clean old image if replaced."""
        if self.pk:
            original = Testimonial.objects.get(pk=self.pk)
            if original.photo and original.photo != self.photo:
                # Use save=False to avoid recursion loop
                original.photo.delete(save=False)
        super().save(*args, **kwargs)
