##coding=utf-8
import uuid

from django.shortcuts import render

# Create your views here.
from models import UserMessage


def getFrom(request):
    ret = None
    if request.method == 'POST':
        reqs = request.POST
        print(reqs)
        oid = uuid.uuid4()
        name = reqs.get('name')
        email = reqs.get('email')
        message = reqs.get('message')
        address = reqs.get('address')
        #保存前台传来的请求数据
        UserMessage.objects.create(
            object_id=oid,
            name=name,
            email=email,
            message=message,
            address=address
        ).save()
        #从数据库中查询保存的数据
        umObj = UserMessage.objects.get(object_id=oid)
        print(umObj.name)
        print('*'*88)
        #使用过滤查询
        umObj1 = UserMessage.objects.filter(name=name, object_id=oid)#相当于and
        print(umObj1[0].name)
        print('*'*88)

        #将数据返回到前台
        ret = {
        'umObj1': umObj1[0],
        }
        print(ret)

    return render(request, 'form.html', ret)