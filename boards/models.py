from django.db import models


class Board(models.Model):
    class Meta:
        verbose_name = "board"
        verbose_name_plural = "boards"

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name
