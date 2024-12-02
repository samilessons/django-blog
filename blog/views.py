from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

data_from_db = [
	{
		"id": 1,
		"title": "CSTO should not have fought for Yerevan in Karabakh, Putin says",
		"is_published": True,
		"content": """
			The Collective Security Treaty Organization (CSTO) should not have fought for Yerevan in Karabakh; in this case,
			there was no external aggression against Armenia, Russian President Vladimir Putin said, TASS reports. Also,
			the Russian president did not rule out that Armenia will return to full-time work within the CSTO.
			He added that Armenia has not yet announced its withdrawal from the CSTO and supports all the
			documents of the summit of this organization.
		"""
	},
	{
		"id": 2,
		"title": "US dollar still rising in Armenia",
		"is_published": False,
		"content": """
			The American dollar’s (USD) exchange rate against the Armenian dram (AMD) comprised AMD 392.97/$1 in Armenia
			on Thursday;
		"""
	},
	{
		"id": 3,
		"title": "Ameriabank Named Armenia’s Best Bank for Real Estate by Euromoney",
		"is_published": True,
		"content": """
			<span style="color: red"> Ameriabank </span> has been recognized as Armenia’s best bank for real estate by an international financial publication
			Euromoney, becoming the first-ever recipient of this award in Armenia.
			The Real Estate Awards honor excellence in
			
			the commercial real estate sector, acknowledging not only financial success and client service,
			but also a
			
			commitment to improving the sector through technological advances and sustainability initiatives
		"""
	}
]

categories_from_db = [
	{"id": 1, "name": "Traveling"},
	{"id": 2, "name": "Sport"},
	{"id": 3, "name": "IT & Development"},
	{"id": 4, "name": "Cars"},
	{"id": 5, "name": "Fashion"},
]


def index(request):
	data = {
		"title": "Home Page",
		"description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
		"posts": data_from_db,
		"cat_selected": 0
	}
	return render(request, "blog/home.html", data)


def about(request):
	return render(request, "blog/about.html", {"title": "About Page"})


def show_more(request, post_id):
	return render(request, "blog/read-more.html", {"title": "Read More"})


def show_category(request, cat_id):
	return render(
		request,
		"blog/category.html",
		{
			"title": categories_from_db[cat_id - 1].get("name"),
			"cat_selected": cat_id
		},
	)


def add_post(request):
	return render(request, "blog/add-post.html", {"title": "Add Post"})


def contacts(request):
	return render(request, "blog/contacts.html", {"title": "Contacts"})


def login(request):
	return render(request, "blog/login.html", {"title": "Login"})


def page_not_found(request, exception):
	return HttpResponseNotFound(f"<h1> Page Not Found 404 </h1>")
