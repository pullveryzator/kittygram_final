from django.contrib import admin

from .models import Achievement, Cat


class CatAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'birth_year',
        'color',
        'owner',
    )
    list_per_page = 15
    search_fields = (
        'name',
        'owner',
    )
    list_display_links = ('name',)


class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    list_per_page = 15
    search_fields = (
        'name',
    )
    list_display_links = (
        'name',
    )


admin.site.empty_value_display = 'Не задано'
admin.site.site_header = 'Управление проектом "Kittygram"'
admin.site.site_title = 'Kittygram'
admin.site.register(Cat, CatAdmin)
admin.site.register(Achievement, AchievementAdmin)
