
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Patient
from .serializers import PatientSerializer

class PatientViewset(APIView):
    
    def get(self, request, format=None):
        Ndata = Patient.objects.all()
        serializer = PatientSerializer(Ndata, many=True)
        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class PatientDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Ndata = self.get_object(pk)
        serializer = PatientSerializer(Ndata)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Ndata = self.get_object(pk)
        serializer = PatientSerializer(Ndata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        Ndata = self.get_object(pk)
        print(Ndata)
        serializer = PatientSerializer(Ndata, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Ndata = self.get_object(pk)
        Ndata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    
