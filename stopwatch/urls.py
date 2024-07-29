from django.urls import path
from stopwatch.views import IndexView, StartView, PauseView, ResetView,RecordLapView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('start/', StartView.as_view(), name = 'start'),
    path('pause/', PauseView.as_view(), name = "pause"),
    path('reset/', ResetView.as_view(), name='reset'),
    path('record/', RecordLapView.as_view(), name = 'lap'),
 ]
