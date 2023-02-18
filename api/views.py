from rest_framework import generics,mixins,viewsets,status
from .models import (User,Trending,Place,Activities,Guide,Item,Festival,Purchase,Attraction,Booking,GuideDetail)
from .serializers import (UserSerializer,RegisterSerializer,TrendingSerializer,PlaceSerializer,ActivitiesSerializer,
                          FestivalSerializer,ItemSerializer,GuideSerializer,PurchaseSerializer,AttractionSerializer,BookingSerializer,
                          GuideSerializer)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response

# Create your views here.
class ActivitiesView(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=ActivitiesSerializer
    queryset=Activities.objects.all()

class PlaceView(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=PlaceSerializer
    queryset=Place.objects.all()

class TrendingViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=TrendingSerializer
    queryset=Trending.objects.all()

class RegisterView(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=RegisterSerializer
    queryset=User.objects.all()

class FestivalViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=FestivalSerializer
    queryset=Festival.objects.all()

class ItemViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=ItemSerializer
    queryset=Item.objects.all()

class GuideViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=GuideSerializer
    queryset=Guide.objects.all()

class PurchaseViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin):
    permission_classes=[IsAuthenticated]
    serializer_class=PurchaseSerializer
    queryset=Purchase.objects.all()

class AttractionViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=AttractionSerializer
    queryset=Attraction.objects.all()

class BookingViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin):
    permission_classes=[IsAuthenticated]
    serializer_class= BookingSerializer
    queryset=Booking.objects.all()

class GuideDetailViewset(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=GuideSerializer
    queryset=GuideDetail.objects.all()
    

class BlacklistTokenView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            refresh_token=request.data["refresh_token"]
            token=RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class LoggedInUserView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)