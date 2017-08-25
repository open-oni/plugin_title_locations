from django.template.defaulttags import register

# Filter for looking up a dict value in templates
#
# Usage: {{ thing|lookup:some_variable }}
@register.filter(name='lookup')
def lookup(obj, key):
    return obj[key]

