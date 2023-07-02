from django.contrib import admin

from pages.models import GlobalIncrementTracker, Page

class PageAdmin(admin.ModelAdmin):
    # also add where the model is registered in db
    list_display = ('title', 'url', 'shard')

    def shard(self, obj):
        return obj._state.db
    
admin.site.register(Page, PageAdmin)

admin.site.register(GlobalIncrementTracker)