from rest_framework import serializers
from ..models import Models, Trim, ModelsShown, FeaturesAccessory, Exterior, \
    Upholstery, Wheel, Package, Option, Location, TrimEnImage, TrimFrImage, Gallery, Interior, Performance, Colour, Information, TestDrive, KeepingInTouch
from django.contrib.auth.models import User, Group


class ModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models
        fields = ('name', 'year', 'base_price', 'freight_DPI')


class FeaturesAccessorySerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = FeaturesAccessory
        fields = ('id', 'name', 'description', 'url', 'path')
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


class FeaturesAccessoryImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = FeaturesAccessory
        fields = ('url', 'path', 'md5')
#        depth = 1
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


class ExteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exterior
        fields = ('id', 'name')


class InteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = ('id', 'name')


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exterior
        fields = ('id', 'name')


class ColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exterior
        fields = ('id', 'name', 'hexcode')

'''
class UpholsterySerializer(serializers.ModelSerializer):
#    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Upholstery
        fields = ('id', 'name')
#        extra_kwargs = {
#                'url': {
#                    'required': False,
#                 }
#            }

#    def get_url_url(self, obj):
#        return obj.url.url
'''

class UpholsterySerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Upholstery
        fields = ('id', 'name', 'url', 'path')
        read_only_fields = ('path', )        
        extra_kwargs = {
                'url': {'required': False},
#                'path': {'required': False}
            }

    def get_url_url(self, obj):
        if obj.url == '':
            pass
        else:
            return obj.url.url

#    def get_url_url(self, obj):
#        return obj.url.url



'''
class UpholsteryImageSerializer(serializers.ModelSerializer):
#    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Upholstery
        fields = ('md5',)
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }

#    def get_url_url(self, obj):
#        return obj.url.url



'''
class UpholsteryImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Upholstery
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

















class WheelSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Wheel
        fields = ('id', 'name', 'url', 'path')
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


class WheelImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Wheel
        fields = ('url', 'path', 'md5',)
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


class PackageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Package
        fields = ('id', 'name', 'description', 'price_override', 'url', 'path')
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


class PackageImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Package
        fields = ('url', 'path', 'md5',)
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


#class OptionSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Option
#        fields = ('id', 'name', 'description')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'language')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }


class TrimEnImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = TrimEnImage
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


class TrimFrImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = TrimFrImage
        fields = '__all__'

    def get_url_url(self, obj):
        if obj.url == '':
            pass
        else:
            return obj.url.url

#    def get_url_url(self, obj):
#        return obj.url.url


class GallerySerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Gallery
        fields = ('id', 'name', 'url', 'path', 'link')
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
        
#class GalleryTrimSerializer(serializers.ModelSerializer):
#    vehicle = ModelsSerializer(read_only=True)

#    class Meta:
#        model = Trim
#        fields = ('gallery',) 


class GalleryImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = Gallery
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

        
class TrimSerializer(serializers.ModelSerializer):
    features_accessories = FeaturesAccessorySerializer(read_only=True, many=True)
    colours = ColourSerializer(read_only=True, many=True)
    upholsteries = UpholsterySerializer(read_only=True, many=True)
    wheels = WheelSerializer(read_only=True, many=True)
    packages = PackageSerializer(read_only=True, many=True) 
#    options = OptionSerializer(read_only=True, many=True)
    model = ModelsSerializer(read_only=True)
    gallery = GallerySerializer(read_only=True, many=True)
    path = serializers.SerializerMethodField('get_url_url')


    class Meta:
        model = Trim
        fields = ('id', 'logo', 'urllogo', 'path', 'link', 'model', 'name', 'power', 'torque', 'top_speed', 'city', 'hwy', 'combined', 'acceleration', 'car_range', 'range_value', 'features_accessories', 'interior', 'exterior', 'performance', 'upholsteries', 'wheels', 'packages', 'colours', 'gallery')
        extra_kwargs = {
                'urllogo': {
                    'required': False,
                 }
            }        

    def get_url_url(self, obj):
        if obj.urllogo.name == '':
            return ''
        else:
            return obj.urllogo.url       


class TrimImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')
    urllogo = serializers.SerializerMethodField()
    

    class Meta:
        model = Trim
        fields = ('urllogo','path', 'md5')
        extra_kwargs = {
                'urllogo': {
                    'required': False,
                 }
            }
   
    def get_url_url(self, obj):
        if obj.urllogo.name == '':
            return ''
        else:
            return obj.urllogo.url 

    def get_urllogo(self, obj):
        if obj.urllogo == '':
            return ''
        else:
            return obj.urllogo            
            
        
class ModelsShownImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')


    class Meta:
        model = ModelsShown
        fields = ('url', 'path', 'md5',)
        extra_kwargs = {
                'url': {
                    'required': False,
                 }
            }
            
    def get_url_url(self, obj):
        if obj.urllogo.name == '':
            return ''
        else:
            return obj.urllogo.url   





class TrimEnSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')
    
    class Meta:
        model = TrimEnImage
        fields = ('url','path')

    def get_url_url(self, obj):
        if obj.url == '':
            pass
        else:
            return obj.url.url

#    def get_url_url(self, obj):
#        return obj.url.url


class TrimFrSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = TrimFrImage
        fields = ('url', 'path')
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


class ModelsShownSerializer(serializers.ModelSerializer):
    vehicle = TrimSerializer(read_only=True)
    path = serializers.SerializerMethodField('get_url_url')
    location = LocationSerializer(read_only=True, many=True)

    class Meta:
        model = ModelsShown
        fields = ('vehicle', 'url', 'path', 'price_override',
                  'disclaimer',  'location', )
#        depth = 1
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


class ModelsShownImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = ModelsShown
        fields = ('url', 'path', 'md5',)
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


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ('id', 'first_name', 'last_name', 'email')


class TestDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDrive
        fields = '__all__'


class KeepingInTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeepingInTouch
        fields = '__all__'        
