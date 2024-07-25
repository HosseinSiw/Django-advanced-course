from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET',])
def api_post_list(request):
    return Response({"view": "api_post_list"})
