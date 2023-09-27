from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

# str - любая непустая строка без слеша
# int - только числа
# slug - буквы, цифры, дефисы
# uuid - цифры, маленькие латинские символы ascii + дефис
# path - любая непустая строка

urlpatterns = [
    path('', BlogHome.as_view(), name='index'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('contacts/', ContactFormView.as_view(), name='contacts'),
]
