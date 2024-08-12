from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Blog
from .serializers import BlogSerializer

@api_view(["GET"])
def get_all_blogs(request):

    get_all_blogs = Blog.objects.all()
    serializer = BlogSerializer(get_all_blogs, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_single_blog(request, id):
    try:
        get_single_blog = Blog.objects.get(id=id)
        serializer = BlogSerializer(get_single_blog)
        return Response(serializer.data)
    except Blog.DoesNotExist:
        return Response(status=404)
    
@api_view(["POST"])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["PUT"])
def update_blog(request, id):
    try:
        update_blog = Blog.objects.get(id=id)
        serializer = BlogSerializer(update_blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Blog.DoesNotExist:
        return Response(status=404)
    
@api_view(["DELETE"])
def delete_blog(request, id):
    try:
        delete_blog = Blog.objects.get(id=id)
        delete_blog.delete()
        return Response(status=204)
    except Blog.DoesNotExist:
        return Response(status=404)