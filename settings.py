from page_controllers import Index_view, Catalog_view, Contact
from front_controllers import user_key, secret_key

ROUTES = {
    '/': Index_view(),
    '/catalog/': Catalog_view(),
    '/contact/': Contact()
}
# front controllers
FRONT_CONTROLLER = [
    user_key,
    secret_key
]
