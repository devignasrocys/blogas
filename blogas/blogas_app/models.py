from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(_("first name"), max_length=50, db_index=True)
    last_name = models.CharField(_("last name"), max_length=50, db_index=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def display_posts(self):
        return ", ".join(post.post for post in self.post.all())
    display_posts.short_description = _("posts")

    def display_comments(self):
        return ", ".join(comment.comment for comment in self.comment.all())
    display_comments.short_description = _("comments")


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
    article = models.CharField(_("article"), max_length=100)
    post = models.TextField(_("post"), max_length=4000)

    def __str__(self) -> str:
        return f"{self.id} {self.author} {self.date} {self.post}"
    
    class Meta:
        ordering = ["date"]
    
    def display_post(self):
        return self.post
    display_post.short_description = _("post")

    def display_date(self):
        return self.date
    display_date.short_description = _("date")


class Comment(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="comment",
        verbose_name=_("author")
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comment",
        verbose_name=_("post")
    )
    comment = models.TextField(_("comment"), max_length=4000)
    date = models.DateField(_("date"))

    def __str__(self) -> str:
        return f"{self.author} {self.comment} {self.date}"
    
    def display_comment(self):
        return self.comment
    display_comment.short_description = _("comment")

    def display_date(self):
        return self.date
    display_date.short_description = _("date")