# -*- coding:utf-8 -*-
from django.http import HttpResponse
from TestModel.models import Test

def testdb_update(request):
    test1 = Test.objects.get(id=1)
    test1.name = "Google"
    test1.save()

    return HttpResponse('<p>修改成功</p>')