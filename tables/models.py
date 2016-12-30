from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    post_name = models.CharField(max_length=30, db_column='post_name')
    salary = models.CharField(max_length=20, db_column='salary')
    duties = models.CharField(max_length=500, db_column='duties')
    requirements = models.CharField(max_length=500, db_column='requirements')

    def get_absolute_url(self):
        return reverse('tables:create_post')

    def __str__(self):
        return str(self.id)


class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True, db_column='w_id')
    full_name = models.CharField(max_length=100, db_column='fullname')
    age = models.IntegerField(db_column='age')
    gender = models.CharField(max_length=15, db_column='gender')
    address = models.CharField(max_length=200, db_column='address')
    phone = models.CharField(max_length=20, db_column='w_phone')
    passport = models.CharField(max_length=10, db_column='passport')
    post_id = models.ForeignKey(Post, on_delete=models.PROTECT, db_column='post_id')

    def get_absolute_url(self):
        return reverse('tables:create_worker')

    def __str__(self):
        return self.full_name