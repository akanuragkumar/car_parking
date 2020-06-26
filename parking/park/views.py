from django.shortcuts import render
from django.http import JsonResponse
import json

ranger = 10
car_to_slot = {}
slots = {str(value): None for value in range(1, ranger + 1)}


def add_car(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        car_number = payload.get('car_number')
        for key, value in slots.items():
            if value is None:
                slot = key
                slots[key] = car_number
                car_to_slot[car_number] = key
                break
        return JsonResponse({'slot': slot, 'car_number': car_number, 'car_to_slot': car_to_slot, 'slots': slots})


def un_park(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        slot = payload.get('slot')
        for key, value in car_to_slot.items():
            if value == slot:
                del car_to_slot[key]
                break
        return JsonResponse({'Success': 'Car removed!', 'car_to_slot': car_to_slot, 'slots': slots})


def get_car(request):
    if request.GET.get('car_number'):
        car_number = request.GET.get('car_number')
        car_slot = car_to_slot[car_number]
        return JsonResponse({'slot': car_slot, 'car_number': car_number})
    elif request.GET.get('slot'):
        slot = request.GET.get('slot')
        car_number = slots[slot]
        return JsonResponse({'slot': slot, 'car_number': car_number,'car_to_slot': car_to_slot, 'slots': slots})

