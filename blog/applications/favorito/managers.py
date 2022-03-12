from django.db import models

class FavoriteManager(models.Manager):

    def entradas_user(self, user):
        return self.filter(user = user, entry__public = True).order_by('-created')