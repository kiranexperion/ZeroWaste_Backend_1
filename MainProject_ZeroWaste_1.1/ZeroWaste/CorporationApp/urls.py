from .import views
from django.urls import path

urlpatterns = [
    path('wastelist/',views.getWastes,name = 'wastes'),
    path('corporation/login',views.postCorporationlogin,name='login'),
    path('corporation/logout',views.postLogoutView,name='logout'),
    # path('corporation/bookingreport',views.postBookingReport,name='bookingreport'),
    path('corporation/bookingreport',views.getBookingReport,name='bookingreport'),
    path('corporation/wastelistupdate/',views.editWasteList,name='editwaste'),
    path('corporation/addwastetype',views.postAddWaste,name='postAddWaste'),
    path('corporation/deletewastetype',views.postDeleteWaste,name='postDeleteWaste'),

]