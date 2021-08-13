from django.db import models


class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="")
    head0 = models.CharField(max_length=100, default="")
    chead0 = models.CharField(max_length=500, default="")
    head1 = models.CharField(max_length=100, default="")
    chead1 = models.CharField(max_length=500, default="")
    head2 = models.CharField(max_length=100, default="")
    chead2 = models.CharField(max_length=500, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="shop/image", default="")

    def __str__(self):
        return self.title