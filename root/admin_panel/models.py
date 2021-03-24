from django.db import models


class Adminz(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    # permissions
    add_user = models.BooleanField(default=True)
    delete_user = models.BooleanField(default=True)
    view_all_user = models.BooleanField(default=True)
    edit_user = models.BooleanField(default=True)
    view_statistics = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.username}'

class Userz(models.Model):
    name = models.CharField(max_length=200)
    mobile_no = models.IntegerField()
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=200)
    department_name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=1000)

    # permissions
    add_user = models.BooleanField(default=False)
    delete_user = models.BooleanField(default=False)
    view_all_user = models.BooleanField(default=False)
    edit_user = models.BooleanField(default=False)
    view_statistics = models.BooleanField(default=False)