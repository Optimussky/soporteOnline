from django.db import models

# Create your models here.

class Areas(models.Model):
    nombre = models.CharField(verbose_name='Nombre',max_length=200,help_text="Agrege nueva área")
    created_at = models.DateTimeField(verbose_name='Creado',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado',auto_now=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Areas"
    
    def __str__(self):
        return self.nombre


class Agenda(models.Model):
    area = models.ForeignKey(Areas,on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name='Nombre',max_length=200,help_text="Agrege nueva área")
    telefono = models.CharField(verbose_name='Teléfono',max_length=150)
    created_at = models.DateTimeField(verbose_name='Creado',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado',auto_now=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Agenda"

    def __str__(self):
        return self.area.nombre


class Subcategoria(models.Model):
    nombre = models.CharField(verbose_name='Subcategoria',max_length=150)
    created_at = models.DateTimeField(verbose_name="Creado",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Actualizado", auto_now=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural: "Subcategorias"

    def __str__(self):
        return self.nombre

class Asunto(models.Model):
    categoria = models.CharField(verbose_name='Categoría', max_length=200)
    subcategoria = models.ForeignKey(Subcategoria,verbose_name="Subcategoria", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Creado",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Actualizado", auto_now=True)

    class Meta:
        ordering = ["categoria"]
        verbose_name_plural = "Asuntos"

    def __str__(self):
        return self.categoria
    

class Registro(models.Model):
    area = models.ForeignKey(Areas,verbose_name='Área', on_delete=models.CASCADE)
    asunto = models.ForeignKey(Asunto, on_delete=models.CASCADE)
    registro = models.CharField(max_length=250,verbose_name="Registro",help_text="Descripción del registro")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Registros"


    def __str__(self):
        return self.registro