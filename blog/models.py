from django.core.urlresolvers import reverse

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.FileField(blank=True)
    text = models.TextField()	
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
			
	
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
	
    def get_absolute_url(self):
        return reverse("post:detail",kwargs={"id": self.id})


# inverser les dates de publications des articles
		
class Meta:
    ordering = ["-published_date","-created_date"]


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    #categorie = models.ForeignKey('blog.Post', related_name='categorie')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
	
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
		
def approved_comments(self):
	return self.comments.filter(approved_comment=True)

