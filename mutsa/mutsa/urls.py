from django.contrib import admin
from django.urls import path
import lion.views
from django.conf.urls import include
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lion.views.home, name='home'),
    path('lion/<int:lion_id>/',lion.views.detail, name='detail'),
    path('lion/write/', lion.views.write, name='write'),
    path('lion/create/', lion.views.create, name='create'),
    path('accounts/', include('accounts.urls')),
   path('portfolio/', portfolio.views.portfolio, name='portfolio'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
