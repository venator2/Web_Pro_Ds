from django.apps import AppConfig

class MyShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_shop'

    def ready(self):
        import my_shop.signals
