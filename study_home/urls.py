from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('team/', include('teacher.urls', namespace='team')),
    path('courses/', include('course.urls', namespace='courses_all')),
    path('account/', include('account.urls', namespace='account')),
    path('teacher_personal/', include('teacher_personal.urls', namespace='teacher_personal')),
    path('', include('school.urls', namespace='school')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
