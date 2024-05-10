from django.db import models

class Hompage(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    text = models.TextField(
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.id
    def __str__(self):
        return self.title
    def __str__(self):
        return self.text
   