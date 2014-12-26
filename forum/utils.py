from pymongo import MongoClient
from appsoc import params

client = None

def get_mongo_client():
	global client
	if not client:
		try:
			print "Getting new Mongo Client"
			client = MongoClient()
		except Exception:
			raise Exception
	return client

def get_posts():
	cursor = client.appsoc.forum.find({'type':'post'})
	posts = [post for post in cursor if post.get('show','') == True]
	return posts

def get_user(username):
	return client.appsoc.user.find_one({'username':username})

def make_post(post_dict):
	collection = client.appsoc.forum
	ids = collection.distinct('post_id')
	if ids and (None not in ids):
		max_id = max(ids)
		post_dict['post_id'] = int(max_id) + 1
	else:
		post_dict['post_id'] = 1
	return collection.insert(post_dict)

def make_comment(username,comment_dict):
	collection = client.appsoc.forum
	ids = collection.distinct('comment_id')
	if ids and (None not in ids):
		max_id = max(ids)
		comment_dict['comment_id'] = max_id + 1
	else:
		comment_dict['comment_id'] = 1

	comment_id = comment_dict['comment_id']
	comment_post_id = comment_dict.get('comment_post_id',0)
	post_id = int(comment_post_id)

	if post_id:
		post = collection.find_one({'post_id':post_id})
		comments = post.get('comments',[]) + [comment_id]
		post['comments'] = comments
		collection.save(post)

		#USER
		user = client.appsoc.user.find_one({'username':username})
		comments = user.get('comments',[]) + [comment_id]
		user['comments'] = comments
		client.appsoc.user.save(user)

	print 'user: %s made comment with pk %s on post with pk %s'%(username,comment_id,post_id)
	return collection.insert(comment_dict)

def user_post(username,post_id):
	collection = client.appsoc.user
	user = collection.find_one({'username':username})
	posts = user.get('posts',[])
	posts = posts + [str(post_id)]
	user['posts'] = posts
	collection.save(user)
	print 'user: %s posted post with pk %s'%(username,post_id)

def is_valid_pk(pk):
	return True

def get_one_post(pk):
	collection = client.appsoc.forum
	post = collection.find_one({'type':'post','post_id':int(pk)})
	# post = dict()
	return post

def like_post(username,pk):
	collection = client.appsoc.forum
	post = collection.find_one({'type':'post','post_id':int(pk)})
	like_count = post.get('likes',0)
	if like_count:
		like_count = int(like_count) + 1
	else:
		like_count = 1

	user = client.appsoc.user.find_one({'username':username})
	liked_posts = user.get('likes',[]) + [pk]
	user['likes'] = liked_posts
	post['likes'] = like_count
	
	client.appsoc.user.save(user)
	collection.save(post)
	print 'user: %s liked post with pk %s'%(username,pk)

def unlike_post(username,pk):
	collection = client.appsoc.forum
	post = collection.find_one({'type':'post','post_id':int(pk)})

	like_count = post.get('likes',0)
	if like_count and like_count >= 1:
		like_count = int(like_count) - 1
	user = client.appsoc.user.find_one({'username':username})

	liked_posts = user.get('likes',[])

	if pk in liked_posts:
		liked_posts = liked_posts.remove(pk)
		if not liked_posts:
			liked_posts = []

	post['likes'] = like_count
	client.appsoc.user.save(user)
	collection.save(post)
	print 'user: %s un-liked post with pk %s'%(username,pk)




def get_post_time(post_dict):
	return post_dict.get('time','')

def get_post_likes(post_dict):
	return int(post_dict.get('likes',0))


client = get_mongo_client()
