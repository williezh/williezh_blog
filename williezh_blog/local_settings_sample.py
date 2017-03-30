#coding:utf-8

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'williezh_blog',      #数据库里的database名称
        'USER': 'root',         #进入数据库的用户名
        'PASSWORD': '100200',   #密码
        'HOST': '127.0.0.1',
        'PORT': 3306,
        }
    }
 
email_conf={
    "EMAIL_BACKEND" : 'django.core.mail.backends.smtp.EmailBackend', #email后端    
    "EMAIL_USE_TLS" : False,  #是否使用TLS安全传输协议    
    "EMAIL_USE_SSL" : True,    #是否使用SSL加密，qq企业邮箱要求使用，网易邮箱则不需要
    "EMAIL_HOST" : 'smtp.126.com',   #发送邮件的邮箱 的 SMTP服务器
    "EMAIL_PORT" : 25,    #发件箱的SMTP服务器端口
    "EMAIL_HOST_USER" : 'jaket5219999@126.com',   #发送邮件的邮箱地址
    "EMAIL_HOST_PASSWORD" : '9999',       #发送邮件的邮箱密码
    "DEFAULT_FROM_EMAIL" : 'jaket5219999@126.com',      #这项可要可不要
}


