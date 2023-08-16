from django.shortcuts import render , redirect;
from . import dataStore;

DB = dataStore.getMenu()

 
def getItem(key,id):
    targetList = DB[key]
    for index,item in enumerate(targetList):
        if item["id"]==id:
            return item
    return None


def getIndex(key,id):
    targetList = DB[key]
    for index,item in enumerate(targetList):
        if item["id"]==id:
            return index
    return None

def homePage(request):
    return render(request ,"menu/base.html")



def dish_list(request):
    menu = DB['menu']
    return render(request,"menu/dishList.html",{"dishes":menu})


def dish_detail(request, dish_id):
    dish = getItem('menu',dish_id)
    return render(request, 'menu/dishDetail.html', {'dish': dish})


def add_dish(request):
    if request.method == 'POST':
        dishName = request.POST.get("dishName")
        length = len(DB["menu"])
        if length==0:
            id = 1
        else:
            lastItemId = DB['menu'][length-1]["id"]
            id  = lastItemId+1
        dishPrice = request.POST.get("price");
        stock = request.POST.get("stock")
        newDish = {"id":int(id),"dishName":dishName,"price":int(dishPrice),"stock":int(stock)}
        DB['menu'].append(newDish);
        dataStore.write(DB)
        return redirect('dish_list')
    return render(request, 'menu/addDish.html')


def update_dish(request, dish_id):
    dish = getItem('menu',dish_id)
    if request.method == 'POST':
        dishName = request.POST.get("dishName")
        length = len(DB["menu"])
        if length==0:
            id = 1
        else:
            lastItemId = DB['menu'][length-1]["id"]
            id  = lastItemId+1
        dishPrice = request.POST.get("price");
        stock = request.POST.get("stock")
        updatedDish = {"id":int(id),"dishName":dishName,"price":int(dishPrice),"stock":int(stock)}
        index = getIndex('menu',dish_id)
        DB['menu'][index] = updatedDish
        dataStore.write(DB);
        return redirect('dish_list')
    return render(request, 'menu/updateDish.html', {'dish': dish})



def delete_dish(request, dish_id):
    dish = getItem('menu',dish_id)
    if request.method == 'POST':
        # Delete the dish
        return redirect('dish_list')
    return render(request, 'menu/deleteDish.html', {'dish': dish})

