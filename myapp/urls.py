from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from . import views
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',views.register,name='register'),
    path('transactions/',views.Transactionlistcreateview.as_view()),
    path('transactions/<str:username>/',views.Transactionupdateretrieveview.as_view()),
     path('transactions/<str:username>/<str:date>/',views.Transactionlistview.as_view()),
     #path('transactions/<str:username>/',views.TransactionListusername.as_view()),
]
    #path('categories/'),
    #path('budget/'),

