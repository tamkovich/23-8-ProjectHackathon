from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from kategor.models import Categories
from tovar.models import Product
from django.views.generic import CreateView
from django.core.paginator import Paginator

def all_cat(request):
		prods = Product.objects.all().order_by("id")
		cats = Categories.objects.all()
		return render(request, "kategor/categories.html", {"cats": cats, "prods": prods})

def spec_cat(request, slug):
		prods = Product.objects.all().order_by("id")
		cat = Categories.objects.get(slug=slug)

		paginator = Paginator(prods, 4) # Show 4 contacts per page

		page_request_var = "page"
		page = request.GET.get(page_request_var)
		try:
			prods = paginator.get_page(page)
		except PageNotAnInteger:
			prods = paginator.page(1)
		except EmptyPage:
			prods = paginator.page(paginator.num_pages)

		context = {
			"cat": cat,
			"prods": prods,
			"title": "List",
			"page_request_var": page_request_var,
		}

		return render(request, "kategor/categorie.html", context)