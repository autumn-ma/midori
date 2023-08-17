from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from itertools import chain
from midori.database_router import ShardedRouter

from .models import Page

class ListAsQuerySet(list):

    def __init__(self, *args, model, **kwargs):
        self.model = model
        super().__init__(*args, **kwargs)

    # def filter(self, *args, **kwargs):
    #     return self  # filter ignoring, but you can impl custom filter

    def order_by(self, *args, **kwargs):
        return self


class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"

class PageViewSet(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get_queryset(self):
        from django.db.models import Q

        qs_shard0 = Page.objects.using('shard0').all()
        qs_shard1 = Page.objects.using('shard1').all()
        qs_shard2 = Page.objects.using('shard2').all()
        qs_shard3 = Page.objects.using('shard3').all()
        qs_default = Page.objects.using('default').all()

        combined_qs = list(chain(qs_shard0, qs_shard1, qs_shard2, qs_shard3, qs_default))
        combined_qs = ListAsQuerySet(combined_qs, model=Page)
        return combined_qs
        
    
    @action(detail=False, methods=['get'], url_path='get_by_url/(?P<url>.+)')
    def get_by_url(self, request, url):
        print(f"get_by_url: {url}")
        shard_alias = ShardedRouter().get_shard_alias(url)[0]
        page = Page.objects.using(shard_alias).get(url=url)
        serializer = PageSerializer(page)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='get_by_hash/(?P<hash>.+)')
    def get_by_hash(self, request, hash):
        shard_alias = ShardedRouter().get_shard_alias_from_hash(hash)
        page = Page.objects.using(shard_alias).get(hash=hash)
        serializer = PageSerializer(page)
        return Response(serializer.data)
