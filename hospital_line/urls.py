from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Authentication API',
        default_version='v1',
        description='Test Description'
    ),
    public=True
)



urlpatterns = [
    path('', schema_view.with_ui()),
    path('admin/', admin.site.urls),
    path('account/', include('applications.account.urls')),
    path('department/', include('applications.department.urls')),
    path('doctor/', include('applications.doctor.urls')),
    path('appointment/', include('applications.appointment.urls')),
    path('review/', include('applications.review.urls')),
    # path('', include('applications.celery.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
