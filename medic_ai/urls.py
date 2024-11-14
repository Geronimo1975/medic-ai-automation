from django.urls import path, include

urlpatterns = [
    path('medical/', include('medical.urls')),  # Include rutele din aplicația `medical`
    # alte rute globale...
]
