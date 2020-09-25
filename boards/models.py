from django.contrib.auth import get_user_model
from django.db import models


class Board(models.Model):
    class Meta:
        verbose_name = "board"
        verbose_name_plural = "boards"

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Comment(models.Model):
    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    user = models.ManyToManyField(get_user_model(), related_name="comment")
    body = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.user}: {self.body}"
