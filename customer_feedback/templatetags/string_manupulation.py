__author__ = 'mwas'

from django import template

register = template.Library()

@register.assignment_tag(takes_context=True)
def addString(context,text1,text2):
    return context[(text1 + text2)]

@register.assignment_tag(takes_context=True)
def getContext(context,text):
    return context[text]

@register.assignment_tag(takes_context=True)
def data_in_context(context,text):
    return context.has_key(text)

@register.assignment_tag
def concatenateString(text1,text2):
    return text1+text2

@register.assignment_tag
def convertToStirng(text1):
    return str(text1)





