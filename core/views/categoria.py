from rest_framework.viewsets import ModelViewSet

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #permission_classes = [IsAuthenticated]