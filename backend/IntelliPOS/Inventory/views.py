import string
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#import business logic and class

import Inventory.models as Models

import Inventory.mySerializer as Serializer
# Create your views here.


@csrf_exempt 
def BrandsApi(request, id = ''):
    if request.method == 'GET':
        if id == '':
            brands = Models.Brands.objects.all()
        else:
            brands = Models.Brands.objects.filter(BId = id)
        brands_serializer = Serializer.BrandSerializer(brands, many = True)
        return JsonResponse(brands_serializer.data, safe=False)
    elif request.method == 'POST':
        brands_data = JSONParser().parse(request)
        brands_Serializer = Serializer.BrandSerializer(data=brands_data)
        if brands_Serializer.is_valid():
            brands_Serializer.save()
            return JsonResponse('Data Added Succesfully!', safe=False)
        return JsonResponse('Failed To Add Data!',safe=False)
    elif request.method == 'PUT':
        brands_data = JSONParser().parse(request)
        brands = Models.Brands.objects.get(BId = brands_data['BId'])
        brands_serializer = Serializer.BrandSerializer(brands, data = brands_data)
        if brands_serializer.is_valid():
            return JsonResponse('Data Updated Successfully!', safe = False)
        return JsonResponse('Failed To Update Data!', safe = False)
    elif request.method == 'DELETE':
        brands = Models.Brands.objects.get(BId = id)
        brands.delete()
        return JsonResponse('Data Deleted Successfully!', safe = False)

@csrf_exempt 
def CategoryApi(request, id = ''):
    if request.method == 'GET':
        #category = Models.Category.objects.all()
        
        if id == '':
            #return JsonResponse('In IF', safe=False)
            category = Models.Category.objects.all()
        else:
            #return JsonResponse('In ELSE' + id, safe=False)
            category = Models.Category.objects.filter(CId = id)
        
        category_serializer = Serializer.CategorySerializer(category, many = True)
        return JsonResponse(category_serializer.data, safe=False)
    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_Serializer = Serializer.CategorySerializer(data=category_data)
        if category_Serializer.is_valid():
            category_Serializer.save()
            return JsonResponse('Data Added Succesfully!', safe=False)
        return JsonResponse('Failed To Add Data!',safe=False)
    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category = Models.Category.objects.get(CId = category_data['CId'])
        category_Serializer = Serializer.CategorySerializer(category, data = category_data)
        if category_Serializer.is_valid():
            return JsonResponse('Data Updated Successfully!', safe = False)
        return JsonResponse('Failed To Update Data!', safe = False)
    elif request.method == 'DELETE':
        category = Models.Category.objects.get(CId = id)
        category.delete()
        return JsonResponse('Data Deleted Successfully!', safe = False)

@csrf_exempt 
def ItemSetupApi(request, id = ''):
    if request.method == 'GET':
        #res
        #res= business Instance method recall
        #return res;
        #inside buseinss logics class -> relvant method-> import dbModule -> singnature passed ->will return result
        if id == '':
            myInvItems = Models.ItemSetup.objects.all()
        else:
            myInvItems = Models.ItemSetup.objects.filter(ItemId = id) 
        myInvItems_Serializer = Serializer.ItemSetupSerializer(myInvItems, many = True)
        return JsonResponse(myInvItems_Serializer.data, safe=False)
    elif request.method == 'POST':
        myInvItems_data = JSONParser().parse(request)
        myInvItems_Serializer = Serializer.ItemSetupSerializer(data=myInvItems_data)
        if myInvItems_Serializer.is_valid():
            myInvItems_Serializer.save()
            return JsonResponse('Data Added Succesfully!', safe=False)
        return JsonResponse('Failed To Add Data!',safe=False)
    elif request.method == 'PUT':
        itemSetup_data = JSONParser().parse(request)
        itemSetup = Models.ItemSetup.objects.get(ItemId = itemSetup_data['ItemId'])
        itemSetup_serializer = Serializer.ItemSetupSerializer(itemSetup, data = itemSetup_data)
        if itemSetup_serializer.is_valid():
            return JsonResponse('Data Updated Successfully!', safe = False)
        return JsonResponse('Failed To Update Data!', safe = False)
    elif request.method == 'DELETE':
        itemSetup = Models.ItemSetup.objects.get(ItemId = id)
        itemSetup.delete()
        return JsonResponse('Data Deleted Successfully!', safe = False)
        
