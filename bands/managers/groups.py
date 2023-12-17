from crum import get_current_user
from django.db import models
from django.db.models import Q


class GroupManager(models.Manager):
    def my_groups(self):
        user = get_current_user()
        return self.filter(
            Q(band__leader=user)
            | Q(band__participants=user)
        )

    def my_groups_admin(self):
        user = get_current_user()
        return self.filter(
            Q(band__leader=user)
            | Q(manager__user=user)
        )
