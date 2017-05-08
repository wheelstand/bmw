from colorfield.fields import ColorField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from wheelstand import choices
import hashlib
import uuid
from model_utils.fields import MonitorField
import urllib, os
from django.core.files import File
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from sortedm2m.fields import SortedManyToManyField


def random_string():
	salt = uuid.uuid4().hex
	return hashlib.md5(salt.encode()).hexdigest()


class Models(models.Model):
	name_en = models.CharField(max_length=255,
	                           verbose_name=_('Name English'),
	                           help_text=_('English'))
	name_fr = models.CharField(max_length=255,
	                           verbose_name=_('Name French'),
	                           blank=True, null=True,
	                           help_text=_('French'))
	year = models.CharField(max_length=4, choices=choices.MODEL_YEAR_CHOICES)
	base_price = models.DecimalField(max_digits=8,
	                                 decimal_places=0,
	                                 blank=True,
	                                 null=True)
	freight_DPI = models.DecimalField(max_digits=8,
	                                  decimal_places=0,
	                                  blank=True,
	                                  null=True,
	                                  verbose_name='Freight & PDI')

	colour = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	exterior = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	interior = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	trim_price = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	optional_equipement = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	wheels = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	taxes = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	isBMWi = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = "Models"

	def __unicode__(self):
		if self.name_en[-5:-1] == 'Coup':
			return u"%s%s" % (self.name_en[:-1], 'e')
		else:
			return u"%s" % self.name_en

	@property
	def name(self):
		return {
			'en': self.name_en,
			'fr': self.name_fr
		}


class StaticModelEN(models.Model):
	name = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'), blank=True,
	                        default='')
	url = models.ImageField(max_length=255, upload_to='uploads/static_en/', null=True, blank=True,
	                        verbose_name=_('Image'))
	link = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
	md5 = models.CharField(default=random_string(), max_length=255, editable=False)
	status_changed = MonitorField(monitor='url', editable=False)

	def __unicode__(self):
		return u"%s" % self.name

	def new_md5(self):
		if status_changed:
			self.md5 = random_string()

	def save(self, *args, **kwargs):
		if self.link and not self.url:
			result = urllib.urlretrieve(self.link)
			self.url.save(
				os.path.basename(self.link),
				File(open(result[0]))
			)
		super(StaticModelEN, self).save(*args, **kwargs)


class StaticModelFR(models.Model):
	name = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), blank=True,
	                        default='')
	url = models.ImageField(max_length=255, upload_to='uploads/static_fr/', null=True, blank=True,
	                        verbose_name=_('Image'))
	link = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
	md5 = models.CharField(default=random_string(), max_length=255, editable=False)
	status_changed = MonitorField(monitor='url', editable=False)

	def __unicode__(self):
		return u"%s" % self.name

	def new_md5(self):
		if status_changed:
			self.md5 = random_string()

	def save(self, *args, **kwargs):
		if self.link and not self.url:
			result = urllib.urlretrieve(self.link)
			self.url.save(
				os.path.basename(self.link),
				File(open(result[0]))
			)
		super(StaticModelFR, self).save(*args, **kwargs)


class StaticModel(models.Model):
	name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('French'), blank=True,
	                           default='')
	url_en = models.ImageField(max_length=255, upload_to='uploads/static_fr/', null=True, blank=True,
	                           verbose_name=_('Image English'))
	name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), blank=True,
	                           default='')
	url_fr = models.ImageField(max_length=255, upload_to='uploads/static_fr/', null=True, blank=True,
	                           verbose_name=_('Image French'))

	def __unicode__(self):
		return u"%s" % self.name_en

	@property
	def name(self):
		return {
			'en': self.name_en,
			'fr': self.name_fr
		}

	@property
	def path(self):
		return {
			'en': '/media/' + self.url_en.name,
			'fr': '/media/' + self.url_fr.name
		}


class TrimEnImage(models.Model):
	url = models.ImageField(max_length=255, upload_to='uploads/trims_en/', null=True, blank=True,
	                        verbose_name=_('Image'))
	link = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
	md5 = models.CharField(default=random_string(), max_length=255, editable=False)
	status_changed = MonitorField(monitor='url', editable=False)

	def __unicode__(self):
		return u"%s" % self.link

	def new_md5(self):
		if status_changed:
			self.md5 = random_string()

	def save(self, *args, **kwargs):
		if self.link and not self.url:
			result = urllib.urlretrieve(self.link)
			self.url.save(
				os.path.basename(self.link),
				File(open(result[0]))
			)
		super(TrimEnImage, self).save(*args, **kwargs)


