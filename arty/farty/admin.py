from django.contrib import admin
from .models import heroname, hero_rank, association

class HeroRankInline(admin.TabularInline):
    model = hero_rank
    extra = 1

class HeroNameAdmin(admin.ModelAdmin):
    inlines = [HeroRankInline]
    list_display = ('name', 'herotype', 'age')
    search_fields = ('name', 'herotype')

class AssociationAdmin(admin.ModelAdmin):
    filter_horizontal = ('members',)
    
admin.site.register(heroname, HeroNameAdmin)
admin.site.register(hero_rank)
admin.site.register(association, AssociationAdmin)
# Register your models here.
