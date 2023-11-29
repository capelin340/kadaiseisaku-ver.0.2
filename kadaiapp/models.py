from accounts.models import CustomUser
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(verbose_name='カテゴリ', max_length=10)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    CATEGORY = (('G1','G1レースについて'),('G2','G2レースについて'),('G3','G3レースについて'),('Users','みんなのニュースについて'))
    
    title = models.CharField(verbose_name = 'タイトル',max_length = 200) #文字数
    content = models.TextField(verbose_name = '本文')
    posted_at = models.DateTimeField(verbose_name = '投稿時間',auto_now_add = True)
    category = models.CharField(verbose_name ='カテゴリ',max_length = 50,choices = CATEGORY)

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    category = models.CharField(max_length=50)
    title = models.CharField(verbose_name='タイトル', max_length=50)
    firsttext = models.TextField(verbose_name='本文', max_length=200)
    # image = models.ImageField(verbose_name='画像', upload_to='data_photo')
    posted_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)

    






    def __str__(self):
        return self.title
    



