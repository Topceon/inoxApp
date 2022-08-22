from django.contrib import admin

from store.models import Storage


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    fields = [
        'name',
    ]