from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Categoria, SubCategoria, Marca, UM
from .forms import CategoriaForm, SubCategoriaForm, Marcaform, UMform

#Vistas de Categoria
class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'inv/categorias_list.html'
    context_object_name = "obj"
    login_url = 'bases:login'


class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    #Sobre-escribimos el metodo form_valid para obtener al usuario que esta logeado

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    #Sobre-escribimos el metodo form_valid para obtener al usuario que esta logeado


class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')





#Vistas de Sub Categoria
class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name = 'inv/subcategorias_list.html'
    context_object_name = "obj"
    login_url = 'bases:login'

class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:subcategoria_list')



#Vistas de Marca
class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = Marcaform
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = Marcaform
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


#Vista basada en función
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()

    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not marca:
        return redirect('inv:marca_list')

    if request.method == 'GET':
        contexto = {'obj':marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        return redirect('inv:marca_list')
    
    return render(request, template_name, contexto)



#Vistas de Unidad de Medida
class UMView(LoginRequiredMixin, generic.ListView):
    model = UM
    template_name = 'inv/um_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class UMNew(LoginRequiredMixin, generic.CreateView):
    model = UM
    template_name = 'inv/um_form.html'
    context_object_name = 'obj'
    form_class = UMform
    success_url = reverse_lazy('inv:um_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class UMEdit(LoginRequiredMixin, generic.UpdateView):
    model = UM
    template_name = 'inv/um_form.html'
    context_object_name = 'obj'
    form_class = UMform
    success_url = reverse_lazy('inv:um_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


#Vista basada en función
def um_inactivar(request, id):
    um = UM.objects.filter(pk=id).first()

    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not um:
        return redirect('inv:um_list')

    if request.method == 'GET':
        contexto = {'obj':um}

    if request.method == 'POST':
        um.estado = False
        um.save()
        return redirect('inv:um_list')
    
    return render(request, template_name, contexto)