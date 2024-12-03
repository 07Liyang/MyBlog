from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    USER_GENDER_TYPE = (
        ('male', 'male'),
        ('female', 'female'),
    )

    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    # 短文本或者标题字段
    nike_name = models.CharField('Nike_Name', max_length=23, blank=True, default='')
    desc = models.TextField('Personal Profile', max_length=200, blank=True, default='')
    gexing = models.CharField('Personalised Signature', max_length=100, blank=True, default='')
    birthday = models.DateField('Birthday', null=True, blank=True)
    gender = models.CharField('Gender', max_length=6, choices=USER_GENDER_TYPE, default='male')
    address = models.CharField('Address', max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='images/%Y/%m', default='images/default.png', max_length=100, verbose_name = 'Avatar')
