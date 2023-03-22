from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Note

@api_view(['GET'])
def getData(request):
    if request.method == 'GET': 
        data = request.GET['test']
        note = Note.objects.filter(id=5).values()
        data1 = note[0]['title']
        print(data1)
    text = "hello rest api"
    return Response(text)