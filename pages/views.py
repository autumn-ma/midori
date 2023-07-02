from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from .models import Page

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
        print(qs_shard0)
        qs_shard1 = Page.objects.using('shard1').all()
        print(qs_shard1)
        qs_shard2 = Page.objects.using('shard2').all()
        print(qs_shard2)
        qs_shard3 = Page.objects.using('shard3').all()
        print(qs_shard3)
        qs_default = Page.objects.using('default').all()
        print(qs_default)

        combined_qs = qs_shard0.union(qs_shard1, qs_shard2, qs_shard3, qs_default)
        
        return combined_qs