class TrimFrImage(models.Model):
	url = models.ImageField(max_length=255, upload_to='uploads/trims_fr/', null=True, blank=True,
	                        verbose_name=_('Image'))
	link = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
	md5 = models.CharField(default=random_string(), max_length=255, editable=False)
	status_changed = MonitorField(monitor='url', editable=False)

	def __unicode__(self):
		return u"%s" % self.link

	def new_md5(self):
		if status_changed:
			self.md5 = random_string()

	def save(self, *args, **kwargs):
		if self.link and not self.url:
			result = urllib.urlretrieve(self.link)
			self.url.save(
				os.path.basename(self.link),
				File(open(result[0]))
			)
		super(TrimFrImage, self).save(*args, **kwargs)


class Trim(models.Model):
	model = models.ForeignKey('Models', blank=True, null=True)
	image_en = models.OneToOneField('TrimEnImage', blank=True,
	                                null=True,
	                                verbose_name=_('Image English'),
	                                help_text=_('English'))
	image_fr = models.OneToOneField('TrimFrImage',
	                                blank=True,
	                                null=True,
	                                verbose_name=_('Image French'),
	                                help_text=_('French'))
	name_en = models.CharField(max_length=255,
	                           verbose_name=_('Name English'),
	                           help_text=_('English'))
	name_fr = models.CharField(max_length=255,
	                           verbose_name=_('Name French'),
	                           blank=True, null=True,
	                           help_text=_('French'))
	MSRP = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	power = models.CharField(max_length=255, blank=True)
	torque = models.CharField(max_length=255, blank=True)
	top_speed = models.CharField(max_length=255, blank=True, verbose_name=('Consumption'))
	acceleration = models.CharField(max_length=255, blank=True)
	features_accessories = SortedManyToManyField('FeaturesAccessory',
	                                             blank=True,
	                                             verbose_name=_('Features and Accessories'))
	#    exteriors = models.ManyToManyField('Exterior', blank=True)
	colours = models.ManyToManyField('Colour', blank=True)
	upholsteries = models.ManyToManyField('Upholstery',
	                                      blank=True,
	                                      verbose_name=_('Upholstery'))

	wheels = SortedManyToManyField('Wheel', blank=True)
	packages = SortedManyToManyField('Package', blank=True)
	#    options = models.ManyToManyField('Option', blank=True)
	gallery = models.ManyToManyField('Gallery', blank=True)
	interior_en = models.TextField(null=True, blank=True, verbose_name=('Interior English'), help_text=_('English'))
	performance_en = models.TextField(null=True, blank=True, verbose_name=('Performance English'),
	                                  help_text=_('English'))
	exterior_en = models.TextField(null=True, blank=True, verbose_name=('Exterior English'), help_text=_('English'))
	interior_fr = models.TextField(null=True, blank=True, verbose_name=('Interior French'), help_text=_('French'))
	performance_fr = models.TextField(null=True, blank=True, verbose_name=('Performance French'), help_text=_('French'))
	exterior_fr = models.TextField(null=True, blank=True, verbose_name=('Exterior French'), help_text=_('French'))
	#   colour = models.TextField(null=True, blank=True)
	city = models.CharField(max_length=255, blank=True)
	hwy = models.CharField(max_length=255, blank=True)
	combined = models.CharField(max_length=255, blank=True)

	logo = models.CharField(max_length=255, blank=True)
	urllogo = models.ImageField(max_length=255, upload_to='uploads/logo/', blank=True, verbose_name=_('Image'),
	                            default='')
	link = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
	md5 = models.CharField(default=random_string(), max_length=255, editable=False)
	status_changed = MonitorField(monitor='urllogo', editable=False)
	car_range = models.BooleanField(default=False, verbose_name=('Range'))
	range_value = models.CharField(max_length=255, blank=True)

	def __unicode__(self):
		return u"%s" % self.name_en

	@property
	def name(self):
		return {
			'en': self.name_en,
			'fr': self.name_fr
		}

	@property
	def image(self):
		return {
			'en': self.image_original_en,
			'fr': self.image_original_fr
		}

	@property
	def path_en(self):
		return self.image_original_en

	@property
	def url_en(self):
		return self.image_original_en

	@property
	def path_fr(self):
		return self.image_original_en

	@property
	def url_fr(self):
		return self.image_original_fr

	@property
	def trim_en(self):
		return {
			'url': self.image_original_en,
			'path': self.image_original_en,
			'md5': self.md5_en
		}

	@property
	def trim_fr(self):
		return {
			'url': self.image_original_fr,
			'path': self.image_original_fr,
			'md5': self.md5_fr
		}

	@property
	def interior(self):
		return {
			'en': self.interior_en,
			'fr': self.interior_fr
		}

	@property
	def exterior(self):
		return {
			'en': self.exterior_en,
			'fr': self.exterior_fr
		}

	@property
	def performance(self):
		return {
			'en': self.performance_en,
			'fr': self.performance_fr
		}

	@models.permalink
	def get_absolute_url(self):
		return ('trim_view', (), {'slug': self.slug})

	def new_md5(self):
		if status_changed:
			self.md5 = random_string()

	def save(self, *args, **kwargs):
		if self.link and not self.urllogo:
			result = urllib.urlretrieve(self.link)
			self.urllogo.save(
				os.path.basename(self.link),
				File(open(result[0]))
			)
		super(Trim, self).save(*args, **kwargs)


