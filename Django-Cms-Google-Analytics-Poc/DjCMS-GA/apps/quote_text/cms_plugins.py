from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from apps.quote_text.models import QuoteText


class QuoteTextPlugin(CMSPluginBase):
    model = QuoteText
    name = 'Quote Text'
    render_template = 'quote_text/quote_text.html'
    cache = False
    # import ipdb
    # ipdb.set_trace()

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(QuoteTextPlugin)
