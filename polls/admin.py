from django.contrib import admin
from . import models


# Register your models here.


class Choiceinline(admin.TabularInline):
    """
    会在 question 的编辑页面添加至少三个关联新增选择的选项
    StackedInline 是上下排序比较占地方，可以使用 TabularInline,是左右排列
    inline 必须是 model 类中 有 forginkey 字段才能使用
    """
    model = models.Choice
    extra = 3


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    list_display 是 定义在列表中显示哪些字段以及显示顺序
    list_filter 是 定义筛选过滤,在显示页面增加 查询功能
    fields 则定义 表单中显示的可编辑字段以及显示顺序
    fieldsets 将可编辑表单 分为多个表单集. fields 和 fieldsets 不能同时出现
    """
    list_display = ('id', 'question_text', 'pub_date', 'was_published_recently')
    list_filter = ('pub_date', 'question_text')
    # fields = ['pub_date', 'question_text']

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('时间', {'fields': ['pub_date']}),
    ]

    inlines = [Choiceinline]


@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'votes')