class Gallery(models.Model):
	#    trim = models.ForeignKey('Trim', blank=True, null=True, related_name='gallery')
	name = models.CharField(max_length=255, null=True, blank=True)
	url = models.ImageField(upload_to='uploads/gallery/', null=True, blank=True, verbose_name=_('Image'))
	link = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
	md5 = models.CharField(default=random_string(), max_length=255, editable=False)
	status_changed = MonitorField(monitor='url', editable=False)

	class Meta:
		verbose_name_plural = "Galleries"

	def new_md5(self):
		if status_changed:
			self.md5 = random_string()

	def save(self, *args, **kwargs):
		if self.link and not self.url:
			result = urllib.urlretrieve(self.link)
			self.url.save(
				os.path.basename(self.link),
				File(open(result[0]))
			)
		super(Gallery, self).save(*args, **kwargs)

	def __unicode__(self):
		return u"%s" % self.name

	def image_thumb(self):
		if self.url.name is None:
			return '<img src="/media/%s" width="0" height="0" />' % (self.url)
		else:
			return '<img src="/media/%s" width="100" height="100" />' % (self.url)

	image_thumb.allow_tags = True


class ModelsShown(models.Model):
	vehicle = models.ForeignKey('Trim', blank=True, null=True)
	url_en = models.ImageField(max_length=255, upload_to='uploads/models_shown/', null=True, blank=True,
	                           verbose_name=_('Image'))
	link = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))

	md5 = models.CharField(default=random_string(), max_length=255, editable=False)

	url_fr = models.ImageField(max_length=255, upload_to='uploads/models_shown/', null=True, blank=True,
	                           verbose_name=_('Image_fr'))
	link_fr = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
	md5_fr = models.CharField(default=random_string(), max_length=255, editable=False)

	price_override = models.DecimalField(max_digits=8,
	                                     decimal_places=2,
	                                     blank=True,
	                                     null=True)
	disclaimer_override_en = models.TextField(max_length=2000,
	                                          verbose_name=_('Disclaimer English'),
	                                          null=True,
	                                          blank=True,
	                                          help_text=_('English'))
	disclaimer_override_fr = models.TextField(max_length=2000,
	                                          verbose_name=_('Disclaimer French'),
	                                          null=True,
	                                          blank=True,
	                                          help_text=_('French'))
	location = models.ManyToManyField('Location', blank=True)
	status_changed = MonitorField(monitor='url')
	colour_en = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('Colour English'),
	                             help_text=_('English'))
	colour_fr = models.CharField(blank=True, null=True, max_length=255, verbose_name=_('Colour French'),
	                             help_text=_('English'))
	exterior = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	interior = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	trim_price = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	optional_equipement = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	wheels = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	taxes = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=False, default=0)
	static_model_shown_en = models.ImageField(max_length=255, upload_to='uploads/static_models_shown/', null=True,
	                                          blank=True, verbose_name=_('Static Models Shown Image English'),
	                                          help_text=_('English'))
	#    static_model_shown_fr = models.ImageField(max_length=255, upload_to='uploads/static_models_shown/', null=True, blank=True, verbose_name=_('Static Models Shown Image French'), help_text=_('French'))
	static_model_en = models.OneToOneField('StaticModelEN', blank=True,
	                                       null=True,
	                                       verbose_name=_('Image English'),
	                                       help_text=_('English'))
	static_model_fr = models.OneToOneField('StaticModelFR',
	                                       blank=True,
	                                       null=True,
	                                       verbose_name=_('Image French'),
	                                       help_text=_('French'))
	static_model = models.OneToOneField('StaticModel', blank=True,
	                                    null=True,
	                                    verbose_name=_('Static Image'),
	                                    help_text=_('Static Image'))
	stand_alone_option = models.ManyToManyField('StandAloneOption', blank=True)
	package = models.ManyToManyField('Package', blank=True)
	optional_equipment = models.ManyToManyField('OptionalEquipment', blank=True)

	class Meta:
		verbose_name_plural = "Models Shown"

	@property
	def colour(self):
		return {
			'en': self.colour_en,
			'fr': self.colour_fr
		}

	@property
	def disclaimer(self):
		return {
			'en': self.disclaimer_override_en,
			'fr': self.disclaimer_override_fr
		}

	@property
	def static_model_shown(self):
		return {
			'en': self.static_model_shown_en,
			'fr': self.static_model_shown_fr
		}

	@property
	def url(self):
		return {
			'en': self.url_en.name,
			'fr': self.url_fr.name
		}

	@property
	def path(self):
		return {
			'en': '/media/' + str(self.url_en.name),
			'fr': '/media/' + str(self.url_fr.name)
		}

	def new_md5(self):
		if status_changed:
			self.md5 = random_string()

	def save(self, *args, **kwargs):
		if self.status_changed:
			self.md5 = random_string()
		if self.link and not self.url_en:
			result = urllib.urlretrieve(self.link)
			self.url_en.save(
				os.path.basename(self.link),
				File(open(result[0]))
			)
		if self.link_fr and not self.url_fr:
			result = urllib.urlretrieve(self.link_fr)
			self.url_fr.save(
				os.path.basename(self.link_fr),
				File(open(result[0]))
			)
		super(ModelsShown, self).save(*args, **kwargs)

	def image_thumb(self):
		if self.url.name is None:
			return '<img src="/media/%s" width="0" height="0" />' % (self.url)
		else:
			return '<img src="/media/%s" width="100" height="100" />' % (self.url)

	image_thumb.allow_tags = True

	def image_thumb_fr(self):
		if self.url_fr.name is None:
			return '<img src="/media/%s" width="0" height="0" />' % (self.url_fr)
		else:
			return '<img src="/media/%s" width="100" height="100" />' % (self.url_fr)

	image_thumb_fr.allow_tags = True


