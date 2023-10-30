from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('employees_app.employees.urls')),
                  path('templates/', include('employees_app.template_examples.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
