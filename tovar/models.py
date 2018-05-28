from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from django.utils.text import slugify
from django.db.models.signals import pre_save

class Product(models.Model):
		categorie_id = models.IntegerField(default=0)
		title = models.CharField(max_length=120)
		post = models.TextField()
		slug = models.SlugField(unique=True, null=True, blank=True)
		image = models.ImageField(blank=True, upload_to='images/', help_text='300x240px', verbose_name='Ссылка картинки')
		rating = models.IntegerField(default=0)
		date = models.DateTimeField()

		def __str__(self): 
			return self.title

		@property
		def get_content_type(self):
			instance = self
			content_type = ContentType.objects.get_for_model(instance.__class__)
			return content_type

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title, allow_unicode=True)
	if new_slug is not None:
		slug = new_slug
	qs = Product.objects.filter(slug=slug).order_by('-id')
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Product)