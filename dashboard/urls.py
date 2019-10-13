from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import dashboard, dashboard_orders, dashboard_order_details, confirm_delete_product, add_a_product, add_a_category
from products.views import toggle_status
from charts import urls as urls_charts

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboardorders', views.dashboard_orders, name='dashboard_orders'),
    path('dashboardorder/<int:id>', views.dashboard_order_details,
         name='dashboard_order_details'),
    path('dashboardproducts', views.dashboard_product, name='dashboard_product'),
    path('dashboardproducts/confirmdeleteproduct/<int:pk>',
         views.confirm_delete_product, name='confirm_delete_product'),
    path('dashboardaddproduct', views.add_a_product, name='add_a_product'),
    path('dashboardaddcategory', views.add_a_category, name='add_a_category'),
    path('toggle_status/<int:id>', toggle_status),
    path('charts/', include(urls_charts)),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
