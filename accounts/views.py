from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from accounts import models
from accounts.serializers import ClientSerializer,FileUploadSerializer
import io, csv, pandas as pd
from rest_framework import status
from accounts.filters import ClientFilter


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer


    def post(self, request, *args, **kwargs):
        chunksize = 10 ** 3
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        my_list = []
        for chunk in pd.read_csv(file, chunksize=chunksize):
            df = chunk.reset_index()
            for index, row in df.iterrows():
                new_file = models.Client(
                            name = row['name'],
                            created_at = row['created_at'],
                            updated_at = row['updated_at']
                )
                my_list.append(new_file)
                if len(my_list) > 20000:
                     models.Client.objects.bulk_create(my_list)
                     my_list = []
        models.Client.objects.bulk_create(my_list)
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)


class ClientViewset(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = ClientSerializer
    filter_class = ClientFilter
