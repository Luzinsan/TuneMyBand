from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAuthenticated


class IsMyBand(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if obj.leader == request.user:
            return True

        if request.method in SAFE_METHODS:
            return request.user in obj.participants.all()

        return False


class IsColleagues(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if obj.band.leader == request.user:
            return True

        if request.method in SAFE_METHODS:
            return request.user in obj.band.participants.all()
        return False


class IsMembers(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if (
            obj.group.band.leader == request.user
            or obj.group.manager.user == request.user
        ):
            return True

        if request.method in SAFE_METHODS:
            return request.user in obj.group.band.participants.all()
        return False


class IsMyGroup(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if obj.band.leader == request.user:
            return True

        if request.method in SAFE_METHODS:
            return request.user in obj.band.participants.all()

        if obj.manager.user == request.user:
            return True
        return False


class IsOfferManager(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if obj.band.leader == request.user:
            return True
        return False
