from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.

from .models import Question, Choice

"""
view 函数，接受的第一个参数就是request,
django 要求返回一个正确HttpResponse 或者 当找不到时应该 抛出 404 not found error
Http404 可以返回要给 404页面
get_object_or_404 可以代替 try except，返回 result 或者 抛错返回 404
还有 get_list_ot_404   filter 
def 为 基础视图，提供最基础的函数函数

通用视图则使用 generic class APIView 或者  decorator 函数装饰器 api_view 
"""


def index(request):
    """
    Model.objects.get() filter(过滤) all order_by
    loader 用来解析路径并返回模板
    使用 template 的render 方法 传入 context 上下文变量
    直接使用render方法，传入request， template 和 context
    render m默认调用了 template 的 render_to_string 方法
    基础视图
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    """
    listView 结合了 generic 的 APIView 和 mixins 的 ListMixin,提供的context 是 modelname_list ，这里是
    last_question_list ，不是默认的，所以需要重命名
    这里由于传入的 contxt 不是 model 的小写，所以需要另外命名
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        queryset = Question.objects.order_by('-pub_date')[:5]
        return queryset


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


class DetailView(generic.DetailView):
    """
    detailview 主要是 generic 的 apiview 和 mixins 的 DetailMixins ，主要作用是接收pk参数
    返回 question 的 id 详情，期望从 url中捕获到 pk 关键词，所以 在url中需要把参数改为 pk
    template_name 有一个默认的名称 即  app name/model name _detail.html
    如果要对 queryset做一些筛选，则需要重写 get_queryset 或者 queryset
    """
    template_name = 'polls/detail.html'
    model = Question
    queryset =  Question.objects.filter(pub_date__lte=timezone.now())
    # def get_queryset(self):
    #     return Question.objects.filter(pub_date__lte=timezone.now())


def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)


class ResultView(generic.DetailView):
    """
    detailView 内部实现了 get_object 和 context ，内部获取到 pk， **kwargs
    """
    template_name = 'polls/results.html'
    model = Question


def vote(request, pk):
    """
    如果没有传 choice ，则报错，如果 成功则 +1，然后 save， 然后重定向到 results页面
    """
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        # 如果请求是 post 且未提供 choice
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # reverse 根据传入的 视图全局命名 以及参数反推出 url
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
