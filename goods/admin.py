from django.contrib import admin

from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "image"]

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount", "brand", "model", "technology", "resolution", 
                    "print_speed", "resurs", "trays", "connection", "dopf",
                    "dlay", "typef", "color", "form", "pocr", "plotn", "collist"]
    list_editable = ["discount",]
    search_fields = ["name", "description", "brand", "technology", "resolution", "print_speed", "trays", "connection"]
    list_filter = ["discount", "quantity", "category"]
    fields = [
        "name", "category", "slug", "description",
        "brand", "model", "technology", "resolution", "print_speed", 
        "trays", "connection", "dopf",  "resurs", 
        "dlay", "typef", "color", "form", "pocr", "plotn", "collist",
        "image", ("price", "discount"), "quantity",
    ]



