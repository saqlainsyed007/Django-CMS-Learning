from django.db import models
from cms.models.pluginmodel import CMSPlugin
from ckeditor.fields import RichTextField


class DNNAgreeDisagree(CMSPlugin):

    title = models.TextField(
        verbose_name='Title',
        max_length=40,
        null=True,
        blank=True,
    )

    title_text = RichTextField(
        verbose_name='Title Text',
        max_length=118,
        null=True,
        blank=True,
    )

    subtitle = models.TextField(
        verbose_name='Subtitle',
        max_length=35,
        null=True,
        blank=True,
    )

    subtitle_caption = models.TextField(
        verbose_name='Subtitle Caption',
        max_length=40,
        null=True,
        blank=True,
    )

    subtitle_text = RichTextField(
        verbose_name='Subtitle Text',
        max_length=182,
        null=True,
        blank=True,
    )

    selected = models.BooleanField(
        verbose_name='Selected',
    )

    class Meta:
        verbose_name = 'Agree Disagree'

    def __unicode__(self):
        return self.title
