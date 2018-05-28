from urllib.parse import quote_plus

from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.utils import timezone
from django.db.models import Q

# Create your views here.
from .forms import PostForm
from .models import Post

def posts_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	# if not request.user.is_authenticated():
	# 	raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Succesfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form": form,
	}
	return render(request, 'form.html', context)

def posts_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date():
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, 'post_detail.html', context)

def posts_list(request):
	queryset_list = Post.objects.all()

	paginator = Paginator(queryset_list, 2) # Show 25 contacts per page

	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.get_page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "List",
		"page_request_var": page_request_var,
	}

	return render(request, 'post_list.html', context)

# def posts_update(request, slug=None):
# 	if not request.user.is_staff or not request.user.is_superuser:
# 		raise Http404
# 	instance = get_object_or_404(Post, slug=slug)
# 	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
# 		return HttpResponseRedirect(instance.get_absolute_url())

# 	context = {
# 		"title": instance.title,
# 		"instance": instance,
# 		"form": form,
# 	}
# 	return render(request, 'post_form.html', context)

# def posts_delete(request, slug=None):
# 	if not request.user.is_staff or not request.user.is_superuser:
# 		raise Http404
# 	instance = get_object_or_404(Post, slug=slug)
# 	instance.delete()
# 	messages.success(request, "Successfully deleted")
# 	return redirect('posts:list')