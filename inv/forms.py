from django import forms

from .models import Categoria, SubCategoria, Marca, UM, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion':'Descripcion de la Categoria',
                    'estado':'Estado',}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
    #Le da al campo Descricion de un TextInput a un form-control


class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset = Categoria.objects.filter(estado=True).order_by('descripcion')
    )
    class Meta:
        model = SubCategoria
        fields = ['categoria','descripcion', 'estado']
        labels = {'categoria':'Sub Categoria',
                    'estado':'Estado',}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['categoria'].empty_label = "Seleccione Categoria"



class Marcaform(forms.ModelForm):
    class Meta():
        model = Marca
        fields = ['descripcion', 'estado']
        labels = {'descripcion':'Descripcion de la Marca',
        'estado':'Estado',}
        widget = {'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })


class UMform(forms.ModelForm):
    class Meta():
        model = UM
        fields = ['descripcion', 'estado']
        labels = {'descripcion':'Descripcion de la Unidad de Medida',
        'estado':'Estado',}
        widget = {'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })


class ProductoForm(forms.ModelForm):
    class Meta():
        model = Producto
        fields = ['codigo','codigo_barra','descripcion','estado',\
            'precio','existencia','ultima_compra',\
            'marca','subcategoria','unidad_medida']
        exclude = ['um','fm','uc','fc']
        widget = {'descripcion':forms.TextInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
            'class':'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True