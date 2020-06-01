from django.urls import path
from . import views

"""
path 中的 name 是为了 在 template 中可以通过 {% url 'detail' %} 引用到
如果多个 应用的 urls 的 path中使用了同一个name的话，需要给urls添加要给命名空间
app_name, 那么相应的 templates 中 的 url 也要加上命名空间 {% url 'polls:detail' %} 
"""
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/results/', views.results, name='results'),
    path('<int:pk>/vote/', views.vote, name='vote'),
]
