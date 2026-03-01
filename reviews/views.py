from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Review
from .serializers import ReviewSerializer
class PropertyReviewsView(APIView):
    permission_classes=[permissions.AllowAny]
    def get(self, request, version, property_id):
        qs=Review.objects.filter(property_id=property_id).order_by('-created_at')
        page=int(request.query_params.get('page',1)); size=int(request.query_params.get('page_size',20))
        start=(page-1)*size; end=start+size
        return Response({'count':qs.count(),'results':ReviewSerializer(qs[start:end], many=True).data})
class CreateReviewView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self, request, version, property_id):
        s=ReviewSerializer(data=request.data); s.is_valid(raise_exception=True)
        r=Review.objects.create(property_id=property_id, user=request.user,
                                rating=s.validated_data['rating'], content=s.validated_data.get('content',''))
        return Response(ReviewSerializer(r).data, status=status.HTTP_201_CREATED)

class ReviewDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, version, pk):
        try: r=Review.objects.get(pk=pk)
        except Review.DoesNotExist: return Response({'detail':'Not found'}, status=404)
        return Response(ReviewSerializer(r).data)
    def put(self, request, version, pk):
        r=Review.objects.get(pk=pk)
        if r.user != request.user: return Response({'detail':'Permission denied'}, status=403)
        s=ReviewSerializer(r, data=request.data)
        s.is_valid(raise_exception=True); s.save(); return Response(s.data)
    def patch(self, request, version, pk):
        r=Review.objects.get(pk=pk)
        if r.user != request.user: return Response({'detail':'Permission denied'}, status=403)
        s=ReviewSerializer(r, data=request.data, partial=True)
        s.is_valid(raise_exception=True); s.save(); return Response(s.data)
    def delete(self, request, version, pk):
        r=Review.objects.get(pk=pk)
        if r.user != request.user: return Response({'detail':'Permission denied'}, status=403)
        r.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
