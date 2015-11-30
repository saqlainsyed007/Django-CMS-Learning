from django.db import models
from cms.models.pluginmodel import CMSPlugin
from ckeditor.fields import RichTextField


class IconTextBullets(CMSPlugin):

    title = models.CharField(
        verbose_name='Title',
        max_length=40,
        null=True,
        blank=True,
    )

    image1 = models.ImageField(
        verbose_name='Image 1',
        help_text='Upload an Iamge',
        upload_to='icon_text_bullets',
        default=False,
    )

    subtitle_1 = models.CharField(
        verbose_name='Subtitle 1',
        max_length=20,
        null=True,
        blank=True,
    )

    text_1 = RichTextField(
        verbose_name='Text 1',
        max_length=600,
        null=True,
        blank=True,
    )

    image2 = models.ImageField(
        verbose_name='Image 2',
        help_text='Upload an Iamge',
        upload_to='icon_text_bullets',
        default=False,
    )

    subtitle_2 = models.CharField(
        verbose_name='Subtitle 2',
        max_length=20,
        null=True,
        blank=True,
    )

    text_2 = RichTextField(
        verbose_name='Text 2',
        max_length=600,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Icon with Bullet Points or Text'

    def __unicode__(self):
        return self.title
