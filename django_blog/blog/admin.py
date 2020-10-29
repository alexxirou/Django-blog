from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass


# Add in this class to customized the Admin Interface
#class CategoryAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug':('name',)}



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)





