from rest_framework import serializers
from ..models import Models, Trim, ModelsShown, FeaturesAccessory, Exterior, \
	Upholstery, Wheel, Package, Option, Location, TrimEnImage, TrimFrImage, Gallery, Interior, Performance, Colour, \
	Information, TestDrive, KeepingInTouch, StaticModelEN, StaticModelFR, StaticModel, StandAloneOption, \
	OptionalEquipment
from django.contrib.auth.models import User, Group


class ModelsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Models
		fields = ('id', 'name', 'year', 'base_price', 'colour',
		          'exterior', 'interior', 'trim_price', 'optional_equipement', 'wheels', 'freight_DPI', 'taxes',
		          'isBMWi')


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


# def get_url_url(self, obj):
#        return obj.url.url


class FeaturesAccessoryImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = FeaturesAccessory
		fields = ('url', 'path', 'filesize')
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

	def get_alternate_md5(self, obj):
		return str(obj.url.size)


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
		read_only_fields = ('path',)
		extra_kwargs = {
			'url': {'required': False},
			#                'path': {'required': False}
		}

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url


# def get_url_url(self, obj):
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
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = Upholstery
		fields = ('url', 'path', 'filesize')
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

	def get_alternate_md5(self, obj):
		if obj.url == '':
			pass
		else:
			return str(obj.url.size)


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


# def get_url_url(self, obj):
#        return obj.url.url


class WheelImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = Wheel
		fields = ('url', 'path', 'filesize',)
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

	def get_alternate_md5(self, obj):
		if obj.url == '':
			pass
		else:
			return str(obj.url.size)


class PackageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	package_model = ModelsSerializer(read_only=True, many=True)

	class Meta:
		model = Package
		fields = ('id', 'name', 'description', 'price_override', 'url', 'path', 'code', 'field_type', 'package_model')
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


# def get_url_url(self, obj):
#        return obj.url.url


class PackageImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = Package
		fields = ('url', 'path', 'filesize',)
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

	def get_alternate_md5(self, obj):
		if obj.url == '':
			return ''
		else:
			return str(obj.url.size)


# class OptionSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Option
#        fields = ('id', 'name', 'description')


class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ('id', 'name', 'language', 'disclaimer')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'url', 'username', 'email', 'groups')
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'url', 'name')
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}


class TrimEnImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = TrimEnImage
		fields = ('url', 'path', 'filesize')
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

	def get_alternate_md5(self, obj):
		if obj.url == '':
			return ''
		else:
			return str(obj.url.size)


class TrimFrImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = TrimFrImage
		fields = '__all__'

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url

	def get_alternate_md5(self, obj):
		if obj.url == '':
			pass
		else:
			return str(obj.url.size)


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


# def get_url_url(self, obj):
#        return obj.url.url

# class GalleryTrimSerializer(serializers.ModelSerializer):
#    vehicle = ModelsSerializer(read_only=True)

#    class Meta:
#        model = Trim
#        fields = ('gallery',)


class GalleryImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = Gallery
		fields = ('url', 'path', 'filesize')
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

	def get_alternate_md5(self, obj):
		return str(obj.url.size)


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
		fields = (
		'id', 'logo', 'urllogo', 'path', 'link', 'model', 'name', 'MSRP', 'power', 'torque', 'top_speed', 'city', 'hwy',
		'combined', 'acceleration', 'car_range', 'range_value', 'features_accessories', 'interior', 'exterior',
		'performance', 'upholsteries', 'wheels', 'packages', 'colours', 'gallery')
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
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = Trim
		fields = ('urllogo', 'path', 'filesize')
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

	def get_alternate_md5(self, obj):
		if obj.urllogo == '':
			return ''
		else:
			return str(obj.url.size)


class ModelsShownImageSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = ModelsShown
		fields = ('url', 'path', 'filesize',)
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

	def get_alternate_md5(self, obj):
		return str(obj.url.size)


class TrimEnSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')

	class Meta:
		model = TrimEnImage
		fields = ('id', 'url', 'path')

	def get_url_url(self, obj):
		if obj.url == '':
			pass
		else:
			return obj.url.url


# def get_url_url(self, obj):
#        return obj.url.url


class TrimFrSerializer(serializers.ModelSerializer):
	path = serializers.SerializerMethodField('get_url_url')

	class Meta:
		model = TrimFrImage
		fields = ('id', 'url', 'path')
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


# def get_url_url(self, obj):
#        return obj.url.url


'''

class StaticModelENSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = StaticModelEN
        fields = ('id', 'name', 'url', 'path', 'md5')
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


class StaticModelENImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = StaticModelEN
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


class StaticModelFRSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = StaticModelEN
        fields = ('id', 'name', 'url', 'path', 'md5')
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


class StaticModelFRImageSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_url_url')

    class Meta:
        model = StaticModelFR
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
'''


class StaticModelSerializer(serializers.ModelSerializer):
	#    path = serializers.SerializerMethodField('get_url_url')

	class Meta:
		model = StaticModel
		fields = ('id', 'name', 'path')


class StaticModelImageSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField('get_alternate_url')
	path = serializers.SerializerMethodField('get_alternate_path')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = StaticModel
		fields = ('url', 'path', 'filesize')

	def get_alternate_url(self, obj):
		return 'http://bmw.capeesh.ca/media/' + obj.url_en.name

	def get_alternate_path(self, obj):
		return '/media/' + obj.url_en.name

	def get_alternate_md5(self, obj):
		return str(obj.url_en.size)


class StaticModelImageFRSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField('get_alternate_url')
	path = serializers.SerializerMethodField('get_alternate_path')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = StaticModel
		fields = ('url', 'path', 'filesize')

	def get_alternate_url(self, obj):
		return 'http://bmw.capeesh.ca/media/' + obj.url_fr.name

	def get_alternate_path(self, obj):
		return '/media/' + obj.url_fr.name

	def get_alternate_md5(self, obj):
		return str(obj.url_fr.size)


class StandAloneOptionMSSerializer(serializers.ModelSerializer):
	class Meta:
		model = StandAloneOption
		fields = ('id', 'code', 'title', 'price')


class PackageMSSerializer(serializers.ModelSerializer):
	class Meta:
		model = Package
		fields = ('id', 'name', 'description', 'price_override', 'link', 'url', 'status_changed', 'code', 'field_type')


class OptionalEquipmentMSSerializer(serializers.ModelSerializer):
	class Meta:
		model = OptionalEquipment
		fields = ('id', 'code', 'title', 'price', 'field_type')


class ModelsShownSerializer(serializers.ModelSerializer):
	vehicle = TrimSerializer(read_only=True)
	#    path = serializers.SerializerMethodField('get_url_url')
	location = LocationSerializer(read_only=True, many=True)
	#    static_model_en  = StaticModelENSerializer(read_only=True)
	#    static_model_fr  = StaticModelFRSerializer(read_only=True)
	static_model = StaticModelSerializer(read_only=True)
	stand_alone_option = StandAloneOptionMSSerializer(read_only=True, many=True)
	package = PackageMSSerializer(read_only=True, many=True)
	optional_equipment = OptionalEquipmentMSSerializer(read_only=True, many=True)
	url = serializers.SerializerMethodField('get_alternate_url')
	path = serializers.SerializerMethodField('get_alternate_path')

	class Meta:
		model = ModelsShown
		fields = (
		'id', 'static_model_shown', 'vehicle', 'url', 'path', 'price_override', 'disclaimer', 'location', 'colour',
		'exterior', 'interior', 'trim_price', 'wheels', 'taxes', 'static_model', 'stand_alone_option', 'package',
		'optional_equipment')
		depth = 1

	# extra_kwargs = {
	#                'url': {
	#                    'required': False,
	#                 }
	#            }

	#    def get_url_url(self, obj):
	#        if obj.url == '':
	#            pass
	#        else:
	#            return obj.url.url

	#    def get_url_url(self, obj):
	#        return obj.url.url
	def get_alternate_url(self, obj):
		return 'http://bmw.capeesh.ca/media/' + obj.url_en.name

	def get_alternate_path(self, obj):
		return '/media/' + obj.url_en.name


class ModelsShownImageSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField('get_alternate_url')
	path = serializers.SerializerMethodField('get_alternate_path')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = ModelsShown
		fields = ('url', 'path', 'filesize',)
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}

	def get_url_url(self, obj):
		if obj.url_en == '':
			pass
		else:
			return obj.url_en.url

			#    def get_url_url(self, obj):
			#        return obj.url.url

	def get_alternate_url(self, obj):
		return 'http://bmw.capeesh.ca/media/' + obj.url_en.name

	def get_alternate_path(self, obj):
		return '/media/' + obj.url_en.name

	def get_alternate_md5(self, obj):
		if obj.url_en == '':
			pass
		else:
			return str(obj.url_en.size)


class ModelsShownFRImageSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField('get_alternate_url')
	path = serializers.SerializerMethodField('get_alternate_path')
	filesize = serializers.SerializerMethodField('get_alternate_md5')

	class Meta:
		model = ModelsShown
		fields = ('url', 'path', 'filesize',)
		extra_kwargs = {
			'url': {
				'required': False,
			}
		}

	def get_url_url(self, obj):
		if obj.url_fr == '':
			pass
		else:
			return obj.url_fr.url

			#    def get_url_url(self, obj):
			#        return obj.url.url

	def get_alternate_url(self, obj):
		return 'http://bmw.capeesh.ca/media/' + str(obj.url_fr.name)

	def get_alternate_path(self, obj):
		return '/media/' + str(obj.url_fr.name)

	def get_alternate_md5(self, obj):
		if obj.url_fr == '':
			pass
		else:
			return str(obj.url_fr.size)


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


class StandAloneOptionSerializer(serializers.ModelSerializer):
	stand_alone_model = ModelsSerializer(read_only=True, many=True)

	class Meta:
		model = StandAloneOption
		fields = ('id', 'code', 'title', 'price', 'stand_alone_model')


class OptionalEquipmentSerializer(serializers.ModelSerializer):
	stand_alone_model = ModelsSerializer(read_only=True, many=True)

	class Meta:
		model = OptionalEquipment
		fields = ('id', 'code', 'title', 'price', 'stand_alone_model', 'field_type')