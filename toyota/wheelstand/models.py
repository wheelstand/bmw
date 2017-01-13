from django.db import models
from django.utils.translation import ugettext_lazy as _
from colorfield.fields import ColorField
import choices
from django.core.files import File
import urllib
import os
from model_utils.fields import MonitorField
from .views import random_string


class Models(models.Model):
    name_en = models.CharField(max_length=255, help_text=_('English'), verbose_name="Name English")
    name_fr = models.CharField(max_length=255, help_text=_('French'), verbose_name="Name French", null=True, blank=True,)
    internal_id = models.CharField(max_length=255, null=True, blank=True,  verbose_name='Internal ID')   
    year = models.CharField(max_length=4, choices=choices.MODEL_YEAR_CHOICES)
    subhead_en = models.TextField(max_length=255, help_text=_('English'), verbose_name="Subhead English", null=True, blank=True)
    subhead_fr = models.TextField(max_length=255, help_text=_('French'), verbose_name="Subhead French", null=True, blank=True,)
    url_logo = models.ImageField(upload_to='uploads/models/', blank=True, null=True, verbose_name=_('Logo'))
    link_logo = models.CharField(max_length=255, null=True, blank=True, verbose_name="OR Remote URL")
    url = models.ImageField(upload_to='uploads/models/', blank=True, null=True, verbose_name=_('Image'),)
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name="OR Remote URL", )
    disclaimer_en = models.TextField(max_length=1000, null=True,
                                     blank=True, help_text=_('English'),
                                     verbose_name="Pricing Disclaimer English")
    disclaimer_fr = models.TextField(max_length=1000, null=True, blank=True,
                                     help_text=_('French'), verbose_name="Pricing Disclaimer French")
    base_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    freight_DPI = models.DecimalField(max_digits=8, decimal_places=2,
                                      blank=True, null=True, verbose_name='Freight & PDI')
    gallery = models.ManyToManyField('Gallery', blank=True)
    lease_APR_from = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True,)
    lease_APR_for = models.IntegerField(blank=True, null=True, help_text=_('Months'))
    lease_payment_from = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True,)
    down_payment = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True,)
    accessory = models.ManyToManyField('Accessories', blank=True)
    price_override = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True,)
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)

    class Meta:
        verbose_name_plural = "Models"

    def __unicode__(self):
        return u"%s" % self.name_en

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        if self.link_logo and not self.url_logo:
            result_logo = urllib.urlretrieve(self.link_logo)
            self.url_logo.save(
                    os.path.basename(self.link_logo),
                    File(open(result_logo[0]))
                    )            
        super(Models, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)

    def image_thumb_logo(self):
        if self.url_logo.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url_logo)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url_logo)

    image_thumb.allow_tags = True
    image_thumb_logo.allow_tags = True

    @property
    def name(self):
        return {
            'en': self.name_en,
            'fr': self.name_fr
        }

    @property
    def subhead(self):
        return {
            'en': self.subhead_en,
            'fr': self.subhead_fr
        }

    @property
    def disclaimer(self):
        return {
            'en': self.disclaimer_en,
            'fr': self.disclaimer_fr
        }


class Gallery(models.Model):
#    image = models.ForeignKey('Models', blank=True, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)  
    url = models.ImageField(upload_to='uploads/gallery/', null=True, blank=True, verbose_name=_('Image'),)
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)

    class Meta:
        verbose_name_plural = "Galleries"

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        super(Gallery, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)
    image_thumb.allow_tags = True

    def __unicode__(self):
        return u"%s" % self.url.name[16:]























        

class Trim(models.Model):
    model = models.ForeignKey('Models', blank=True, null=True)
    name_en = models.CharField(max_length=255, help_text=_('English'), verbose_name="Name English")
    name_fr = models.CharField(max_length=255, help_text=_('French'), verbose_name="Name French", null=True, blank=True)
    internal_id = models.CharField(max_length=255, null=True, blank=True, verbose_name='Internal ID')   
    url = models.ImageField(upload_to='uploads/interiors/', null=True,  blank=True, verbose_name=_('Image'),)
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)
    features_en = models.TextField(max_length=2000, help_text=_('English'), verbose_name="Features English")
    features_fr = models.TextField(max_length=2000, help_text=_('French'), verbose_name="Features French", null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    colour = models.ForeignKey('Colours', blank=True, null=True)
    url_colour = models.ImageField(upload_to='uploads/interiors/', null=True,  blank=True, verbose_name=_('Image'))
    link_colour = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
    md5_colour = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed_colour = MonitorField(monitor='url', editable=False)
    interiors = models.ManyToManyField('Interiors', blank=True, )
#    starsafety = models.BooleanField(default='False', verbose_name='Star Safety')
#    TSS = models.BooleanField(default='False', verbose_name='Toyota Safety Sense')

    class Meta:
        verbose_name_plural = "Trims"

    def __unicode__(self):
        return u"%s" % self.name_en

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.status_changed_colour:
            self.md5_colour = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        super(Trim, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)

    def image_thumb_colour(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url_colour)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url_colour)
    image_thumb.allow_tags = True


    def get_interiors(self):
        return ",".join([str(p) for p in self.interiors.all()])    

    @property
    def name(self):
        return {
            'en': self.name_en,
            'fr': self.name_fr
        }

    @property
    def features(self):
        return {
            'en': self.features_en,
            'fr': self.features_fr
        }

