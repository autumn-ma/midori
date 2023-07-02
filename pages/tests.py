from django.test import TestCase
from midori.sharding_utils import get_next_auto_id_across_shard
from pages.models import Page

class ShardingUtilsTestCase(TestCase):
    def setUp(self) -> None:
        Page.objects.create(url="https://www.google.com", title="Google", descirption="Google", hash="hash", blob_ref="blob_ref", priority=0)

    def test_get_next_auto_id_across_shard(self):
        print(Page.objects.all())
        next_value = get_next_auto_id_across_shard(Page._meta.db_table)
        self.assertEqual(next_value, 1)