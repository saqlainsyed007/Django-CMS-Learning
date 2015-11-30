from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from apps.multiple_images.models import MultipleImages


class MultipleImagesPlugin(CMSPluginBase):
    model = MultipleImages
    name = 'Multiple Images'
    render_template = 'multiple_images/multiple_images.html'
    cache = False
    # import ipdb
    # ipdb.set_trace()

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(MultipleImagesPlugin)
