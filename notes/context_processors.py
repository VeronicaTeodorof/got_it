from .models import Source


def sidebar_sources(request):
    if request.user.is_authenticated:
        # `prefetch_related` used to reduce the number of queries
        # avoids N+1: one query per Source without this
        sources = (
            Source.objects
            .filter(user=request.user)
            .prefetch_related("units")
        )
    else:
        sources = Source.objects.none()
    return {"sidebar_sources": sources}
