from django.urls import path
from app import views

urlpatterns = [
	path('', views.allMateriels),
	path('add', views.addMateriel),
	path('<num>/update', views.updateMateriel),
	path('<num>/delete', views.deleteMateriel)
]