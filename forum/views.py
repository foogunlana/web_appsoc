from django.shortcuts import render
from utils import client, get_posts, get_user, make_post, make_comment, user_post, is_valid_pk, get_one_post, get_post_time, like_post, unlike_post, get_post_likes
from django.contrib.auth.decorators import login_required #logout_required, permission_required, user_passes_test
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import PostForm, CommentForm
from appsoc import params

import time

# Create your views here.

@login_required(login_url='/login')
def home(request,*args):
	posts = get_posts()
	post_form = PostForm()
	comment_form = CommentForm()

	sorted_posts = sorted(posts,key=get_post_time)
	posts = list(reversed(sorted_posts))

	if len(posts) > params.post_limit:
		posts = posts[:params.post_limit]

	context = {
		'posts':posts,
		'post_form':post_form,
		'comment_form':comment_form
		}
	return render(request,'forum/home.html',context)

@login_required(login_url='/login')
def post(request):
	if request.method == 'POST':
		post_form = PostForm(request.POST)
		username = str(request.user)

		if post_form.is_valid():
			title = post_form.cleaned_data.get('title','')
			body = post_form.cleaned_data.get('body','')

			new_post = {
				'title':title,
				'body':body,
				'author':username,
				'time':time.time(),
				'show':True,
				'type':'post',
				'comments':[],
			}

			post_id = make_post(new_post)	
			user_post(username,post_id)
		else:
			print "form was not valid"

	return HttpResponseRedirect(reverse('forum:home'))

@login_required(login_url='/login')
def comment(request):
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		username = str(request.user)

		if comment_form.is_valid():
			body = comment_form.cleaned_data.get('body','')
			post_id = request.POST.get('post_id','')
			
			new_comment = {
				'body':body,
				'time':time.time(),
				'author':username,
				'show':True,
				'comment_post_id':post_id,
				'type':'comment',
			}

			make_comment(username,new_comment)	
		else:
			print "form was not valid"

	return HttpResponseRedirect(reverse('forum:home'))

@login_required(login_url='/login')
def sort(request,sort):
	if request.method == 'GET':
		posts = get_posts()
		post_form = PostForm()
		comment_form = CommentForm()

		if sort:
			if sort == 'time':
				sorted_posts = sorted(posts,key=get_post_time)
				posts = list(reversed(sorted_posts))
			if sort == 'likes':
				sorted_posts = sorted(posts,key=get_post_likes)
				posts = list(reversed(sorted_posts))
				
		# if len(posts) > params.post_limit:
		# 	posts = posts[:params.post_limit]

		context = {
			'posts':posts,
			'post_form':post_form,
			'comment_form':comment_form,
			'sort':sort,
			}
	return render(request,'forum/home.html',context)

@login_required(login_url='/login')
def sort_user(request,sort):
	if request.method == 'GET':
		posts = get_posts()
		post_form = PostForm()
		comment_form = CommentForm()

		if sort == 'mybanks':
			username = str(request.user)
			user = get_user(username)
			likes = [int(like) for like in user.get('likes','')]
			posts = [post for post in posts if post.get('post_id','') in likes]
			sorted_posts = sorted(posts,key=get_post_time)
			posts = list(reversed(sorted_posts))
		else:
			username = str(sort)
			posts = [post for post in posts if post.get('author','') == username]

		# if len(posts) > params.post_limit:
		# 	posts = posts[:params.post_limit]

		context = {
			'posts':posts,
			'post_form':post_form,
			'comment_form':comment_form,
			'sort':sort,
			}
	return render(request,'forum/home.html',context)

@login_required(login_url='/login')
def detail(request,pk):
	comment_form = CommentForm()

	if request.method == 'GET':
		if is_valid_pk(pk):
			post = get_one_post(pk)
	context = {
		'post':post,
		'comment_form':comment_form,
		}
	return render(request,'forum/post_detail.html',context)

@login_required(login_url='/login')
def like(request,pk):
	if request.method == 'GET':
		username = str(request.user)
		if is_valid_pk(pk):
			user = client.appsoc.user.find_one({'username':username})
			if pk not in user.get('likes',[]):
				like_post(username,pk)

	return HttpResponseRedirect(str('{}#%s'%(pk)).format(reverse('forum:home')))

@login_required(login_url='/login')
def unlike(request,pk):
	if request.method == 'GET':
		username = str(request.user)
		if is_valid_pk(pk):
			user = client.appsoc.user.find_one({'username':username})
			if pk in user.get('likes',[]):
				unlike_post(username,pk)

	return HttpResponseRedirect(str('{}#%s'%(pk)).format(reverse('forum:home')))





