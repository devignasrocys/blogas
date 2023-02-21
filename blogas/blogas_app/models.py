from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(_("first name"), max_length=50, db_index=True)
    last_name = models.CharField(_("last name"), max_length=50, db_index=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    id = models.UUIDField(
        _("ID"),
        primary_key=True,
        default=uuid.uuid4,
        help_text=_("Unique ID for ")
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="post",
        verbose_name=_("author")
    )
    date = models.DateField(_("date"))
    post = models.TextField(_("post"), max_length=4000)

    def __str__(self) -> str:
        return f"{self.id} {self.author} {self.date} {self.post}"
    
    class Meta:
        ordering = ["date"]