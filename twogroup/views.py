from django.shortcuts import render
from django.db.models import Q

from tovar.models import Product		
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from podarok.models import Post


def home(request):
	# query = request.GET.get("q")
	queryset_list = Post.objects.all().order_by("id")
	context = {
		'object_list': queryset_list,
	}
	return render(request, 'index.html', context)
	# queryset_list = Product.objects.all()
	# queryset_list = queryset_list.filter(Q(title__icontains=query)|
	# 																		 Q(post__icontains=query)
	# 																		).distinct()

	# paginator = Paginator(queryset_list, 4) # Show 4 contacts per page

	# page_request_var = "page"
	# page = request.GET.get(page_request_var)
	# try:
	# 	queryset = paginator.get_page(page)
	# except PageNotAnInteger:
	# 	queryset = paginator.page(1)
	# except EmptyPage:
	# 	queryset = paginator.page(paginator.num_pages)

	# context = {
	# 	"object_list": queryset,
	# 	"title": "Найденные записи по запросу: ", #+ query,
	# 	"page_request_var": page_request_var,
	# }

	# return render(request, 'twogroup/tovar_list.html', context)

def about(request):
	return render(request, 'twogroup/about.html')

def contact(request):
	return render(request, 'twogroup/contact.html')

def tovars(request):
	queryset_list = Product.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(Q(title__icontains=query)|
																				 Q(content__icontains=query)
																				).distinct()

	paginator = Paginator(queryset_list, 4) # Show 4 contacts per page

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
		"title": "Найденные записи по запросу: ", #+ query,
		"page_request_var": page_request_var,
	}

	return render(request, 'twogroup/tovar_list.html', context)
