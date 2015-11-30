from django.db import models
from cms.models.pluginmodel import CMSPlugin
from ckeditor.fields import RichTextField


class MultipleTextImages(CMSPlugin):

    title = models.CharField(
        verbose_name='Title',
        max_length=40,
        null=True,
        blank=True,
    )

    title_text = models.TextField(
        verbose_name='Title Text',
        max_length=124,
        null=True,
        blank=True,
    )

    subtitle_1 = models.CharField(
        verbose_name='Subtitle 1',
        max_length=16,
        null=True,
        blank=True,
    )

    image1 = models.ImageField(
        verbose_name='Image 1',
        help_text='Upload an Iamge',
        upload_to='multiple_text_images',
        default=False,
    )

    subtitle_text_1 = RichTextField(
        verbose_name='Subtitle Text 1',
        max_length=265,
        null=True,
        blank=True,
    )

    subtitle_2 = models.CharField(
        verbose_name='Subtitle 2',
        max_length=16,
        null=True,
        blank=True,
    )

    image2 = models.ImageField(
        verbose_name='Image 2',
        help_text='Upload an Iamge',
        upload_to='multiple_text_images',
        default=False,
    )

    subtitle_text_2 = RichTextField(
        verbose_name='Subtitle Text 2',
        max_length=265,
        null=True,
        blank=True,
    )

    subtitle_3 = models.CharField(
        verbose_name='Subtitle 3',
        max_length=16,
        null=True,
        blank=True,
    )

    image3 = models.ImageField(
        verbose_name='Image 3',
        help_text='Upload an Iamge',
        upload_to='multiple_text_images',
        default=False,
    )

    subtitle_text_3 = RichTextField(
        verbose_name='Subtitle Text 3',
        max_length=265,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Multiple Text and Images'

    def __unicode__(self):
        return self.title
