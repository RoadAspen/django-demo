# django-demo

> django 官网 跟随练习

+ settings
    - BASE_DIR 项目绝对路径
    - SECRET_KEY 项目密钥
    - LANGUAGE_CODE 语言 zh-hans
    - TIME_ZONE 时区 Asia/Shanghai
    - ALLOWED_HOSTS 可接受 ip 访问，开发时可设置为 * ，所有
    - INSTALLED_APPS 安装的app，外部安装或者自建的app需要在这里挂载到项目
    - MIDDLEWARE 中间件
    - ROOT_URLCONF 根路由
    - TEMPLATES admin 的公共模板
    - DATABASES 数据库配置
    - AUTH_PASSWORD_VALIDATORS 密码验证
    - STATIC_URL 静态资源路径，查找根目录 static 文件夹 或者 app 内部 static 目录，可以忽略 static文件夹 之上的路径

+ urls
    - path 路径映射  url -> view 
    - pk 传递 uri 参数
    - view as_view 函数 和 类 
    - name url 的名称，用户 reverse 和 template 中 url 返回 path路径
    - app_name 全局命名空间，用以代表app

+ views
    - 函数， 第一个参数为 request，之后的参数为 uri参数
    - 类继承自generic 提供的 APIView，以及 混合 Mixins 提供的 mixins ，默认提供 众多api及属性方法
        - queryset 查询集
        - get_queryset 获取 queryset
        - template_name 模板的路径名
        - context_object_name 传入模板的变量名
        - 如果需要筛选或者自定义返回queryset，则需要覆写 queryset 或者 在 get_queryset return 之前做一些事情
     - loader.get_template 获取模板资源
    - render 默认实现了loader.get_template 和 template.render_to_string 方法
   
+ templates
    - 模板文件夹，html 包含模板语法，语法可以采用{% %} 包裹的 for if 以及 load static 之后的 static 和 url 语法，还有 model语法
    - {{}} 双括号 用于展示数据
    - 根目录下的templates 则用来定制覆盖 django admin 后台页面，需要在 setting 的 templates 选项中设置 dirs 路径

+ models
    - 定义fields， foreignkey  charfield datetimefield  integetfield booleanfield textfield manytomanyfield 等
    - field 的 verbose_name 以及 meta 中的 verbose_name verbose_name_plural(复数) 等 作用于 django admin 后台管理
    - __str__ 定义django admin 后台中用哪个字段表示 一条数据
    - was_published_recently 函数，作用于实例（instance）上执行，类似于给一条数据提供一个方法，可设置多个
    - foreignkey 设置 related_name 用于 外联model 实例反向查询当前model实例
  
+ admin
    - ModelAdmin 模型在 django admin后台显示的配置
        - 继承自 admin.ModelAdmin
        - @admin.register(Modelname) 将Admin类注册到 django admin 后台
        - list_display 配置 在 admin 中显示的list 属性
        - list_filter 配置 admin中的 可筛选字段
        - fields 配置 在 编辑页 显示的 的 可编辑字段以及出现顺序
        - fieldsets 用于将 编辑选项分块显示，主要用于字段分类，fields 和 fieldsets 不能同时显示
        - inlines 配置 model foreignkey 的 Modelinline
    - ModelInline  
        - 继承自 admin.TabularInline（紧密布局） 或者 admin.StackedInline （松散布局）
        - model 指定 Model
        - extra 指定 出现几条可编辑列
    
     
  
