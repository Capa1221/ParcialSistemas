from django.db import models

class Mensaje(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    imagen1 = models.ImageField(upload_to='imagenes', null=True, blank=True)
    
    def __str__(self):
        return f'{self.titulo} - {self.subtitulo}'

class Deporte(models.Model):
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    TituloD = models.CharField(max_length=200)
    Descripcion = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.TituloD} - {self.Descripcion}'

class Deportes2(models.Model):
    imagen1 = models.ImageField(upload_to='imagenes', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='imagenes', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='imagenes', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='imagenes', null=True, blank=True)
    TituloD2 = models.CharField(max_length=200)
    def __str__(self):
        return f'Deportes2: {self.TituloD2}'
    
class SubtituloE3(models.Model):
    subtituloE3 = models.CharField(max_length=200)
    def __str__(self):
        return f'SubtituloE3: {self.subtituloE3}'
    
class Contenido(models.Model):
    imagenE3 = models.ImageField(upload_to='imagenes', null=True, blank=True)
    tituloE3 = models.CharField(max_length=200)
    paisE3 = models.CharField(max_length=200)
    descripcionE3 = models.CharField(max_length=300)

    def __str__(self):
        return (
            f"Imagen E3: {self.imagenE3}\n"
            f"Titulo E3: {self.tituloE3}\n"
            f"Pais E3: {self.paisE3}\n"
            f"Descripcion E3: {self.descripcionE3}"
        )


    