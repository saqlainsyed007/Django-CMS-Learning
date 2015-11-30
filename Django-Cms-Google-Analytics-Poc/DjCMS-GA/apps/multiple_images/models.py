from django.db import models
from cms.models.pluginmodel import CMSPlugin


class MultipleImages(CMSPlugin):

    title = models.CharField(
        verbose_name='Title',
        max_length=40,
        null=True,
        blank=True,
    )

    no_of_images = models.IntegerField(
        choices=((2, '2'), (3, '3')),
        verbose_name="Number of Images",
        default=2,
    )

    image1 = models.ImageField(
        verbose_name='Image 1',
        help_text='Upload an Iamge',
        upload_to='multiple_images',
        default=False,
    )

    image2 = models.ImageField(
        verbose_name='Image 2',
        help_text='Upload an Iamge',
        upload_to='multiple_images',
        default=False,
    )

    image3 = models.ImageField(
        verbose_name='Image 3',
        help_text='Upload an Iamge (Will not appear if images selected are 2)',
        upload_to='multiple_images',
        default=False,
    )

    class Meta:
        verbose_name = 'Multiple Images'

    def __unicode__(self):
        return self.title
