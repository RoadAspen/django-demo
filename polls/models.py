from django.db import models
import datetime

# Create your models here.
from django.utils import timezone  # django 中和时区相关的工具


class Question(models.Model):
    """
    问题模型
    """
    question_text = models.CharField(max_length=200, verbose_name='问题类型')
    pub_date = models.DateTimeField(verbose_name='提出时间')

    def __str__(self):
        """
        django 使用该方法 返回值代表这个对象
        """
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """
    回答
    """
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, verbose_name='选项关联问题')
    choice_text = models.CharField(max_length=200, verbose_name='选项文本')
    votes = models.IntegerField(default=0, verbose_name='投票数')

    def __str__(self):
        """
        django 使用该方法 返回值代表这个对象
        """
        return self.choice_text
