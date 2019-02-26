# -*- coding:utf-8 -*-
from django.http import HttpResponse
from TestModel.models import Test

def testdb_delete(request):
    test1 = Test.objects.get(id=1)
    test1.delete()

    return HttpResponse('<p>删除成功</p>')