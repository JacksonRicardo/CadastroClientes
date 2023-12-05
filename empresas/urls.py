from django.contrib import admin
from django.urls import path
from clientes import views as cliente_views

urlpatterns = [
    path('', cliente_views.home, name='home'),
    path('cliente/add/', cliente_views.ClienteCreateView.as_view(), name="add_cliente"),
    path('funcionario/add/', cliente_views.FuncionarioCreateView.as_view(), name="add_funcionario"),
    path('cliente/<int:pk>/', cliente_views.detalhes_cliente, name="detalhes_cliente"),
    path('funcionario/<int:pk>/', cliente_views.detalhes_funcionario, name="detalhes_funcionario"),
    path('cliente/<int:pk>/update/', cliente_views.ClienteUpdateView.as_view(), name="update_cliente"),
    path('cliente/<int:pk>/deleta/', cliente_views.deleta_cliente, name="deleta_cliente"),
    path('funcionario/<int:pk>/update/', cliente_views.FuncionarioUpdateView.as_view(), name="update_funcionario"),
    path('funcionario/<int:pk>/deleta/', cliente_views.deleta_funcionario, name="deleta_funcionario"),
    path('gerente/add/', cliente_views.GerenteCreateView.as_view(), name="add_gerente"),
    path('gerente/<int:pk>/update/', cliente_views.GerenteUpdateView.as_view(), name="update_gerente"),
    path('gerente/<int:pk>/', cliente_views.detalhes_gerente, name="detalhes_gerente"),  # Adicione esta linha para a visualização detalhes_gerente

    path('admin/', admin.site.urls),
]
