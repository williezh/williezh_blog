#coding:utf-8

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'williezh_blog',      #数据库里的database名称
        'USER': 'williezh',         #进入数据库的用户名
        'PASSWORD': 'jaket5219999',   #密码
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset':'utf8mb4',
            },
        }        
    }
 
email_conf={
    "EMAIL_BACKEND" : 'django.core.mail.backends.smtp.EmailBackend', #email后端    
    "EMAIL_USE_TLS" : False,  #是否使用TLS安全传输协议    
    "EMAIL_USE_SSL" : False,    #是否使用SSL加密，qq企业邮箱要求使用，网易邮箱则不需要
    "EMAIL_HOST" : 'smtp.gmail.com',   #发送邮件的邮箱 的 SMTP服务器
    "EMAIL_PORT" : 587,    #发件箱的SMTP服务器端口
    "EMAIL_HOST_USER" : 'williezh1113@gmail.com',   #发送邮件的邮箱地址
    "EMAIL_HOST_PASSWORD" : 'jaket521',       #发送邮件的邮箱密码
    "DEFAULT_FROM_EMAIL" : 'williezh1113@gmail.com',      #这项可要可不要
}


