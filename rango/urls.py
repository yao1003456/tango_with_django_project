from django.urls import path
from rango import views
from rango.views import AboutView, AddCategoryView, AddPageView, ShowCategoryView, GotoUrlView, RestrictedView, RegisterProfileView


app_name = 'rango'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("about/", views.AboutView.as_view(), name="about"),
    path('category/<slug:category_name_slug>/', views.ShowCategoryView.as_view(), name='show_category'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.AddPageView.as_view(), name='add_page'),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    path('restricted/', views.RestrictedView.as_view(), name='restricted'),
    # path('logout/', views.user_logout, name='logout'),
    # path('search/', views.search, name='search'),
    path('goto/', views.GotoUrlView.as_view(), name='goto'),
    path('register_profile/', views.RegisterProfileView.as_view(), name='register_profile'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    path('like_category/', views.LikeCategoryView.as_view(), name='like_category'),
    path('suggest/', views.CategorySuggestionView.as_view(), name='suggest'),


    ]