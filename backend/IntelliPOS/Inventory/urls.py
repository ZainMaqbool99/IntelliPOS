from django.urls import path
import Inventory.views as Views


urlpatterns = [

    path('Category', Views.CategoryApi),
    path('Category/<str:id>', Views.CategoryApi),

    path('Brands', Views.BrandsApi),
    path('Brands/<str:id>', Views.BrandsApi),

    path('ItemSetup', Views.ItemSetupApi),
    path('ItemSetup/<str:id>', Views.ItemSetupApi),

    path('Opening', Views.OpeningApi),
    path('Opening/<str:id>', Views.OpeningApi),

    path('Purchase$', Views.PurchaseApi),
    path('^Purchase/<str:id>', Views.PurchaseApi),

    path('Stock', Views.StockApi),
    path('Stock/<str:id>', Views.StockApi)
]