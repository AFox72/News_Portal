from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    _rating = models.IntegerField(default=0)

    def update_rating(self):
        self._rating = 0
        for comment in Comment.objects.filter(user=self.user):
            self._rating += comment.rating

        for post in Post.objects.filter(author=Author.objects.get(user=self.user)):
            self._rating += post.rating * 3
            for comments_to_post in Comment.objects.filter(post=post):
                self._rating += comments_to_post.rating
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = 'article'
    news = 'news'
    type = [
        (article, 'article'),
        (news, 'news')
    ]
    type_post = models.CharField(choices=type, max_length=7, default=article)
    publication_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    post_name = models.CharField(max_length=30, unique=True)
    post_text = models.TextField()
    rating = models.IntegerField(default=0, null=True)


    def __str__(self):
        return f'{self.post_name.title()}, {self.publication_date}, {self.self.post_text}'

    def rate1(self):
        grade = input("like or dislike:")
        if grade == 'like':
            self.rating += 1
        if grade == 'dislike':
            self.rating -= 1
        self.save()


    def preview(self):
        return self.post_text[:123] + '...'


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0, null=True)

    def rate2(self):
        grade = input("like or dislike:")
        if grade == 'like':
            self.rating += 1
        if grade == 'dislike':
            self.rating -= 1
        self.save()