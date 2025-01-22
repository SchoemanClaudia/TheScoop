from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    """
    Configures `reviews` app with default auto field.
    Related to `reviews` app and does not directly
    interact with other models.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'
