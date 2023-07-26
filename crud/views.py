from django.shortcuts import render,redirect
from .models import Blog,Contacts # manager objects
from .forms import BlogForm



# Create your views here.
def index(request):
    blog = Blog.objects.all()
    return render(request,"crud/home.html",{"blogs":blog})


def about(request):
    return render(request,"crud/about.html")

def create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return  redirect("home")
    return render(request,"crud/createblog.html",{"form":form})

def deleteBlog(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("home")

def updateBlog(request,id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST or None,instance=blog)
    if (form.is_valid()):
        form.save()
        return redirect("home")
    return render(request,"crud/create.html",{"form":form})
    

def partData(request,id):
    blog = Blog.objects.get(id=id)
    print(blog)
    context = {
        "blog":blog
    }
    return render(request,"crud/index.html",context)

def contacts(request):
    if(request.method == "POST"):
        dataName = request.POST.get("name")
        dataEmail = request.POST.get("email")

        contacts = Contacts(
            name=dataName,
            email=dataEmail
        )

        contacts.save()
        return redirect("home")
      
           

    return render(request,"crud/contact.html")
