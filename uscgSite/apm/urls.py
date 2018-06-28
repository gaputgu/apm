from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^product_line/(?P<name>\w+)/$',views.product_line_view,name='product_line_view'),
    url(r'^ship_class/(?P<name>.*)/$',views.ship_class_view,name='ship_class_view'),
    url(r'^ship/(?P<name>.*)/$',views.ship_instance_view,name='ship_instance_view'),
    url(r'^maintenance_item/(?P<title>.*)/$',views.maintenance_item_view,name='maintenance_item_view'),
]
