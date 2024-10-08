from django.conf import settings
from django.db import models

from PIL import Image


class Photo(models.Model):

    # Images treatments
    IMAGE_MAX_SIZE = (800, 800)

    # Fields
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

    def resize_image(self):
        image = Image.open(self.image.path)
        image.thumbnail(self.IMAGE_MAX_SIZE)

        # save teh resized image to the file system
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        # make sure that data saving still work
        super().save(*args, **kwargs)

        # resize photo
        self.resize_image()


class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    word_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def _get_word_count(self):
        word_count = len(self.content.split(' '))

        return word_count

    def save(self, *args, **kwargs):
        # compute word count
        self.word_count = self._get_word_count()

        # save
        super().save(*args, **kwargs)