@csrf_exempt 
def OpeningApi(request, id = ''):
    if request.method == 'GET':
        if id == '':
            opening = Models.Opening.objects.all()
        else:
            opening = Models.Opening.objects.filter(OPId = id)
        opening_serializer = Serializer.OpeningSerializer(opening, many = True)
        return JsonResponse(opening_serializer.data, safe=False)
    elif request.method == 'POST':
        opening_data = JSONParser().parse(request)
        opening_serializer = Serializer.OpeningSerializer(data=opening_data)
        if opening_serializer.is_valid():
            opening_serializer.save()
            return JsonResponse('Data Added Succesfully!', safe=False)
        return JsonResponse('Failed To Add Data!',safe=False)
    elif request.method == 'PUT':
        opening_data = JSONParser().parse(request)
        opening = Models.Opening.objects.get(OPId = opening_data['OPId'])
        opening_serializer = Serializer.OpeningSerializer(opening_data, data = opening_data)
        if opening_serializer.is_valid():
            return JsonResponse('Data Updated Successfully!', safe = False)
        return JsonResponse('Failed To Update Data!', safe = False)
    elif request.method == 'DELETE':
        opening = Models.Opening.objects.get(OPId = id)
        opening.delete()
        return JsonResponse('Data Deleted Successfully!', safe = False)

@csrf_exempt 
def PurchaseApi(request, id = ''):
    if request.method == 'GET':
        if id == '':
            purchase = Models.Purchase.objects.all()
        else:
            purchase = Models.Purchase.objects.filter(PId = id)
        purchase_serializer = Serializer.PurchaseSerializer(purchase, many = True)
        return JsonResponse(purchase_serializer.data, safe=False)
    elif request.method == 'POST':
        purchase_data = JSONParser().parse(request)
        purchase_Serializer = Serializer.PurchaseSerializer(data=purchase_data)
        if purchase_Serializer.is_valid():
            purchase_Serializer.save()
            return JsonResponse('Data Added Succesfully!', safe=False)
        return JsonResponse('Failed To Add Data!',safe=False)
    elif request.method == 'PUT':
        purchase_data = JSONParser().parse(request)
        purchase = Models.Purchase.objects.get(PId = purchase_data['PId'])
        purchase_Serializer = Serializer.PurchaseSerializer(purchase, data = purchase_data)
        if purchase_Serializer.is_valid():
            return JsonResponse('Data Updated Successfully!', safe = False)
        return JsonResponse('Failed To Update Data!', safe = False)
    elif request.method == 'DELETE':
        purchase = Models.Purchase.objects.get(PId = id)
        purchase.delete()
        return JsonResponse('Data Deleted Successfully!', safe = False)

@csrf_exempt
def StockApi(request, id = ''):
    if request.method == 'GET':
        if id == '':
            stock = Models.Stock.objects.all()
        else:
            stock = Models.Stock.objects.filter(SId = id)
        stock_serializer = Serializer.StockSerializer(stock, many = True)
        return JsonResponse(stock_serializer.data, safe=False)
    elif request.method == 'POST':
        stock_data = JSONParser().parse(request)
        stock_Serializer = Serializer.StockSerializer(data=stock_data)
        if stock_Serializer.is_valid():
            stock_Serializer.save()
            return JsonResponse('Data Added Succesfully!', safe=False)
        return JsonResponse('Failed To Add Data!',safe=False)
    elif request.method == 'PUT':
        stock_data = JSONParser().parse(request)
        stock = Models.Stock.objects.get(SId = stock_data['SId'])
        stock_Serializer = Serializer.StockSerializer(stock, data = stock_data)
        if stock_Serializer.is_valid():
            return JsonResponse('Data Updated Successfully!', safe = False)
        return JsonResponse('Failed To Update Data!', safe = False)
    elif request.method == 'DELETE':
        stock = Models.Stock.objects.get(SId = id)
        stock.delete()
        return JsonResponse('Data Deleted Successfully!', safe = False)
