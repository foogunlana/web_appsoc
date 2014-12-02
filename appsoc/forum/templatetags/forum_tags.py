from django import template
from forum.utils import client
from time import strftime


import time

register = template.Library()

@register.filter("date_unix")
def date_unix(value):
	try:
		value = int(value)
	except ValueError:
		value = float(value)
	return strftime("%H:%M %p,  %a, %d  %b %y", time.localtime(value))

@register.filter("fetch_comment_item")
def fetch_comment_item(comment_id,key):
	comment_id = int(comment_id)
	collection = client.appsoc.forum
	comment = collection.find_one({'comment_id':comment_id})
	if comment:
		item = comment.get(key,'')
		return item
	return 0

@register.filter("banks")
def banks(username):
	collection = client.appsoc.user
	user = collection.find_one({'username':username})
	banks = user.get('likes',[])
	return [int(pk) for pk in banks]

