from django.http import JsonResponse,HttpResponse
from .models import Dish

# Create your views here.


def dish_list(request):
    dishes = Dish.objects.all()
    dish_data = [{'id': dish.id, 'dish_name': dish.dish_name, 'price': dish.price} for dish in dishes]
    return JsonResponse(dish_data, safe=False)

def add_dish(request):
    if request.method == 'POST':
        dish_name = request.POST.get('dish_name')
        price = request.POST.get('price')
        Dish.objects.create(dish_name=dish_name, price=price)
        return JsonResponse({'message': 'Dish added successfully'})
    return JsonResponse({'message': 'Method not allowed'}, status=405)


def home(request):
    return HttpResponse("<h1>Welcome to Zesty Zomato</h1>")

