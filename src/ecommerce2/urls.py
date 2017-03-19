from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from carts.views import CartView, ItemCountView, CheckoutView, CheckoutFinalView
from orders.views import OrderList, OrderDetail, ChefList

urlpatterns = [
    # Examples:
    url(r'^landing/$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'ecommerce2.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'ecommerce2.views.location', name='location'),
    url(r'^failure/', 'ecommerce2.views.failure', name='failure'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include('products.urls')),
    #url(r'^$', include('products.urls')),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^orders/$', OrderList.as_view(), name='orders'),
    url(r'^orders/(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
    url(r'^cheforders/$', ChefList.as_view(), name='chef_orders'),
    url(r'^cart/count/$', ItemCountView.as_view(), name='item_count'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^checkout/final$', CheckoutFinalView.as_view(), name='checkout_final'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)