from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    rating = models.IntegerField(default=0)

    def update_rating(self):
        rating_of_posts = Post.objects.filter(author=self).aggregate(rp=Sum('rating'))['rp']
        rating_of_comm = Comment.objects.filter(user_comm=self.user).aggregate(rc=Sum('rating'))['rc']
        rating_of_comm_to_post = Comment.objects.filter(post_comm__author=self).aggregate(rcp=Sum('rating'))['rcp']

        self.rating = rating_of_posts * 3 + rating_of_comm + rating_of_comm_to_post
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    article = 'AR'
    news = 'NE'

    CHOICE = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='PostCategory')

    type_post = models.CharField(max_length=2, choices=CHOICE, default=news)
    date_post = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        preview_text = self.text[0:124] + '...'
        return preview_text

    def __str__(self):
        return f'{self.title}: {self.preview()}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_comm = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comm = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()
    date_comm = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


