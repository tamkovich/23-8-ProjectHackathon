from django.db import models
from django.conf import settings
from tovar.models import Product
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class CommentManager(models.Manager):
	def filter_by_instance(self, pk):
		content_type = ContentType.objects.get_for_model(Product)
		qs = super(CommentManager, self).filter(content_type=content_type, object_id=pk)
		return qs

class Comment(models.Model):
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	# post 			= models.ForeignKey(Product, on_delete=models.CASCADE)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	# null=True
	content_object = GenericForeignKey('content_type', 'object_id')

	content 	= models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user.username)

