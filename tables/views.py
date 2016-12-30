from django.shortcuts import HttpResponse, render_to_response
from django.template import loader, RequestContext
from django.views.generic import CreateView
from .models import Post, Worker


def index(request):
    template = loader.get_template('tables/tindex.html')
    return HttpResponse(template.render())


def to_homepage(request):
    template = loader.get_template('taxistation/homepage.html')
    return HttpResponse(template.render())


#=================================================================================
#TABLE POSTS
#=================================================================================
def details_posts(request):
    all_posts = Post.objects.all()
    post_data = {'post_detail': all_posts}
    print(post_data)
    return render_to_response('tables/posts.html', post_data, RequestContext(request))


class PostCreate(CreateView):
    model = Post
    fields = ['post_name', 'salary', 'duties', 'requirements']


def post_delete(request, pk):
    query = Post.objects.get(pk=pk)
    query.delete()
    all_posts = Post.objects.all()
    post_data = {'post_detail': all_posts}
    print(post_data)
    return render_to_response('tables/posts.html', post_data,  RequestContext(request))


#=================================================================================
#TABLE WORKERS
#=================================================================================
def details_workers(request):
    all_workers = Worker.objects.all()
    worker_data = {'worker_detail': all_workers}
    print(worker_data)
    return render_to_response('tables/workers.html', worker_data, RequestContext(request))


class WorkerCreate(CreateView):
    model = Worker
    fields = ['full_name', 'age', 'gender', 'address', 'phone', 'passport', 'post_id']


def worker_delete(request, pk):
    query = Worker.objects.get(pk=pk)
    query.delete()
    all_workers = Worker.objects.all()
    worker_data = {'worker_detail': all_workers}
    print(worker_data)
    return render_to_response('tables/workers.html', worker_data,  RequestContext(request))









#=================================================================================
#DEPARTMENTS
#=================================================================================
def departments(request):
    template = loader.get_template('tables/departments.html')
    return HttpResponse(template.render())