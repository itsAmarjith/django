from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import TodoModel
from .serializers import TodoSerializer
from rest_framework.response import Response
# Create your views here.


#  GET all and POST


@api_view(['GET','POST'])

def Todo_list(request):
    if request.method=='GET':

        todo=TodoModel.objects.all()
        serializer=TodoSerializer(todo,many=True)
        return Response(serializer.data)

    if request.method=='POST':
        todo=request.data
        serializer=TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'todocreate'})


        return Response(serializer.errors)

# GET one, PUT, DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id):

    try:
        todo = TodoModel.objects.get(id=id)
    except TodoModel.DoesNotExist:
        return Response({'message': 'Todo not found'})

    # GET one todo
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    # PUT - update todo
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    # DELETE - delete todo
    if request.method == 'DELETE':
        todo.delete()
        return Response({'message': 'Todo deleted'})   






