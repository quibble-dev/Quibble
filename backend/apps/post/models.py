from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern

from apps.comment.models import Comment
from apps.community.models import Community
from apps.user.models import Profile
from mixins.models.created_at import CreatedAtMixin
from mixins.models.is_public import IsPublicMixin
from mixins.models.shortuuid import ShortUUIDMixin

cover_file_pattern = FilePattern(filename_pattern="cover/{uuid:s}{ext}")

# Create your models here.


class Post(CreatedAtMixin, IsPublicMixin, ShortUUIDMixin):
    community = models.ForeignKey(
        Community,
        related_name='posts',
        verbose_name=_('community'),
        on_delete=models.CASCADE,
    )
    poster = models.ForeignKey(
        Profile,
        related_name='posts',
        verbose_name=_('poster'),
        on_delete=models.CASCADE,
    )
    highlighted = models.BooleanField(_('highlighted'), default=False)
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=25, blank=True)
    content = models.TextField(_('content'), blank=True)
    cover = models.ImageField(
        _('cover'),
        upload_to=cover_file_pattern,
        blank=True,
        null=True,
    )
    upvotes = models.ManyToManyField(
        Profile, blank=True, verbose_name=_('upvotes'), related_name=_('upvoted_posts')
    )
    downvotes = models.ManyToManyField(
        Profile, blank=True, verbose_name=_('downvotes'), related_name=_('downvoted_posts')
    )
    comments = models.ManyToManyField(
        Comment, related_name='comments', blank=True, verbose_name=_('comments')
    )

    def save(self, *args, **kwargs):
        """Override save method to slugify title."""
        if not self.slug:
            self.slug = slugify(self.title[:25])

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.pk}/{self.slug}'

    class Meta:  # pyright: ignore
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']
