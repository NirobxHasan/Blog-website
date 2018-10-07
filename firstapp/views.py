from django.shortcuts import render
from firstapp.models import Blog
from firstapp.forms import NewBlog
# Create your views here.
def index(request):
    blog_list = Blog.objects.order_by('date')
    blog_dict = {'blog': blog_list}
    return render(request,'firstapp/index.html',context=blog_dict)

def newblog(request):
    form =  NewBlog()
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR")
    return render(request,'firstapp/newblog.html', {'form':form})
