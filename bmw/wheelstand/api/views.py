from ..models import Models, Trim, ModelsShown, FeaturesAccessory, \
    Exterior, Upholstery, Wheel, Package, Option, Location, TrimEnImage, TrimFrImage, Gallery, Interior, Performance, Colour, Information, TestDrive, KeepingInTouch
from rest_framework import viewsets, generics
from serializers import ModelsSerializer, TrimSerializer, ModelsShownSerializer, \
    FeaturesAccessorySerializer, ExteriorSerializer, \
    WheelSerializer, PackageSerializer, LocationSerializer, \
    UserSerializer, GroupSerializer, WheelImageSerializer, PackageImageSerializer,\
    FeaturesAccessoryImageSerializer, UpholsteryImageSerializer, \
    ModelsShownImageSerializer, TrimEnSerializer, TrimFrSerializer, \
    TrimEnImageSerializer, TrimFrImageSerializer, GallerySerializer, GalleryImageSerializer, InteriorSerializer, PerformanceSerializer, ColourSerializer, UpholsterySerializer, InformationSerializer, TestDriveSerializer, KeepingInTouchSerializer, TrimImageSerializer
from django.contrib.auth.models import User, Group
from drf_multiple_model.views import MultipleModelAPIView


class ModelsViewSet(viewsets.ModelViewSet):
    queryset = Models.objects.all()
    serializer_class = ModelsSerializer


class TrimEnImageViewSet(viewsets.ModelViewSet):
    queryset = TrimEnImage.objects.all()
    serializer_class = TrimEnImageSerializer


class TrimViewSet(viewsets.ModelViewSet):
    queryset = Trim.objects.all()
    serializer_class = TrimSerializer


class ModelsShownViewSet(viewsets.ModelViewSet):
    queryset = ModelsShown.objects.all()
    serializer_class = ModelsShownSerializer


class FeaturesAccessoryViewSet(viewsets.ModelViewSet):
    queryset = FeaturesAccessory.objects.all()
    serializer_class = FeaturesAccessorySerializer


class ExteriorViewSet(viewsets.ModelViewSet):
    queryset = Exterior.objects.all()
    serializer_class = ExteriorSerializer


class InteriorViewSet(viewsets.ModelViewSet):
    queryset = Interior.objects.all()
    serializer_class = InteriorSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer


class ColoursViewSet(viewsets.ModelViewSet):
    queryset = Colour.objects.all()
    serializer_class = ColourSerializer    


class UpholsteryViewSet(viewsets.ModelViewSet):
    queryset = Upholstery.objects.all()
    serializer_class = UpholsterySerializer


class WheelViewSet(viewsets.ModelViewSet):
    queryset = Wheel.objects.all()
    serializer_class = WheelSerializer


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


#class OptionViewSet(viewsets.ModelViewSet):
#    queryset = Option.objects.all()
#    serializer_class = OptionSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class InformationList(generics.ListCreateAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer


class TestDriveList(generics.ListCreateAPIView):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializer


class KeepingInTouchList(generics.ListCreateAPIView):
    queryset = KeepingInTouch.objects.all()
    serializer_class = KeepingInTouchSerializer


class AllAPIView(MultipleModelAPIView):
    objectify = True
    queryList = [
        (Models.objects.all(), ModelsSerializer),
#        (TrimEnImage.objects.all(), TrimEnSerializer),
#        (TrimFrImage.objects.all(), TrimFrSerializer),
        (Trim.objects.all(), TrimSerializer),
        (ModelsShown.objects.all(), ModelsShownSerializer),
        (FeaturesAccessory.objects.all(), FeaturesAccessorySerializer),
#        (Exterior.objects.all(), ExteriorSerializer),
        (Upholstery.objects.all(), UpholsterySerializer),
        (Wheel.objects.all(), WheelSerializer),
        (Package.objects.all(), PackageSerializer),
#        (Option.objects.all(), OptionSerializer),
        (Location.objects.all(), LocationSerializer),
        (Gallery.objects.all(), GallerySerializer),  
#        (Interior.objects.all(), InteriorSerializer),
#        (Performance.objects.all(), PerformanceSerializer),
        (Colour.objects.all(), ColourSerializer),       
         
    ]


class AllAPIImagesView(MultipleModelAPIView):
    flat = True
    add_model_type = False

    queryList = [
        (TrimEnImage.objects.all(), TrimEnImageSerializer),
        (TrimFrImage.objects.all(), TrimFrImageSerializer),
        (ModelsShown.objects.all(), ModelsShownImageSerializer),
        (Upholstery.objects.all(), UpholsteryImageSerializer),   
        (FeaturesAccessory.objects.all(), FeaturesAccessoryImageSerializer),
        (Package.objects.all(), PackageImageSerializer),
        (Wheel.objects.all(), WheelImageSerializer),
        (Gallery.objects.all(), GalleryImageSerializer),  
        (Trim.objects.all(), TrimImageSerializer),     
    ]
