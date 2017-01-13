from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Models, Trim, ModelsShown, Accessories, Location, Colours, Interiors, Gallery, ColourGallery, Dealers, DealerCity, DealerProvince, ModelsShownInteriors, ModelsShownGallery, AllAccessories, AccessoriesShown, TestDrive


class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ('url', 'link', 'md5')

#    def get_model_perms(self, request):
#        return {}


class ModelsAdmin(admin.ModelAdmin):
    filter_horizontal = ('accessory', 'gallery')
    readonly_fields = ('image_thumb', 'image_thumb_logo')
    list_display = ('name_en', 'base_price', 'freight_DPI')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr'), 'internal_id', 'year', 'subhead_en', 'subhead_fr', ('disclaimer_en', 'disclaimer_fr')),
        }),
        (_('Image'), {
            'fields': (('url', 'link', 'image_thumb'),),
        }),
        (_('Logo'), {
            'fields': (('url_logo', 'link_logo', 'image_thumb_logo'),),
        }),
        (_('Prices'), {
            'fields': ('base_price', 'freight_DPI'),
        }),
        (_('Gallery'), {
            'fields': ('gallery',),
        }),
        (_('Special Offers & Promotions'), {
            'fields': ('lease_APR_from','lease_APR_for', 'lease_payment_from', 'down_payment')
        }),
        (_('Special accessories'), {
            'fields': ('accessory', 'price_override',)
        }),
    )


class ColourGalleryInline(admin.StackedInline):
    model = ColourGallery
    readonly_fields = ('image_thumb',)    




class TrimAdmin(admin.ModelAdmin):
    filter_horizontal = ('interiors', )
    list_display = ('name_en', 'model')
    readonly_fields = ('image_thumb',)
    inlines = [ ColourGalleryInline, ]
    fieldsets = (
        (_('General'), {
            'fields': ('model', ('name_en', 'name_fr'), 'internal_id'),
        }),
        (_('Details'), {
            'fields': (('url', 'link', 'image_thumb'), 'features_en', 'features_fr', 'price'),
        }),
#        (_('Colours'), {
#            'fields': ('colour', ('url_colour', 'link_colour', 'image_thumb')),
#        }),

        (_('Interiors'), {
            'fields': ('interiors',),
        }),

    )












class ModelsShownGalleryInline(admin.StackedInline):
    model =  ModelsShownGallery
    readonly_fields = ('image_thumb',)  




class ModelsShownAdmin(admin.ModelAdmin):
    filter_horizontal = ('interiors', 'all_accessories', 'accessories_shown')    
    list_display = ('vehicle', 'trim')
#    readonly_fields = ('image_thumb',)
    inlines = [ ModelsShownGalleryInline, ]    
    fieldsets = (
        (_('General'), {
            'fields': ('vehicle', 'trim', 'colour', ('legal_disclaimer_en', 'legal_disclaimer_fr'), ('standard_features_en', 'standard_features_fr'), 'price_override', 'starsafety', 'TSS', 'IIHS', 'series_code'),
        }),
        (_('Highlights'), {
            'fields': ('fuel_city', 'fuel_highway', 'fuel_combined', 'horsepower', 'engine_displacement', ('engine_description_en', 'engine_description_fr'), 'seats', 'airbags', 'torque', 'towing_capacity'),
        }),
        (_('Selected accessories'), {
            'fields': ('accessory', 'price_override_accessory',),
        }),
        (_('Locations'), {
            'fields': ('location',),
        }),
        (_('Models Shown Interiors'), {
            'fields': ('interiors',),
        }),
        (_('All Accessories'), {
            'fields': ('all_accessories',),
        }),
        (_('Accessories Shown'), {
            'fields': ('accessories_shown',),
        }),


    )









class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_fr', 'base_price')

    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',), 'base_price'),
        }),
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'language_default')
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'language_default'),
        }),
    )


class ColoursAdmin(admin.ModelAdmin):
    list_display = ('name', 'hexcode')
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'hexcode'),
        }),
    )


class InteriorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'link', 'get_trims')
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (_('General'), {
            'fields': ('name',)
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),
    )


'''
class InteriorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'hexcode')
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'hexcode')
        }),

    )   


class InteriorsAdmin(admin.ModelAdmin):
    fields = (('url', 'image_thumb'))
    readonly_fields = ('image_thumb',)
'''
'''
class DealersInline(admin.TabularInline):
    model = Dealers


class DealerProvinceAdmin(admin.ModelAdmin):
    inlines = [DealersInline,]
    list_display = ('province', 'provincial_code')
'''

class AllAccessoriesAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_fr', 'base_price')

    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',), 'base_price'),
        }),
    )

class AccessoriesShownAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_fr', 'base_price')

    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',), 'base_price'),
        }),
    )


class ModelsShownInteriorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'link', 'get_trims')
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (_('General'), {
            'fields': ('name',)
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),
    )




class DealersInline(admin.TabularInline):
    model = Dealers
    fieldsets = (
        (_('General'), {
            'fields': ('dealer_id', 'dealer_name', 'cityname')
        }),
    )

class DealerCityAdmin(admin.ModelAdmin):
    inlines = [DealersInline,]
    list_display = ('cityname', 'province')


class DealerProvinceAdmin(admin.ModelAdmin):
    list_display = ('province', 'provincial_code')


class TestDriveAdmin(admin.ModelAdmin):
    list_display = ('testdrive', 'status')
    fieldsets = (
        (_('Data'), {
            'fields': ('testdrive', 'status'),

        }),   

    )


admin.site.register(Models, ModelsAdmin)

admin.site.register(ModelsShown, ModelsShownAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Colours, ColoursAdmin)
admin.site.register(Interiors, InteriorsAdmin)
admin.site.register(Trim, TrimAdmin)
admin.site.register(Gallery, GalleryAdmin)
#admin.site.register(DealerProvince, DealerProvinceAdmin)
admin.site.register(AllAccessories, AllAccessoriesAdmin)
admin.site.register(AccessoriesShown, AccessoriesShownAdmin)
admin.site.register(ModelsShownInteriors, ModelsShownInteriorsAdmin)
admin.site.register(DealerCity, DealerCityAdmin)
#admin.site.register(DealerProvince, DealerProvinceAdmin)
admin.site.register(TestDrive, TestDriveAdmin)


