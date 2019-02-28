"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#boet6abg9n(z9p96943x+ezsk(lw1uod$l^7jir%m^!l%-n_9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite_db',
        'USER': 'jack',
        'PASSWORD': 'jack',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# 发送邮件设置
# https://docs.djangoproject.com/en/2.0/ref/settings/#email
# https://docs.djangoproject.com/en/2.0/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '1163383582@qq.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']  # 授权码
EMAIL_SUBJECT_PREFIX = '[jack的博客] '
EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)
