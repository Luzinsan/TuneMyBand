from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bands.views import dicts, bands, participants, groups, offers, \
    members

router = DefaultRouter()

router.register(r'dicts/positions', dicts.PositionView, 'positions')
router.register(r'search', bands.BandSearchView, 'bands-search')
router.register(r'(?P<pk>\d+)/participants', participants.ParticipantView, 'participants')
router.register(r'offers', offers.OfferUserView, 'user-offers')
router.register(r'(?P<pk>\d+)/offers', offers.OfferBandView, 'org-offers')
router.register(r'groups/(?P<pk>\d+)/members', members.MemberView, 'members')
router.register(r'groups', groups.GroupView, 'groups')
router.register(r'', bands.BandView, 'bands')

urlpatterns = [
    path('bands/', include(router.urls)),
]

