from .models import Source


def sidebar_sources(request):
    """Add the authenticated user's sources (with prefetched units)
    to every template context."""
    if request.user.is_authenticated:
        # `prefetch_related` used to reduce the number of queries
        # avoids N+1: one query per Source without this
        sources = (
            Source.objects
            .filter(user=request.user)
            .prefetch_related("units")
        )
    else:
        # none() used to return an empty queryset, not a list,
        # so sources stays type-consistent whether the user is
        # authenticated or not
        sources = Source.objects.none()
    return {"sidebar_sources": sources}
