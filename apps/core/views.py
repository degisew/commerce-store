from rest_framework.viewsets import ModelViewSet


class AbstractModelViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]

    # def destroy(self, request, *args, **kwargs):
    #     """
    #     Soft delete data records.
    #     """

    #     instance = self.get_object()
    #     instance.object_state = DataLookup.objects.get(
    #         value=ObjectStateType.DELETED.value
    #     )
    #     instance.deleted_at = timezone.now()
    #     instance.save()

    #     return Response(status=status.HTTP_204_NO_CONTENT)
