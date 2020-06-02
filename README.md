# django-demo

> django 官网 跟随练习

+ urls
  - path 路径映射  url -> view 
  - pk 传递 uri 参数
  - view as_view 函数 和 类 
  - name url 的名称，用户 reverse 和 template 中 url 返回 path路径
  - app_name 全局命名空间，用以代表app

+ views
   - 函数， 第一个参数为 request，之后的参数为 uri参数
   - 类 继承自generic 提供的 APIView，以及 混合 Mixins 提供的 mixins ，默认提供 众多api及属性方法
      - 
   
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
  