#    def model(self):
#        return {
#            'model': self.model
#        }




class ColourGallery(models.Model):
    trim_gallery = models.ForeignKey('Trim', blank=True, null=True, related_name='trim_gallery')
    name = models.CharField(max_length=255, null=True, blank=True) 
    hexcode = ColorField(default='#FFFFFF') 
    url = models.ImageField(upload_to='uploads/colourgallery/', null=True, blank=True, verbose_name=_('Image'),)
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)

    class Meta:
        verbose_name_plural = "Colour Gallery"

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        super(ColourGallery, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)
    image_thumb.allow_tags = True

    def __unicode__(self):
        return u"%s" % self.name

    def related_trim(self, obj):
        return obj.trim_gallery.name
    related_trim.short_description = 'Trim'
















class Accessories(models.Model):
    name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
    name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), null=True, blank=True)
    base_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Accessories"

    def __unicode__(self):
        return u"%s" % self.name_en

    @property
    def name(self):
        return {
            'en': self.name_en,
            'fr': self.name_fr
        }


class ModelsShown(models.Model):
    vehicle = models.ForeignKey('Models', blank=True, null=True)
    trim = models.ForeignKey('Trim', blank=True, null=True)
    colour = models.ForeignKey('Colours', blank=True, null=True)
#    subhead_en = models.CharField(max_length=255, help_text=_('English'), verbose_name="Subhead English", null=True, blank=True)
#    subhead_fr = models.CharField(max_length=255, help_text=_('French'), verbose_name="Subhead French", null=True, blank=True,)
    legal_disclaimer_en = models.CharField(max_length=500, null=True,
                                     blank=True, help_text=_('English'),
                                     verbose_name="Legal Disclaimer English")
    legal_disclaimer_fr = models.CharField(max_length=500, null=True, blank=True,
                                     help_text=_('French'), verbose_name="Legal Disclaimer French")
    standard_features_en = models.TextField(max_length=2000, help_text=_('English'), verbose_name="Standard Features English")
    standard_features_fr = models.TextField(max_length=2000, help_text=_('French'), verbose_name="Standard Features French", null=True, blank=True)
    price_override = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fuel_city = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fuel_highway = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fuel_combined = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    horsepower = models.IntegerField(null=True, blank=True,)
    engine_displacement = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    engine_description_en = models.CharField(max_length=255, null=True,
                                     blank=True, help_text=_('English'),
                                     verbose_name="Engine Description English")
    engine_description_fr = models.CharField(max_length=255, null=True, blank=True, help_text=_('French'), verbose_name="Engine Description English")
    seats = models.IntegerField(null=True, blank=True,)
    airbags = models.IntegerField(null=True, blank=True,)
    torque = models.IntegerField(null=True, blank=True,)
    towing_capacity = models.IntegerField(null=True, blank=True,)
    accessory = models.ForeignKey('Accessories', blank=True, null=True)
    price_override_accessory = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    location = models.ManyToManyField('Location', blank=True)

    interiors = models.ManyToManyField('ModelsShownInteriors', blank=True)
    all_accessories = models.ManyToManyField('AllAccessories', blank=True)
    accessories_shown = models.ManyToManyField('AccessoriesShown', blank=True)
    starsafety = models.BooleanField(default='False', verbose_name='Star Safety')
    TSS = models.BooleanField(default='False', verbose_name='Toyota Safety Sense')   
    series_code = models.CharField(max_length=255, null=True, blank=True, verbose_name="Series Code")  
    IIHS = models.BooleanField(default='False', verbose_name='IIHS')   


    class Meta:
        verbose_name_plural = "Models Shown"

    def __unicode__(self):
        return u"%s" % self.trim

#    @property
#    def subhead(self):
#        return {
#            'en': self.subhead_en,
#            'fr': self.subhead_fr
#        }

    @property
    def legal_disclaimer(self):
        return {
            'en': self.legal_disclaimer_en,
            'fr': self.legal_disclaimer_fr
        }

    @property
    def standard_features(self):
        return {
            'en': self.standard_features_en,
            'fr': self.standard_features_fr
        }

    @property
    def engine_description(self):
        return {
            'en': self.engine_description_en,
            'fr': self.engine_description_fr
        }




