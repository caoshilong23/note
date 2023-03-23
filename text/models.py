from django.db import models

from user.models import User


# Create your models here.


class Text(models.Model):
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('修改时间', auto_now=True)
    is_active = models.BooleanField(verbose_name='是否活跃', default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
