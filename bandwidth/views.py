from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from bandwidth.models import Bandwidth
from bandwidth.serializers import BandwidthSerializer


class BandwidthList(generics.ListAPIView):
    queryset = Bandwidth.objects.all()
    serializer_class = BandwidthSerializer
    name = 'bandwidth-list'


class BandwidthDetail(generics.RetrieveAPIView):
    queryset = Bandwidth.objects.all()
    serializer_class = BandwidthSerializer
    name = 'bandwidth-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'bandwidth': reverse(BandwidthList.name, request=request),
        })