class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'), help_text=_('English'))
    language_default = models.CharField(max_length=4, choices=choices.LANGUAGE_CHOICES, default='EN')

    class Meta:
        verbose_name_plural = "Locations"

    def __unicode__(self):
        return u"%s" % self.name


class Colours(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'), help_text=_('English'))
    hexcode = ColorField(default='#FFFFFF')

    class Meta:
        verbose_name_plural = "Colours"

    def __unicode__(self):
        return u"%s" % self.name


class Interiors(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    hexcode = ColorField(default='#FFFFFF') 
    url = models.ImageField(upload_to='uploads/interiors/', null=True, blank=True, verbose_name=_('Image'),)
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)

    class Meta:
        verbose_name_plural = "Interiors"

    def __unicode__(self):
        return u"%s" % self.name

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        super(Interiors, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)
    image_thumb.allow_tags = True

    def get_trims(self):
        return ",".join([str(p) for p in self.trim_set.all()])


class DealerProvince(models.Model):
    province = models.CharField(max_length=255)
    provincial_code = models.CharField(max_length=4, choices=choices.PROVINCES, default='ON')

    class Meta:
        verbose_name_plural = "Dealer Province"

    def __unicode__(self):
        return u"%s" % self.province


class DealerCity(models.Model):
    cityname = models.CharField(max_length=255)
    province = models.ForeignKey('DealerProvince', blank=True, null=True, related_name='dealercity')

    class Meta:
        verbose_name_plural = "Dealer City"

    def __unicode__(self):
        return u"%s" % self.cityname


class Dealers(models.Model):
    order = models.IntegerField(blank=True, null=True)
    dealer_id = models.CharField(max_length=20, blank=True, null=True)
    dealer_name = models.CharField(max_length=255, blank=True, null=True)
    cityname = models.ForeignKey('DealerCity', blank=True, null=True, related_name='dealers')
#    city = models.CharField(max_length=255, blank=True, null=True)
#    province = models.ForeignKey('DealerProvince', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Dealer"

    def __unicode__(self):
        return u"%s" % self.dealer_name 
















class ModelsShownInteriors(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    hexcode = ColorField(default='#FFFFFF') 
    url = models.ImageField(upload_to='uploads/modelsshowninteriors/', null=True, blank=True, verbose_name=_('Image'),)
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)

    class Meta:
        verbose_name_plural = "Models Shown Interiors"

    def __unicode__(self):
        return u"%s" % self.name

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        super(ModelsShownInteriors, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)
    image_thumb.allow_tags = True

    def get_trims(self):
        return ",".join([str(p) for p in self.trim_set.all()])        


class ModelsShownGallery(models.Model):
    models_shown_gallery = models.ForeignKey('ModelsShown', blank=True, null=True, related_name='models_shown_gallery')
    name = models.CharField(max_length=255, null=True, blank=True) 
    hexcode = ColorField(default='#FFFFFF') 
    url = models.ImageField(upload_to='uploads/modelsshowngallery/', null=True, blank=True, verbose_name=_('Image'),)
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
    md5 = models.CharField(default=random_string(), max_length=255, editable=False)
    status_changed = MonitorField(monitor='url', editable=False)

    class Meta:
        verbose_name_plural = "Models Shown Gallery"

    def save(self, *args, **kwargs):
        if self.status_changed:
            self.md5 = random_string()
        if self.link and not self.url:
            result = urllib.urlretrieve(self.link)
            self.url.save(
                    os.path.basename(self.link),
                    File(open(result[0]))
                    )
        super(ModelsShownGallery, self).save(*args, **kwargs)

    def image_thumb(self):
        if self.url.name is None:
            return '<img src="/media/%s" width="0" height="0" />' % (self.url)
        else:
            return '<img src="/media/%s" width="100" height="100" />' % (self.url)
    image_thumb.allow_tags = True

    def __unicode__(self):
        return u"%s" % self.name


class AllAccessories(models.Model):
    name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
    name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), null=True, blank=True)
    base_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = "All Accessories"

    def __unicode__(self):
        return u"%s" % self.name_en

    @property
    def name(self):
        return {
            'en': self.name_en,
            'fr': self.name_fr
        }


class AccessoriesShown(models.Model):
    name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
    name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), null=True, blank=True)
    base_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Accessories Shown"

    def __unicode__(self):
        return u"%s" % self.name_en

    @property
    def name(self):
        return {
            'en': self.name_en,
            'fr': self.name_fr
        }        


class TestDrive(models.Model):
    testdrive = models.CharField(max_length=3000, blank=False, default='')    
    status = models.BooleanField(default='')    
