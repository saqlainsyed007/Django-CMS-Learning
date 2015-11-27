from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin

# from cms.models.pluginmodel import CMSPlugin
from .models import Hello, ArticlePluginModel, AssociatedItem

# ugettext_lazy is used to translate text to user's language. If you don't
# specify your strings using this function, they will not be translated.
from django.utils.translation import ugettext_lazy as _  # '_' is alias


# cms.plugin_base.CMSPluginBase is actually a subclass of
# django.contrib.admin.options.ModelAdmin
class HelloPlugin(CMSPluginBase):
    # Basic Plugin Model if in case you don't need any special Model Config
    # model = CMSPlugin
    model = Hello
    name = _("Hello Plugin")
    # The template to render
    render_template = "hello/hello_plugin.html"
    # Tells cms whether to cache plugin's output to speed up further instances
    # of the plugin in the other templates
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(HelloPlugin)


class ItemInlineAdmin(admin.StackedInline):
    model = AssociatedItem


class ArticlePlugin(CMSPluginBase):
    model = ArticlePluginModel
    name = _("Article Plugin")
    render_template = "article/index.html"

    # The template to render when plugin form is displayed
    change_form_template = "article/custom-form.html"
    inlines = (ItemInlineAdmin,)

    def render(self, context, instance, placeholder):
        items = instance.associated_item.all()
        context.update({
            'items': items,
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(ArticlePlugin)
