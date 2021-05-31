from django.urls import path
from . import views
from .login_required.auth import auth_middleware

app_name = 'store'

urlpatterns = [
    path('',views.homefunc,name='home'),
    path('signup/',views.signupfunc,name='signup'),
    path('menu/',views.menufunc,name='menu'),
    path('login/',views.loginfunc,name='login'),
    path('logout/',views.logoutfunc,name='logout'),
    path('about/',views.aboutfunc,name='about'),
    path('gallery/',views.galleryfunc,name='gallery'),
    path('contactus/',views.contactusfunc,name='contactus'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.Checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('search/',views.search,name='itemsearch'),
    path('visualize/',views.visualize,name='visualize'),
    path('optimize/',views.optimize,name='optimize'),
    path('pay/', views.payment, name='pay'),
    path('rsearch/',views.search_product,name='search'),
    path('rpay/', views.Roompayment, name='roompay'),
    path('rcheck/', views.roomcheckout, name='roomcheck'),
    path('rorders/', views.roomorders, name='roomorders'),
    path('rooms/', views.room, name='rooms'),
    path('roomcart/',views.roomcart,name='roomcart'),
    
    path('menu/<slug:menu_slug>/',views.categorymenufunc,name='categorymenu'),
    path('<slug:item_slug>/',views.eachitemfunc,name='eachitem')
]