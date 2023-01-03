from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'product/{0}'.format(filename)


class Product(models.Model):
    Pname = models.CharField(max_length=30)
    Pprice = models.IntegerField()
    Pimage = models.ImageField(upload_to='user_directory_path')
    Plink = models.CharField(max_length=350)

    def __str__(self) -> str:
        return self.Pname
