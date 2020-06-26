from django.shortcuts import render
from django.http import JsonResponse
import json

ranger = 0

car_to_slot = {}
slots = {str(value): None for value in range(1, ranger + 1)}


def add_car(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        car_number = payload.get('car_number')
        if car_number is None:
            return JsonResponse({'Error': 'Wrong Key!'})
        for key, value in slots.items():
            if value is None:
                slot = key
                slots[key] = car_number
                car_to_slot[car_number] = key
                break
        else:
            return JsonResponse({'Error': 'Parking full!', 'car_to_slot': car_to_slot, 'slots': slots})
        return JsonResponse({'slot': slot, 'car_number': car_number, 'car_to_slot': car_to_slot, 'slots': slots})


def un_park(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        slot = payload.get('slot')
        if slot in slots and slots[slot]:
            slots[slot] = None
        else:
            return JsonResponse({'Error': 'Slot invalid/Empty!', 'car_to_slot': car_to_slot, 'slots': slots})
        for key, value in car_to_slot.items():
            if value == slot:
                del car_to_slot[key]
                break
        return JsonResponse({'Success': 'Car removed!', 'car_to_slot': car_to_slot, 'slots': slots})


def get_car(request):
    if request.GET.get('car_number'):
        car_number = request.GET.get('car_number')
        if car_number not in car_to_slot:
            return JsonResponse({'Error': 'Car could not be found!', 'car_to_slot': car_to_slot, 'slots': slots})
        else:
            car_slot = car_to_slot[car_number]
            return JsonResponse({'slot': car_slot, 'car_number': car_number})
    elif request.GET.get('slot'):
        slot = request.GET.get('slot')
        if slot not in slots:
            return JsonResponse({'Error': 'Slot invalid/Empty!', 'car_to_slot': car_to_slot, 'slots': slots})
        else:
            car_number = slots[slot]
            return JsonResponse({'slot': slot, 'car_number': car_number, 'car_to_slot': car_to_slot, 'slots': slots})
    else:
        return JsonResponse({'Error': 'Missing or wrong parameter!'})



