from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.template import loader
from django.urls import reverse

# Create your views here.

from .models import Question, Choice

"""
view 函数，接受的第一个参数就是request,
django 要求返回一个正确HttpResponse 或者 当找不到时应该 抛出 404 not found error
Http404 可以返回要给 404页面
get_object_or_404 可以代替 try except，返回 result 或者 抛错返回 404
还有 get_list_ot_404   filter 
"""


def index(request):
    """
    Model.objects.get() filter(过滤) all order_by
    loader 用来解析路径并返回模板
    使用 template 的render 方法 传入 context 上下文变量
    直接使用render方法，传入request， template 和 context
    render m默认调用了 template 的 render_to_string 方法
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)


def vote(request, pk):
    """
    如果没有传 choice ，则报错，如果 成功则 +1，然后 save， 然后重定向到 results页面
    """
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # reverse 根据传入的 视图全局命名 以及参数反推出 url
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
