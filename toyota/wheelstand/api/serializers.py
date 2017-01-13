from rest_framework import serializers
from ..models import Models, Trim, ModelsShown, Accessories, Location, Colours, Interiors, Gallery, ColourGallery, Dealers, DealerProvince, ModelsShownInteriors, ModelsShownGallery, AllAccessories, AccessoriesShown, DealerCity, TestDrive


class ModelsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Models
        fields = ('id', 'name', 'internal_id', 'year', 'subhead', 'url_logo', 'link_logo', 'url', 'link', 'disclaimer', 'base_price', 'freight_DPI', 'gallery', 'lease_APR_from', 'lease_APR_for', 'lease_payment_from', 'down_payment', 'accessory', 'price_override', )
        extra_kwargs = {
                'url': {
                    'required': False,
#                    'allow_blank': True,
                 }
            }        


class ModelsImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Models
        fields = ('url', 'path', 'md5')
        extra_kwargs = {
                'url': {
                    'required': False,
#                    'allow_blank': True,
                 }
            }      

    def get_url_url(self, obj):
        if obj.url == '':
            pass
        else:
            return obj.url.url

#    def get_url_url(self, obj):
#        return obj.url.url



class ColoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colours
        fields = '__all__'


class InteriorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interiors
        fields = ('id', 'name', 'url')


class InteriorsImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Interiors
        fields = ('url', 'path', 'md5')
        extra_kwargs = {
                'url': {
                    'required': False,
#                    'allow_blank': True,
                 }
            }        

    def get_url_url(self, obj):
        if obj.url == '':
            pass
        else:
            return obj.url.url

#    def get_url_url(self, obj):
#        return obj.url.url


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = ('id', 'name', 'base_price')



class ColourGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ColourGallery
        fields = '__all__'


class ColourGalleryImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = ColourGallery
        fields = ('url', 'path', 'md5')
        extra_kwargs = {
                'url': {
                    'required': False,
#                    'allow_blank': True,
                 }
            }        

    def get_url_url(self, obj):
        if obj.url == '':
            pass
        else:
            return obj.url.url

#    def get_url_url(self, obj):
#        return obj.url.url


class TrimSerializer(serializers.ModelSerializer):
    interiors = InteriorsSerializer(read_only=True, many=True)
    trim_gallery = ColourGallerySerializer(read_only=True, many=True)

    class Meta:
        model = Trim
        fields = ('id', 'model', 'name', 'internal_id', 'url', 'link', 'features', 'price', 'interiors', 'trim_gallery' )
#        depth = 1
        extra_kwargs = {
                'url': {
                    'required': False,
#                    'allow_blank': True,
                 }
            }



class TrimImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Trim
        fields = ('url', 'path', 'md5')
        extra_kwargs = {
                'url': {
                    'required': False,
#                    'allow_blank': True,
                 }
            }        

    def get_url_url(self, obj):
        if obj.url == '':
            pass
        else:
            return obj.url.url

#    def get_url_url(self, obj):
#        return obj.url.url


class  ModelsShownInteriorsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ModelsShownInteriors
        fields = ('id', 'name', 'url')


class AllAccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllAccessories
        fields = ('id', 'name', 'base_price')


class AccessoriesShownSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesShown
        fields = ('id', 'name', 'base_price')


class ModelsShownGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelsShownGallery
        fields = '__all__'


class ModelsShownSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True, many=True)
    vehicle = ModelsSerializer(read_only=True)
    trim = TrimSerializer(read_only=True)
    accessory = AccessoriesSerializer(read_only=True)
    interiors = ModelsShownInteriorsSerializer(read_only=True, many=True)
    all_accessories = AllAccessoriesSerializer(read_only=True, many=True)
    accessories_shown = AccessoriesShownSerializer(read_only=True, many=True)
    models_shown_gallery = ModelsShownGallerySerializer(read_only=True, many=True)
    depth = 2

    class Meta:
        model = ModelsShown
        fields = ('id', 'vehicle', 'trim', 'colour', 'legal_disclaimer', 'standard_features', 'price_override', 'starsafety', 'TSS', 'IIHS', 'series_code', 'fuel_city', 'fuel_highway', 'fuel_combined', 'horsepower', 'engine_displacement', 'engine_description', 'seats', 'airbags', 'torque', 'towing_capacity', 'accessory', 'price_override_accessory', 'location', 'models_shown_gallery', 'interiors', 'all_accessories',  'accessories_shown')

class GallerySerializer(serializers.ModelSerializer):
    vehicle = ModelsSerializer(read_only=True)

    class Meta:
        model = Gallery
        fields = '__all__'


class GalleryImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Gallery
        fields = ('url', 'path', 'md5')
        extra_kwargs = {
                'url': {
                    'required': False,
#                    'allow_blank': True,
                 }
            }        

    def get_url_url(self, obj):
        if obj.url == '':
            pass
        else:
            return obj.url.url

#    def get_url_url(self, obj):
#        return obj.url.url


class ModelsShownGalleryImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = ModelsShownGallery
        fields = ('url', 'path', 'md5')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }        

    def get_url_url(self, obj):
        if obj.url == '':
            pass
        else:
            return obj.url.url

#    def get_url_url(self, obj):
#        return obj.url.url








class DealerCitySerializer(serializers.ModelSerializer):
#    dealers = DealersSerializer(read_only=True)    
#    province = DealerProvinceSerializer(read_only=True)   

    class Meta:
        model = DealerCity
        fields = '__all__'
        depth = 3

class DealersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dealers
        fields = ('id', 'dealer_id', 'dealer_name', 'cityname',)
        depth = 3

'''
class DealerProvinceSerializer(serializers.ModelSerializer):
    dealers = DealersSerializer(read_only=True, many=True) 
    cityname = DealerCitySerializer(read_only=True)

    class Meta:
        model = DealerProvince
        fields = ('id', 'province', 'provincial_code', 'dealers', 'cityname')
        depth = 3
'''





class DealersNSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dealers
        fields = ('id', 'dealer_id', 'dealer_name')
#        depth = 1

class DealerCityNSerializer(serializers.ModelSerializer):
    dealers = DealersNSerializer(many=True)   
#    province = DealerProvinceSerializer(read_only=True)   

    class Meta:
        model = DealerCity
        fields = ('id', 'cityname', 'dealers')
#        depth = 1



class DealerProvinceSerializer(serializers.ModelSerializer):
#    dealers = DealersSerializer(read_only=True, many=True) 
#    cityname = DealerCitySerializer(many=True)
    dealercity = DealerCityNSerializer(many=True)

    class Meta:
        model = DealerProvince
        fields = ('id', 'province', 'provincial_code', 'dealercity')
#        depth = 1


class TestDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDrive
        fields = '__all__'