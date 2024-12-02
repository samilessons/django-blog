def menu_context(request):
	return {
		"menu": [
			{
				"link_title": "About Site",
				"link_url": "about"
			},
			{
				"link_title": "Add Post",
				"link_url": "add_post"
			},
			{
				"link_title": "Contacts",
				"link_url": "contacts"
			},
			{
				"link_title": "Login",
				"link_url": "login"
			},
		],
	}