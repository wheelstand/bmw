from ..models import Models, Trim, ModelsShown, Accessories, Location, Colours, Interiors, Gallery, ColourGallery, DealerProvince, Dealers, DealerProvince, ModelsShownInteriors, ModelsShownGallery, AllAccessories, AccessoriesShown, DealerCity, TestDrive
from rest_framework import viewsets, generics
from serializers import ModelsSerializer, TrimSerializer, ModelsShownSerializer, AccessoriesSerializer, LocationSerializer, ColoursSerializer, InteriorsSerializer, InteriorsImageSerializer, TrimImageSerializer, GalleryImageSerializer, ModelsImageSerializer, GallerySerializer, ColourGallerySerializer,ColourGalleryImageSerializer, DealersSerializer, DealerProvinceSerializer, ModelsShownInteriorsSerializer, ModelsShownGallerySerializer, AllAccessoriesSerializer, AccessoriesShownSerializer, ModelsShownGalleryImageSerializer, DealerCitySerializer, TestDriveSerializer
from drf_multiple_model.views import MultipleModelAPIView


class ModelsViewSet(viewsets.ModelViewSet):
    queryset = Models.objects.all()
    serializer_class = ModelsSerializer


class TrimViewSet(viewsets.ModelViewSet):
    queryset = Trim.objects.all()
    serializer_class = TrimSerializer


class ModelsShownViewSet(viewsets.ModelViewSet):
    queryset = ModelsShown.objects.all()
    serializer_class = ModelsShownSerializer


class AccessoriesViewSet(viewsets.ModelViewSet):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ColoursViewSet(viewsets.ModelViewSet):
    queryset = Colours.objects.all()
    serializer_class = ColoursSerializer


class InteriorsViewSet(viewsets.ModelViewSet):
    queryset = Interiors.objects.all()
    serializer_class = InteriorsSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class ColourGalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = ColourGallerySerializer


class DealerProvinceViewSet(viewsets.ModelViewSet):
    queryset = DealerProvince.objects.all()
    serializer_class = DealerProvinceSerializer


class DealerCityViewSet(viewsets.ModelViewSet):
    queryset = DealerCity.objects.all()
    serializer_class = DealerCitySerializer


class DealersViewSet(viewsets.ModelViewSet):
    queryset = Dealers.objects.all()
    serializer_class = DealersSerializer





class ModelsShownInteriorsViewSet(viewsets.ModelViewSet):
    queryset = ModelsShownInteriors.objects.all()
    serializer_class = ModelsShownInteriorsSerializer

class ModelsShownGalleryViewSet(viewsets.ModelViewSet):
    queryset = ModelsShownGallery.objects.all()
    serializer_class = ModelsShownGallerySerializer

class AllAccessoriesViewSet(viewsets.ModelViewSet):
    queryset = AllAccessories.objects.all()
    serializer_class = AllAccessoriesSerializer

class AccessoriesShownViewSet(viewsets.ModelViewSet):
    queryset = AccessoriesShown.objects.all()
    serializer_class = AccessoriesShownSerializer


class TestDriveList(generics.ListCreateAPIView):
    queryset = TestDrive.objects.all()
    serializer_class = TestDriveSerializer


class AllAPIView(MultipleModelAPIView):
    objectify = True
    queryList = [
        (Models.objects.all(), ModelsSerializer),
        (Trim.objects.all(), TrimSerializer),
        (ModelsShown.objects.all(), ModelsShownSerializer),
        (Accessories.objects.all(), AccessoriesSerializer),
        (Location.objects.all(), LocationSerializer),
        (Colours.objects.all(), ColoursSerializer),
        (Interiors.objects.all(), InteriorsSerializer),
        (Gallery.objects.all(), GallerySerializer),        
        (ColourGallery.objects.all(), ColourGallerySerializer),    
        (DealerProvince.objects.all(), DealerProvinceSerializer),
        (Dealers.objects.all(), DealersSerializer), 


        (ModelsShownInteriors.objects.all(), ModelsShownInteriorsSerializer), 
        (ModelsShownGallery.objects.all(), ModelsShownGallerySerializer),         
        (AllAccessories.objects.all(), AllAccessoriesSerializer), 
        (AccessoriesShown.objects.all(), AccessoriesShownSerializer),
    ]


class AllAPIImagesView(MultipleModelAPIView):
    flat = True
    add_model_type = False

    queryList = [
        (Interiors.objects.all(), InteriorsImageSerializer),
        (Trim.objects.all(), TrimImageSerializer),
        (Gallery.objects.all(), GalleryImageSerializer),
        (Models.objects.all(), ModelsImageSerializer),
        (ColourGallery.objects.all(), ColourGalleryImageSerializer),
        (ModelsShownGallery.objects.all(), ModelsShownGalleryImageSerializer), 
    ]
