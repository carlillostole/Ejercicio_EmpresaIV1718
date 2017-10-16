from django.shortcuts import render
from .forms import PostForm
from .models import Post


def post_list(request):
    return render(request, 'empresa/post_list.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'empresa/post_edit.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'empresa/post_edit.html', {'form': form})


def clasificacion(request):
    latest_question_list = Post.objects.order_by('-puntuacion')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'empresa/clasificacion.html', context)

def eliminar(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre_empresa']
            c = Post.object.get(nombre_empresa = nombre)
            c.delete()
            return render(request, 'empresa/eliminar.html')
        else:
            form = PostForm()
    return render(request, 'empresa/eliminar.html')
