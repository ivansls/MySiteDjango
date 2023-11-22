from django.conf.urls.static import static
from django.urls import path, re_path
from ProjectSite.views import *
from mySite import settings

urlpatterns = [
    path('', indexStart, name='index'),

    #Catalog
    path('storepage/', getStorePage, name='StorePage'),
    path('feedback/', getFeedback, name='Feedback'),
    path('productwithdraw/<int:id>/', ProductWithDrawal.as_view(), name='ProductWithdraw'),
    # path('catalog/<str:a>/', getStoreCatalog, name='StoreCatalog'),
    path('catalog/', StoreCatalog.as_view(), name='StoreCatalog'),
    path('catalog/tag/<str:tag>', get_product_by_tag, name='get_by_tag'),
    path('catalog/category/<str:category>', get_product_by_category, name='get_by_category'),

    path('DeleteProduct/<int:id>', DeleteProduct.as_view(), name='deleteProduct'),

    path('addproduct/', getAddingProduct.as_view(), name='AddingProduct'),
    path('productchange/<int:id>/', UpdateProduct.as_view(), name='ProductChange' ),


    path('categorylst/', CategoryLst.as_view(), name='CategoryListView'),
    path('categorylstDet/<int:id>/', CategoryDetailView.as_view(), name='CategoryDetailView' ),

    path('categorylst/tag/', TagListView.as_view(), name='TagListView'),
    path('categorylstDet/tag/<int:id>/', TagDetailView.as_view(), name='TagDetailView' ),
    path('categorylstDet/tag/create', TagCreateView.as_view(), name='TagCreateView' ),

    #api
    path('api/', getApi, name='Api'),
    path('api/addnote/', getAddNote, name='AddNote'),
    path('api/delnote/', getDeleteNote, name='DeleteNote'),
    path('api/editnote/', getEditNote, name='EditNote'),
    path('api/readnote/', getReadNote, name='ReadNote'),

    #PersonalArea
    path('personalarea/', getPersonalAre, name='PersonalAre'),

    #shoppingcart
    path('basket/', getShopingCart, name='ShopingCart'),
    path('basket/list/', BasketListView.as_view(), name='ListShopingCart'),
    path('basket/detail/<int:id>', BasketDetailView.as_view(), name='DetailShopingCart'),
    path('basket/update/<int:id>', BasketUpdateView.as_view(), name='UpdateShopingCart'),
    path('basket/delete/<int:id>', BasketDeleteView.as_view(), name='DeleteShopingCart'),
    path('basket/create/', BasketCreateView.as_view(), name='CreateShopingCart'),

    # path('category/', category_listview.as_view())




]


