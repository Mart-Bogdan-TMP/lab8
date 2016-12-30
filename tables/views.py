from django.shortcuts import HttpResponse, render_to_response, HttpResponseRedirect
from django.template import loader, RequestContext
from django.views.generic import CreateView
from .models import Post


def index(request):
    template = loader.get_template('tables/tindex.html')
    return HttpResponse(template.render())


def to_homepage(request):
    template = loader.get_template('taxistation/homepage.html')
    return HttpResponse(template.render())


#TABLE POSTS

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

