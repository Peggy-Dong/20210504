from django.contrib import admin
from mysite.models import Post, 食譜, 食材

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'pub_date')
admin.site.register(Post, PostAdmin)


admin.site.register(食材)

class 食譜Admin(admin.ModelAdmin):
	list_display = ('name', '食材', 'g')

admin.site.register(食譜, 食譜Admin)