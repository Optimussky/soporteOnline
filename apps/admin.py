from django.contrib import admin
from apps.models import Agenda,Areas,Subcategoria,Asunto,Registro
# Register your models here.


class AgendaAdmin(admin.ModelAdmin):
    list_display = ['id','area','nombre','telefono', 'created_at', 'updated_at']
    search_fields =  ('nombre',)
    ordering = ['nombre']
    list_display_links = ('nombre',)

admin.site.register(Agenda,AgendaAdmin)


class AreasAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'created_at', 'updated_at']
    search_fields =  ('nombre',)
    ordering = ['nombre']
    list_display_links = ('nombre',)
    #actions = [make_published]

admin.site.register(Areas,AreasAdmin)

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','created_at', 'updated_at' ]
    search_fields =  ('nombre',)
    ordering = ['nombre']
    list_display_links = ('nombre',)

admin.site.register(Subcategoria,SubcategoriaAdmin)


class AsuntoAdmin(admin.ModelAdmin):
    list_display = ['id','categoria','subcategoria','created_at', 'updated_at' ]
    search_fields =  ('categoria',)
    ordering = ['categoria']
    list_display_links = ('categoria',)

admin.site.register(Asunto,AsuntoAdmin)


class RegistroAdmin(admin.ModelAdmin):
    #resource_class = RegistroResources
    date_hierarchy = ('created_at')
    readonly_fields = ('created_at','updated_at')
    list_display = ('id','area','asunto','registro', 'created_at','updated_at')
    list_editable = ['registro']
    search_fields =  ('area__nombre','asunto__categoria','registro')
    #list_filter = ('registro','created_at','asunto',)
    list_filter = ('created_at','asunto__categoria')
    list_display_links = ('area',)
    list_per_page = 10

admin.site.register(Registro,RegistroAdmin)


