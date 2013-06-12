from django.db import models


class CurrencyManager(models.Manager):
    """
    Custom manager for Currency model.
    """

    def get_query_set(self):
        return super(CurrencyManager, self).get_query_set()

    def active(self):
        return self.get_query_set().filter(is_active=True)

    def base(self):
        return self.get_query_set().get(is_base=True)

    def default(self):
        return self.get_query_set().get(is_default=True)