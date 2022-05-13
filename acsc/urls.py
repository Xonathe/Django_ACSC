from django.urls import path, include

urlpatterns = [
    path('', include('web_cp.urls')),
]

handler404 = "web_cp.views.page_not_found_view"
