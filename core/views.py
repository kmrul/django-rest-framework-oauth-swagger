from core.serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.schemas import AutoSchema
from core.models import Todo
import coreapi
        

class ListTodoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todos =Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)




class TodoDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        todos = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todos, many=False)
        return Response(serializer.data)




class CreateTodoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




class UpdateTodoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)




class DeleteTodoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        todo_instance = Todo.objects.get(id=pk)
        todo_instance.delete()
        return Response('Deleted')
