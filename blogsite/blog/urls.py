from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.BlogsListView.as_view()),  name='blogs'),
    # url(r'^partial-list$', views.PlayersListPartialView.as_view(),  name='partial-players-list'),
    # # url(r'^$', views.PlayersListView.as_view(), name='player_detail'),
    # url(r'^(?P<pk>[-\w]+)/$', views.player_detail_view, name='player-detail')
]
