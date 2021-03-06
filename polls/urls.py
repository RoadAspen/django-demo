from django.urls import path
from . import views

"""
path 中的 name 是为了 在 template 中可以通过 {% url 'detail' %} 引用到
如果多个 应用的 urls 的 path中使用了同一个name的话，需要给urls添加要给命名空间
app_name, 那么相应的 templates 中 的 url 也要加上命名空间 {% url 'polls:detail' %} 
"""
app_name = 'polls'
urlpatterns = [
    # 最原始的基础 url 以及 view 函数
    # path('', views.index, name='index'),
    # path('<int:pk>/', views.detail, name='detail'),
    # path('<int:pk>/results/', views.results, name='results'),
    # path('<int:pk>/vote/', views.vote, name='vote'),

    # 使用view 通用视图
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:pk>/vote/', views.vote, name='vote'),
]
