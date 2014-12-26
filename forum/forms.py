from django import forms

class PostForm(forms.Form):
	title = forms.CharField(label='Title', max_length = 50, required= True)
	body = forms.CharField(widget=forms.Textarea,label='Body')


class CommentForm(forms.Form):
	body = forms.CharField(widget=forms.Textarea(attrs={'class':'small_textarea'}),label='Body',max_length = 300,)
