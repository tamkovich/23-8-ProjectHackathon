from django.shortcuts import render
from kategor.models import Categories
from tovar.models import Product
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from comments.forms import CommentForm


def spec_prod(request,cat_slug, slug):
		prod = Product.objects.get(slug=slug)
		cat = Categories.objects.get(slug=cat_slug)
		cat_title = cat.title
		content_type = ContentType.objects.get_for_model(Product)
		tid = prod.id
		comments = Comment.objects.filter(content_type=content_type, object_id=tid)
		# cat_id = cat.id

		initial_data = {
			"content_type": prod.get_content_type,
			"object_id": prod.id
		}
		form = CommentForm(request.POST or None, initial=initial_data)
		if form.is_valid():
			c_type = form.cleaned_data.get("content_type")
			content_type = ContentType.objects.get(model=c_type)
			obj_id = form.cleaned_data.get("object_id")
			content_data = form.cleaned_data.get("content")
			new_comment, created = Comment.objects.get_or_create(
																		user = request.user, 
																		content_type = content_type,
																		object_id = obj_id,
																		content = content_data
																)

		context = {
			"cat_title": cat_title, 
			"cat_slug": cat_slug, 
			"prod": prod,
			'comments': comments,
			'comment_form': form
		}
		return render(request, "kategor/tovar.html", context)
