from cms.models.pluginmodel import CMSPlugin
from django.db import models


# Class that is used for plugins inherits from 'CMSPlugin' rather than
# 'models.Model'. CMSPlugin is a subclass of 'Model'.
class Hello(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')


"""
    Everytime the page with your custom plugin is published the plugin is
    copied. So if your custom plugin has foreign key (to it, or from it) or
    many-to-many relations you are responsible for copying those related
    objects, if required, whenever the CMS copies the plugin. It won't do it
    for you automatically.

    Your plugin may have items with foreign keys to it, which will typically
    be the case if you set it up so that they are inlines in its admin. So you
    might have two models, one for the plugin and one for those items.

    You'll then need the copy_relations() method on your plugin model to loop
    over the associated items and copy them, giving the copies foreign keys to
    the new plugin.
"""


class ArticlePluginModel(CMSPlugin):
    title = models.CharField(max_length=50)
    # If you had a Many2ManyField rel like this then,
    # sections = models.ManyToManyField(Section)

    def copy_relations(self, oldinstance):
        for associated_item in oldinstance.associated_item.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            associated_item.pk = None
            associated_item.plugin = self
            associated_item.save()
            # The instance of many to many is copied like this
            # self.sections = oldinstance.sections.all()


class AssociatedItem(models.Model):
    plugin = models.ForeignKey(ArticlePluginModel,
                               related_name="associated_item")


"""
    return u'{0}'.format(self.guest_name) in the __unicode__ method if at all
    you use. NOTE that the return type must be UTF-8 String
"""
