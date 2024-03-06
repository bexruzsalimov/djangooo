from user.models import User
from django import forms
from django.forms.widgets import TextInput
from .models import Post, Category, Comment

      



class CreatePostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Title', 'type': 'text'}
    ))
    summary = forms.CharField(max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Summary', 'type': 'text'}
    ))
    text = forms.CharField(
        widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Body', 'rows': '3'}
    ))
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['category', 'name', 'summary', 'text', 'image']
        

class UpdatePostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Title', 'type': 'text'}
    ))
    summary = forms.CharField(max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Summary', 'type': 'text'}
    ))
    text = forms.CharField(
        widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Body', 'rows': '3'}
    ))
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['category', 'name', 'summary', 'text', 'image',]

class CommentForm(forms.ModelForm):
    body = forms.CharField(label=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'fikringizni shu yerda qoldiring...', 'rows': '3'}
    ))
    class Meta:
        model = Comment
        fields = ['body', 'parent']


