import re
from django import template

register = template.Library()
wikilink = re.compile("\\b([A-Z][a-z]+[A-Z][a-z]+)\\b")

@register.filter
def wikify(value):
    return wikilink.sub(r"<a href='/wikicamp/\1'>\1</a>", value)
    
