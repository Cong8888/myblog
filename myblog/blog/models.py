from django.db import models


# 定义图书模型类
class Article(models.Model):
    # 文章的标题
    title = models.CharField(max_length=40, null=False, verbose_name='标题')

    # 文章的摘要
    brief_content = models.TextField(verbose_name='摘要')

    # 文章的主要内容
    content = models.TextField(verbose_name='内容')

    # 文章的发布日期
    publish_date = models.DateTimeField(auto_now=True, verbose_name='发布日期')

    # 逻辑删除
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
