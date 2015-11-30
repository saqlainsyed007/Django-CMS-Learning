from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from apps.multiple_text_images.models import MultipleTextImages


class MultipleTextImagesPlugin(CMSPluginBase):
    model = MultipleTextImages
    name = 'Multiple Text Images'
    render_template = 'multiple_text_images/multiple_text_images.html'
    cache = False
    # import ipdb
    # ipdb.set_trace()

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(MultipleTextImagesPlugin)