class FeaturesAccessory(models.Model):
	name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
	name_fr = models.CharField(max_length=255, verbose_name=_('Name French'),
	                           help_text=_('French'), blank=True, null=True)
	description_en = models.TextField(max_length=2000, verbose_name=_('Description English'), help_text=_('English'))
	description_fr = models.TextField(max_length=2000, verbose_name=_('Description French'), help_text=_('French'),
	                                  blank=True, null=True)
	url = models.ImageField(max_length=255, upload_to='uploads/features_accessory/', null=True, blank=True,
	                        verbose_name=_('Image'))
	link = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
	md5 = models.CharField(default=random_string(), max_length=255, editable=False)
	status_changed = MonitorField(monitor='url')

	class Meta:
		verbose_name_plural = "Features & Accessories"
		ordering = ['name_en']

	def __unicode__(self):
		return u"%s - %s" % (self.name_en, self.trim)

	@property
	def name(self):
		return {
			'en': self.name_en,
			'fr': self.name_fr
		}

	@property
	def description(self):
		return {
			'en': self.description_en,
			'fr': self.description_fr
		}

	def new_md5(self):
		if status_changed:
			self.md5 = random_string()

	def save(self, *args, **kwargs):
		if self.link and not self.url:
			result = urllib.urlretrieve(self.link)
			self.url.save(
				os.path.basename(self.link),
				File(open(result[0]))
			)
		super(FeaturesAccessory, self).save(*args, **kwargs)

	def image_thumb(self):
		if self.url.name is None:
			return '<img src="/media/%s" width="0" height="0" />' % (self.url)
		else:
			return '<img src="/media/%s" width="100" height="100" />' % (self.url)

	image_thumb.allow_tags = True

	def trims(self):
		return ",".join([str(p) for p in self.trim_set.all()])

	@property
	def trim(self):
		return ",".join([str(p) for p in self.trim_set.all()])


