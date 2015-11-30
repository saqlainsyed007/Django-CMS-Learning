from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from apps.icon_text_bullets.models import IconTextBullets


class IconTextBulletsPlugin(CMSPluginBase):
    model = IconTextBullets
    name = 'Icon Text Bullets'
    render_template = 'icon_text_bullets/icon_text_bullets.html'
    cache = False
    # import ipdb
    # ipdb.set_trace()

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(IconTextBulletsPlugin)
