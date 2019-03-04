from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.entry = kwargs.pop('entry')  # the blog entry instance
        super().__init__(*args, **kwargs)

    def save(self):
        comment = super().save(commit=False)
        comment.entry = self.entry
        comment.save()
        return comment

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.Textarea(attrs={'placeholder': 'Введите ваше имя', 'cols': 50, 'rows': 1}),
            'email': forms.Textarea(attrs={'placeholder': 'email', 'cols': 50, 'rows': 1}),
            'body': forms.Textarea(attrs={'placeholder': 'Введите текст комментария', 'cols': 50, 'rows': 10}),

        }