class Exterior(models.Model):
	name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
	name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), blank=True,
	                           null=True)
	hexcode = ColorField(default='#FFFFFF')

	def __unicode__(self):
		return u"%s" % self.name_en

	@property
	def name(self):
		return {
			'en': self.name_en,
			'fr': self.name_fr
		}

	def trims(self):
		return ",".join([str(p) for p in self.trim_set.all()])


class Upholstery(models.Model):
	name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
	name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), blank=True,
	                           null=True)
	link = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
	url = models.ImageField(max_length=255, upload_to='uploads/upholstery/', null=True, blank=True,
	                        verbose_name=_('Image'))
	md5 = models.CharField(default=random_string(), max_length=255, editable=False)
	status_changed = MonitorField(monitor='url')

	class Meta:
		verbose_name_plural = "Upholsteries"

	def __unicode__(self):
		return u"%s" % self.name_en

	@property
	def name(self):
		return {
			'en': self.name_en,
			'fr': self.name_fr
		}

	def new_md5(self):
		if status_changed:
			self.md5 = random_string()

	def save(self, *args, **kwargs):
		if self.link and not self.url:
			result = urllib.urlretrieve(self.link)
			self.url.save(
				os.path.basename(self.link),
				File(open(result[0]))
			)
		super(Upholstery, self).save(*args, **kwargs)

	def image_thumb(self):
		if self.url.url is None:
			return '<img src="/media/%s" width="0" height="0" />' % (self.url)
		else:
			return '<img src="/media/%s" width="100" height="100" />' % (self.url)

	image_thumb.allow_tags = True

	def trims(self):
		return ",".join([str(p) for p in self.trim_set.all()])


class Wheel(models.Model):
	name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
	name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), blank=True,
	                           null=True)
	link = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
	url = models.ImageField(max_length=255, upload_to='uploads/wheel/', null=True, blank=True, verbose_name=_('Image'))
	md5 = models.CharField(default=random_string(), max_length=255)
	status_changed = MonitorField(monitor='url')

	def __unicode__(self):
		return u"%s" % self.name_en

	@property
	def name(self):
		return {
			'en': self.name_en,
			'fr': self.name_fr,
		}

	def new_md5(self):
		if status_changed:
			self.md5 = random_string()

	def save(self, *args, **kwargs):
		if self.link and not self.url:
			result = urllib.urlretrieve(self.link)
			self.url.save(
				os.path.basename(self.link),
				File(open(result[0]))
			)
		super(Wheel, self).save(*args, **kwargs)

	def image_thumb(self):
		if self.url.name is None:
			return '<img src="/media/%s" width="0" height="0" />' % (self.url)
		else:
			return '<img src="/media/%s" width="100" height="100" />' % (self.url)

	image_thumb.allow_tags = True

	def trims(self):
		return ",".join([str(p) for p in self.trim_set.all()])


