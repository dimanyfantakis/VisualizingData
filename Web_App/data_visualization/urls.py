from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='visualizing_data_home'),
    path('info/', views.info, name='visualizing_data_info'),
    path('lineTest/', views.line_graph, name='visualizing_data_graph_test'),
    path('barTest/', views.bar_graph, name='visualizing_data_graph_test'),
    path('scatterTest/', views.scatter_graph, name='visualizing_data_graph_test')
]
