from django.db import connection, models
from django.db import transaction

from midori.database_router import ShardedRouter

class Page(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=124)
    descirption = models.TextField()

    hash = models.CharField(max_length=124, unique=True)
    blob_ref = models.CharField(max_length=124, unique=True)

    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        from midori.sharding_utils import get_or_create_id_from_global_increment_tracker, save_id_to_global_increment_tracker

        if not self.pk:
            # If it's a new Page object, determine the shard alias based on the URL
            shard_alias = ShardedRouter().get_shard_alias(self.url)
            print(shard_alias)
            using = shard_alias
            kwargs['using'] = using

            table_name = self._meta.db_table

            with transaction.atomic():
                id = get_or_create_id_from_global_increment_tracker(table_name)+1
                self.pk = id
                super().save(*args, **kwargs)
                save_id_to_global_increment_tracker(table_name, id)


class GlobalIndex(models.Model):
    hash = models.CharField(max_length=124, unique=True)
    url = models.URLField()

class GlobalIncrementTracker(models.Model):
    table_name = models.CharField(max_length=124, unique=True)
    last_id = models.IntegerField(default=0)