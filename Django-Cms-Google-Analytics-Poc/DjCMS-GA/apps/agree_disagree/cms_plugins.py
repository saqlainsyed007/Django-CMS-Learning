from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from apps.dnn_agree_disagree.models import DNNAgreeDisagree


class DNNAgreeDisagreePlugin(CMSPluginBase):
    model = DNNAgreeDisagree
    name = 'Agree Disagree'
    render_template = 'agree_disagree/agree_disagree.html'
    cache = False
    # import ipdb
    # ipdb.set_trace()

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(DNNAgreeDisagreePlugin)
