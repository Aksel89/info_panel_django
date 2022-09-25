from django.urls import path

from .views import *

urlpatterns = [
    path('', Index, name='home'),
    path('index_eng/', index_eng, name='index_eng'),
    path('lessons/', lessons, name='lessons'),
    path('mappesh/', mappesh, name='mappesh'),
    path('mappesh_eng/', mappesh_eng, name='mappesh_eng'),
    path('metro/', metro, name='metro'),
    path('metro_eng/', metro_eng, name='metro_eng'),
    path('partners/', partners, name='partners'),
    path('sale/', sale, name='sale'),
    path('taxi/', taxi, name='taxi'),
    path('taxi_eng/', taxi_eng, name='taxi_eng'),
    path('lessons/den_rojdenya/', den_rojdenya, name='den_rojdenya'),
    path('lessons/jivie_uroki/', jivie_uroki, name='jivie_uroki'),
    path('lessons/jivie_uroki/dostoprim/', dostoprim, name='dostoprim'),
    path('lessons/jivie_uroki/atlasprofessiy/', atlas_professiy, name='atlas'),
    path('lessons/jivie_uroki/kak_eto_sdelano/', kak_eto_sdelano, name='kak_eto_sdelano'),
    path('lessons/kvesti/', kvesti, name='kvesti'),
]
