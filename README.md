# williezh_blog
----------------------
my personal blog which power by python3,django1.10,pinax and zinnia

<br />

# Demo:
http://williezh.pythonanywhere.com

# Base on

Python: 3.5

Django:1.10

MySQL:5.1.73

# Run at local:

1. 克隆项目：
```
git clone git@github.com:williezh/williezh_blog
```
2. 进入文件夹：
```
cd williezh_blog
```
3. 建立虚拟环境：
```
virtualenv --python=python3.5 venv
```
4. 激活虚拟环境：
```
source venv/bin/activate
```
5. 安装必需包（首次运行）：
```
pip install -r requiredments.txt
```
6. 由local_settings_sample.py创建local_settings.py
```
cp williezh_blog/local_settings_sample.py williezh_blog/local_settings.py
```
7. 修改其中的数据库配置（'USER','PASSWORD','HOST')
```
vi williezh_blog/local_settings.py
```
8. 初始化数据库（首次运行）：
```
python createdatabase.py
python manage.py migrate
python manage.py loaddata mysql_data.json
```
9. 运行服务：
```
python manage.py runserver
```
10. 打开如下网址即可看到运行效果：

http://127.0.0.1:8000/ 
