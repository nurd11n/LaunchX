JAZZMIN_SETTINGS = {
    "site_header": "LaunchX",
    "site_brand": "LaunchX",
    "welcome_sign": "Welcome to the library",
    "search_model": ["auth.User"],

    "topmenu_links": [

        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        {"model": "auth.User"},

        # {"model": "apps.history.apps.Posts"},
    ],

    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    "language_chooser": True,
}