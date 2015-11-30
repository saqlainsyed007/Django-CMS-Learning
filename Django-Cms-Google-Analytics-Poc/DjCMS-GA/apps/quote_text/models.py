from django.db import models
from cms.models.pluginmodel import CMSPlugin
from ckeditor.fields import RichTextField


LEFT_CONTENT_TYPE = (
    ('QUOTE', 'Quote'),
    ('TEXT', 'Text')
)

RIGHT_CONTENT_TYPE = (
    ('QUOTE', 'Quote'),
    ('TEXT', 'Text')
)


class QuoteText(CMSPlugin):

    left_item_type = models.CharField(
        choices=LEFT_CONTENT_TYPE,
        verbose_name='Left Content',
        default='TEXT',
        max_length=10,
    )

    left_title = models.CharField(
        verbose_name='Left Title',
        max_length=40,
        null=True,
        blank=True,
    )

    left_text = RichTextField(
        verbose_name='Left Text',
        max_length=800,
        null=True,
        blank=True,
    )

    left_quote = models.TextField(
        verbose_name='Left Quote',
        max_length=120,
        null=True,
        blank=True,
    )

    right_item_type = models.CharField(
        choices=LEFT_CONTENT_TYPE,
        verbose_name='Right Content',
        default='TEXT',
        max_length=200,
    )

    right_title = models.CharField(
        verbose_name='Right Title',
        max_length=40,
        null=True,
        blank=True,
    )

    right_text = RichTextField(
        verbose_name='Right Text',
        max_length=800,
        null=True,
        blank=True,
    )

    right_quote = models.TextField(
        verbose_name='Right Quote',
        max_length=120,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Quote Text'

    def __unicode__(self):
        return 'Quote Text'
