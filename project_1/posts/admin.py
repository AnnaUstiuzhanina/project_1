from django.contrib import admin

from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "text", "published", "date", "created", "changed", "group")
    search_fields = ("name", "text", "group",)
    list_filter = ("date", "created", "changed",)
    empty_value_display = "-пусто-"
    autocomplete_fields = ['group']


class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created", "changed",)
    search_fields = ("name", "description",)
    list_filter = ("created", "changed",)
    empty_value_display = "-пусто-"
    search_fields = ['name', 'description']


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