class Package(models.Model):
	package_model = models.ManyToManyField('Models', blank=True)
	name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
	name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), blank=True,
	                           null=True)
	description_en = models.TextField(max_length=2000, help_text=_('English'), verbose_name=_('Description English'))
	description_fr = models.TextField(max_length=2000, help_text=_('French'), verbose_name=_('Description French'),
	                                  blank=True, null=True)
	price_override = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
	link = models.URLField(max_length=255, null=True, blank=True, verbose_name=_('OR Remote URL'))
	url = models.ImageField(max_length=255, upload_to='uploads/models/', null=True, blank=True, verbose_name=_('Image'))
	md5 = models.CharField(default=random_string(), max_length=255, editable=False)
	status_changed = MonitorField(monitor='url')
	code = models.CharField(max_length=255, verbose_name=_('Code'), blank=True, default='')
	field_type = models.CharField(max_length=255, choices=choices.TYPE, default='')

	class Meta:
		ordering = ['name_en']

	def __unicode__(self):
		return u"%s - $%s - %s" % (self.name_en, self.price_override, self.trim)

	@property
	def name(self):
		return {
			'en': self.name_en,
			'fr': self.name_fr
		}

	@property
	def description(self):
		return {
			'en': self.description_en,
			'fr': self.description_fr
		}

	def new_md5(self):
		if status_changed:
			self.md5 = random_string()

	def save(self, *args, **kwargs):
		if self.link and not self.url:
			result = urllib.urlretrieve(self.link)
			self.url.save(
				os.path.basename(self.link),
				File(open(result[0]))
			)
		super(Package, self).save(*args, **kwargs)

	def image_thumb(self):
		if self.url.name is None:
			return '<img src="/media/%s" width="0" height="0" />' % (self.url)
		else:
			return '<img src="/media/%s" width="100" height="100" />' % (self.url)

	image_thumb.allow_tags = True

	def trims(self):
		return ",".join([str(p) for p in self.trim_set.all()])

	@property
	def trim(self):
		return ",".join([str(p) for p in self.trim_set.all()])


class Option(models.Model):
	name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
	name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), blank=True,
	                           null=True)
	description_en = models.TextField(max_length=2000, help_text=_('English'), verbose_name=_('Description English'))
	description_fr = models.TextField(max_length=2000, help_text=_('French'), verbose_name=_('Description French'),
	                                  blank=True, null=True)

	def __unicode__(self):
		return u"%s" % self.name_en

	@property
	def name(self):
		return {
			'en': self.name_en,
			'fr': self.name_fr
		}

	@property
	def description(self):
		return {
			'en': self.description_en,
			'fr': self.description_fr
		}

	def trims(self):
		return ",".join([str(p) for p in self.trim_set.all()])


class Location(models.Model):
	name = models.CharField(max_length=255, verbose_name=_('City'))
	language = models.CharField(max_length=4, choices=choices.LANGUAGE_CHOICES)
	disclaimer_en = models.TextField(max_length=2000, verbose_name=_('Disclaimer English'), null=True, blank=True,
	                                 help_text=_('English'))
	disclaimer_fr = models.TextField(max_length=2000, verbose_name=_('Disclaimer French'), null=True, blank=True,
	                                 help_text=_('French'))

	@property
	def disclaimer(self):
		return {
			'en': self.disclaimer_en,
			'fr': self.disclaimer_fr
		}

	def __unicode__(self):
		return u"%s" % self.name


class Interior(models.Model):
	name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
	name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), blank=True,
	                           null=True)

	def __unicode__(self):
		return u"%s" % self.name_en

	@property
	def name(self):
		return {
			'en': self.name_en,
			'fr': self.name_fr
		}

	def trims(self):
		return ",".join([str(p) for p in self.trim_set.all()])


class Performance(models.Model):
	name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
	name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), blank=True,
	                           null=True)

	def __unicode__(self):
		return u"%s" % self.name_en

	@property
	def name(self):
		return {
			'en': self.name_en,
			'fr': self.name_fr
		}

	def trims(self):
		return ",".join([str(p) for p in self.trim_set.all()])


class Colour(models.Model):
	name_en = models.CharField(max_length=255, verbose_name=_('Name English'), help_text=_('English'))
	name_fr = models.CharField(max_length=255, verbose_name=_('Name French'), help_text=_('French'), blank=True,
	                           null=True)
	hexcode = ColorField(default='#FFFFFF')

	def __unicode__(self):
		return u"%s" % self.name_en

	@property
	def name(self):
		return {
			'en': self.name_en,
			'fr': self.name_fr
		}

	def trims(self):
		return ",".join([str(p) for p in self.trim_set.all()])


# models for forms
class Information(models.Model):
	first_name = models.CharField(max_length=100, blank=False, default='')
	last_name = models.CharField(max_length=100, blank=False, default='')
	email = models.EmailField(max_length=100, blank=False, default='')


