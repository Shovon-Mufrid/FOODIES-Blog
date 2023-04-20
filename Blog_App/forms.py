from django import forms
from Blog_App.models import Blog, Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)


