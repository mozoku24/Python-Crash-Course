[TOC]

# 准备工作

## 建立虚拟环境

```
1、安装virtualenv
在win PowerShell里命令：pip install --user virtualenv -i https://pypi.tuna.tsinghua.edu.cn/simple

2、创建虚拟环境
virtualenv ll_env
因为用anaconda，所以命令改为：conda create -n ll_env（conda帮助：conda create -h）

3、激活停止虚拟环境
activate | deactivate
在win PowerShell里先用命令cmd，再用命令：activate ll_env
```

## 安装Django

```
1、安装Django
国内都要换源pip install --user Django -i https://pypi.tuna.tsinghua.edu.cn/simple

2、在虚拟环境下，创建Django项目
python -m django startproject learning_log . （特别注意，最后有个点）
新建了个目录learning_log和文件manage.py
learning_log目录下有三个重要文件：settings.py、urls.py、wsgi.py

3、创建数据库
python manage.py migrate

4、启动服务器
python manage.py runserver
打开浏览器，输入：http://localhost:8000/

5、创建应用程序
python manage.py startapp learning_logs（大部分工作）
python manage.py startapp users（用户界面）
文件夹下重要文件：models.py（数据）、admin.py、views.py
```



# Django常用操作

```
- 启动服务器
python manage.py runserver
打开浏览器，输入：http://localhost:8000/

- 迁移项目
修改models.py
python manage.py makemigrations learning_logs
python manage.py migrate

- 创建超级用户
python manage.py createsuperuser
```



# 具体分析

## 模型

```
Django项目名称：learning_log
项目下面有两个应用程序：learning_logs、users

1、在learning_logs的models.py
定义两个class：Topic和Entry

2、在learning_logs的目录下创建forms.py
定义两个class：TopicForm和EntryForm

3、在learning_logs的目录下创建admin.py
可查看http://localhost:8000/admin/

4、在项目learning_log中setting.py里，增加APPS，应用修改的模型

5、执行迁移项目命令
```

## URLs

```
1、项目learning_log中的urls.py
原有admin的路径，增加users和llearning_logs这两个项目的路径

2、应用程序learning_logs中的urls.py
app_name = 'learning_logs'
以下页面路径：index、topics、new_topic、new_entry、edit_entry

3、应用程序users中的urls.py
app_name = 'users'
以下页面路径：login、logout、register
```

## 视图

```
1、在learning_logs中的views.py
def：主页index、所有主题topics、单个主题topic、新主题new_topic、
def：新条目new_entry、编辑条目edit_entry

2、在users中的views.py
def：注册新用户register、注销用户logout_view
```

## 模板

```
1、流程：
在learning_logs | users中新建文件夹templates
在templates中新建文件夹learning_logs | users
在最里面的文件夹learning_logs | users中建立html文件

2、在learning_logs下的html文件
HTML：base、edit_entry、index、new_entry、new_topic、topic、topics

3、在users下的html文件
HTML：login、register
```



# 其他

```
IBM笔记本快捷键:
Fn + B = Break
Fn + P = Pause
Fn + S = SysRq
Fn + K = ScrLK

博客美化:
pip install django-bootstrap3

部署博客:
访问https://heroku.com
```
