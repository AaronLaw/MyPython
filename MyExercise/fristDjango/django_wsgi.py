#!/usr/bin/env python
#coding:utf-8

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE","fristDjango.settings")

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHander()