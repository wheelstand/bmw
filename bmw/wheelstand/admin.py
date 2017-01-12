from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Models, Trim, ModelsShown, FeaturesAccessory, Exterior, Upholstery, Wheel, Package, Option, Location, TrimEnImage, TrimFrImage, Gallery, Interior, Performance, Colour, TestDrive, KeepingInTouch
from django.forms import TextInput, Textarea
from django.db import models



#class GalleryInline(admin.TabularInline):
#    model = Gallery
#    extra = 3
#    list_display = ('name_en', 'base_price', 'freight_DPI')
#    verbose_name = "Image"
#    verbose_name_plural = "Gallery"
#    readonly_fields = ('image_thumb',)


class GalleryAdmin(admin.ModelAdmin):

    model = Gallery
    list_display = ('name', 'url', 'image_thumb')

#    def get_model_perms(self, request):
#        return {}



class ModelsAdmin(admin.ModelAdmin):

    list_display = ('name_en', 'year', 'base_price', 'freight_DPI')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr'), 'year'),
        }),
        (_('Prices'), {
            'fields': ('base_price', 'freight_DPI'),
        }),
    )


class TrimEnImageAdmin(admin.ModelAdmin):
    list_display = ('url', 'link')
    fieldsets = (
        (_('Image'), {
            'fields': ('url', 'link'),
        }),         
    )
    def get_model_perms(self, request):
        return {}

class TrimFrImageAdmin(admin.ModelAdmin):
    list_display = ('url', 'link')
    fieldsets = (
        (_('Image'), {
            'fields': ('url', 'link'),
        }),         
    )
    def get_model_perms(self, request):
        return {}


class TrimAdmin(admin.ModelAdmin):
  
    list_display = ('name_en', 'model')
    filter_horizontal = ('features_accessories', 'upholsteries', 'wheels', 'gallery', 'packages', 'colours')
    fieldsets = (
        (_('General'), {
            'fields': ('model', ('name_en', 'name_fr'),),
        }),
#        (_('Logo'), {
#            'fields': ('logo', 'urllogo', 'link'),
#        }),        
        (_('Performance'), {
            'fields': ('power', 'torque', 'acceleration', 'car_range', 'range_value'),
        }),

        (_('Consumption'), {
            'fields': ('top_speed', 'city', 'hwy', 'combined'),
        }),

        (_('Features & Accessories'), {
            'fields': ('features_accessories',),
        }),
        (_('Colours'), {
            'fields': ('colours',),
        }),
        (_('Upholstery'), {
            'fields': ('upholsteries',),
        }),
        (_('Wheels'), {
            'fields': ('wheels',),
        }),
        (_('Packages'), {
            'fields': ('packages',),
        }),
        (_('Options'), {
            'fields': (('interior_en', 'interior_fr'), ('performance_en', 'performance_fr'), ('exterior_en', 'exterior_fr'))
        }),
       
        (_('Image'), {
            'fields': ('gallery',),
        }),        
    )


class ModelsShownAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'price_override')
    readonly_fields = ('image_thumb',)      
    fieldsets = (
        (_('General'), {
            'fields': ('vehicle',),
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),
        (('Prices'), {
            'fields': ('price_override', ('disclaimer_override_en', 'disclaimer_override_fr'),),
        }),
        (('Locations'), {
            'fields': ('location',),
        }),
    )


class FeaturesAccessoryAdmin(admin.ModelAdmin):
    readonly_fields = ('image_thumb',)    
    list_display = ('name_en', 'image_thumb', 'trims')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',), ('description_en', 'description_fr',)),
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),         
    )


class ExteriorAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'trims')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',),),
        }),
    )


class UpholsteryAdmin(admin.ModelAdmin):
    readonly_fields = ('image_thumb',)    
    list_display = ('name_en', 'trims')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',)),
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),        
    )


class WheelAdmin(admin.ModelAdmin):
    readonly_fields = ('image_thumb',)    
    list_display = ('name_en', 'trims')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',)),
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),        
    )


class PackageAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'price_override')
    readonly_fields = ('image_thumb', 'trims')    
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',), ('description_en', 'description_fr',), 'price_override'),
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),          

    )


class OptionAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'description_en', 'trims')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',), ('description_en', 'description_fr')),
        }),
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'language'),
        }),
    )


class InteriorAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'trims')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',),),
        }),
    )


class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'trims')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',),),
        }),
    )


class ColourAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'hexcode', 'trims')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',), 'hexcode'),
        }),
    )  


class TestDriveAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_method', 'email', 'phone', 'status')
    fieldsets = (
        (_('Customer'), {
            'fields': ('salutation', 'first_name', 'last_name', 'contact_method', 'email', 'phone'),

        }),   
        (_('Dealer'), {
            'fields': ('purchase_intent', 'brochure', 'retailer_number', 'retailer_location', 'language', 'consent', 'consentB', 'vehicle', 'status'),
        }),

    ) 


class KeepingInTouchAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'phone', 'purchaseIntent', 'consent', 'status')
    fieldsets = (
        (_('Customer'), {
            'fields': ('firstName', 'lastName', 'phone', 'email', 'purchaseIntent', 'language', 'consent', 'consentB', 'status'),
        }),   
    )   


admin.site.register(Models, ModelsAdmin)
admin.site.register(TrimEnImage, TrimEnImageAdmin)
admin.site.register(TrimFrImage, TrimFrImageAdmin)
admin.site.register(Trim, TrimAdmin)
admin.site.register(ModelsShown, ModelsShownAdmin)
admin.site.register(FeaturesAccessory, FeaturesAccessoryAdmin)
#admin.site.register(Exterior, ExteriorAdmin)
admin.site.register(Upholstery, UpholsteryAdmin)
admin.site.register(Wheel, WheelAdmin)
admin.site.register(Package, PackageAdmin)
#admin.site.register(Option, OptionAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Gallery, GalleryAdmin)
#admin.site.register(Interior, InteriorAdmin)
#admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(TestDrive, TestDriveAdmin)
admin.site.register(KeepingInTouch, KeepingInTouchAdmin)
