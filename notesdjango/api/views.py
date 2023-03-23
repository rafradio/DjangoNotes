from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Note
from django.core import serializers
import json 
from datetime import date, datetime
from django.core.serializers.json import DjangoJSONEncoder

@api_view(['GET'])
def getData(request):
    dict = {}
    if request.method == 'GET': 
        data = request.GET['id']
        # note = Note.objects.get(id=data)
        note = Note.objects.filter(id=data).values()
        # dataJson = serializers.serialize("json", Note.objects.all().filter(id=data), cls=LazyEncoder)
        # data1 = note[0]['date']
        
        for key in note[0].keys():
            dict[key] = note[0][key]
        print(dict)
        # dataJson = serializers.serialize("json", dict, cls=LazyEncoder)
        # print(dataJson.keys())
        # data2 = json.dumps(dict, indent=4, sort_keys=True, default=json_serial) 
    text = "hello rest api"
    return Response(dict)



def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)