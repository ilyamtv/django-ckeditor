from django.forms import Textarea
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.conf import settings

class CKEditor(Textarea):
    
    def __init__(self, *args, **kwargs):
        attrs = kwargs.get('attrs', {})
        attrs['class'] = 'django-ckeditor'
        kwargs['attrs'] = attrs
        
        self.ckeditor_config = {
            'toolbar': attrs.get('toolbar', 'Default'),
            'height': attrs.get('height', '300'),                  
        }
        
        super(CKEditor, self).__init__(*args, **kwargs)
        
    def render(self, name, value, attrs=None):
        rendered = super(CKEditor, self).render(name, value, attrs)

        context = {
            'id': attrs['id'], 
            'js_config': '%scmf/ckeditor/default.js' % settings.STATIC_URL
        }

        return rendered +  mark_safe(render_to_string('ckeditor/default.html', dict(context, **self.ckeditor_config)))

    class Media:
        static_url = getattr(settings, 'JS_PACKS_URL', '%spacks/' % settings.STATIC_URL)
        js = (
            '%sckeditor/ckeditor.js' % static_url,
        )