class TestDrive(models.Model):
	form_language = models.CharField(max_length=100, blank=False, default='')
	salutation = models.CharField(max_length=100, blank=False, default='')
	first_name = models.CharField(max_length=100, blank=False, default='')
	last_name = models.CharField(max_length=100, blank=False, default='')
	contact_method = models.CharField(max_length=100, blank=False, default='')
	email = models.CharField(max_length=100, blank=True, default='')
	phone = models.CharField(max_length=100, blank=True, default='')
	purchase_intent = models.CharField(max_length=100, blank=True, default='')
	brochure = models.BooleanField()
	retailer_number = models.CharField(max_length=100, blank=False, default='')
	retailer_location = models.CharField(max_length=100, blank=True, default='')
	language = models.CharField(max_length=100, blank=False, default='')
	consent = models.BooleanField(verbose_name=_('Opt-in Email'), )
	consentB = models.BooleanField(default='', verbose_name=_('Opt-in Purchase'), )
	vehicle = models.CharField(max_length=100, blank=False, default='')
	status = models.BooleanField(default='')
	city = models.CharField(max_length=100, blank=False, default='')

	def __unicode__(self):
		return u"%s" % self.email


class KeepingInTouch(models.Model):
	form_language = models.CharField(max_length=100, blank=False, default='')
	first_name = models.CharField(max_length=100, blank=False, default='')
	last_name = models.CharField(max_length=100, blank=False, default='')
	email = models.EmailField(max_length=100, blank=False, default='')
	#    phone = models.CharField(max_length=100, blank=False, default='')
	purchaseIntent = models.CharField(max_length=100, blank=True, default='')
	preferredLanguage = models.CharField(max_length=100, blank=False, default='')
	consent = models.BooleanField()
	consentB = models.BooleanField(default='')
	status = models.BooleanField(default='')
	city = models.CharField(max_length=100, blank=False, default='')

	class Meta:
		verbose_name_plural = "Keeping in Touch"

	def __unicode__(self):
		return u"%s" % self.email


class StandAloneOption(models.Model):
	stand_alone_model = models.ManyToManyField('Models', blank=True)
	#    model_shown = models.ManyToManyField('ModelsShown', blank=True)
	code = models.CharField(max_length=255, verbose_name=_('Code'), help_text=_('English'), default='')
	title_en = models.CharField(max_length=255, verbose_name=_('Title English'), help_text=_('English'), default='')
	title_fr = models.CharField(max_length=255, verbose_name=_('Title French'), help_text=_('French'), blank=True,
	                            null=True, default='')
	price = models.CharField(max_length=255, verbose_name=_('Price'), help_text=_('Price'), blank=True, null=True,
	                         default='')

	class Meta:
		verbose_name_plural = "Stand Alone Options"

	def __unicode__(self):
		return u"%s - %s - %s - %s" % (self.title_en, self.price, self.code, self.modelss,)

	@property
	def modelss(self):
		return ", ".join([str(p) for p in self.stand_alone_model.all()])

	@property
	def title(self):
		return {
			'en': self.title_en,
			'fr': self.title_fr
		}


class OptionalEquipment(models.Model):
	optional_equipment_model = models.ManyToManyField('Models', blank=True)
	code = models.CharField(max_length=255, verbose_name=_('Code'), help_text=_('English'), default='')
	title_en = models.CharField(max_length=255, verbose_name=_('Title English'), help_text=_('English'), default='')
	title_fr = models.CharField(max_length=255, verbose_name=_('Title French'), help_text=_('French'), blank=True,
	                            null=True, default='')
	price = models.CharField(max_length=255, verbose_name=_('Price'), help_text=_('Price'), blank=True, null=True,
	                         default='')
	field_type = models.CharField(max_length=255, choices=choices.TYPE, default='')

	class Meta:
		verbose_name_plural = "Optional Equipment"

	def __unicode__(self):
		return u"%s - %s - %s - %s" % (self.title_en, self.price, self.code, self.model_optional,)

	@property
	def model_optional(self):
		return ", ".join([str(p) for p in self.optional_equipment_model.all()])

	@property
	def title(self):
		return {
			'en': self.title_en,
			'fr': self.title_fr
		}