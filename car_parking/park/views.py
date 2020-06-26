from django.http import JsonResponse
import json

ranger = 10

class ParkingArea:

    def __init__(self, slot_number):
        self.slot_number = slot_number
        self.car_number = None

    def __str__(self):
        return str({'slot': self.slot_number, 'car_number': self.car_number})


class Parking:

    def __init__(self, max_slots):
        self.slots = {str(value): ParkingArea(str(value)) for value in range(1, max_slots + 1)}
        self.car_to_slot = {}


def view_parking():
    print("car_to_slot")
    for i in parking.slots.values():
        print(i)
    print("car_to_slot")
    for i in parking.car_to_slot.values():
        print(i)


parking = Parking(ranger)


def add_car(request):
    """This Endpoint takes the car number as input and outputs the slot
where it is parked."""
    if request.method == 'POST':
        payload = json.loads(request.body)
        car_number = payload.get('car_number')
        if car_number is None:
            return JsonResponse({'Error': 'Wrong Key!'}, status=400)
        for key, value in parking.slots.items():
            if value.car_number is None:
                slot = key
                value.car_number = car_number
                parking.car_to_slot[car_number] = value
                break
        else:

            return JsonResponse({'Error': 'Parking full!', 'car_to_slot': parking.car_to_slot, 'slots': parking.slots})
        view_parking()
        a = {i: str(j) for i, j in parking.car_to_slot.items()}
        b = {i: str(j) for i, j in parking.slots.items()}
        return JsonResponse({'slot': slot, 'car_number': car_number, 'car_to_slot': a, 'slots': b})


def un_park(request):
    """This endpoint takes the slot number from which the car is to be removed
from and frees that slot up."""
    if request.method == 'POST':
        payload = json.loads(request.body)
        slot = payload.get('slot')
        if slot in parking.slots and parking.slots[slot].car_number:
            parking.slots[slot].car_number = None
        else:
            a = {i: str(j) for i, j in parking.car_to_slot.items()}
            b = {i: str(j) for i, j in parking.slots.items()}
            return JsonResponse({'Error': 'Slot invalid/Empty!', 'car_to_slot': a, 'slots': b})
        for key, value in parking.car_to_slot.items():
            if value.slot_number == slot:
                del parking.car_to_slot[key]
                break
        a = {i: str(j) for i, j in parking.car_to_slot.items()}
        b = {i: str(j) for i, j in parking.slots.items()}
        return JsonResponse({'Success': 'Car removed!', 'car_to_slot': a, 'slots': b})


def get_car(request):
    """This endpoint takes either slot number or car
number and return both the car number and slot number."""
    if request.GET.get('car_number'):
        car_number = request.GET.get('car_number')
        if car_number not in parking.car_to_slot:
            a = {i: str(j) for i, j in parking.car_to_slot.items()}
            b = {i: str(j) for i, j in parking.slots.items()}
            return JsonResponse({'Error': 'Car could not be found!', 'car_to_slot': a, 'slots': b})
        else:
            car_slot = parking.car_to_slot[car_number].slot_number
            return JsonResponse({'slot': car_slot, 'car_number': car_number})
    elif request.GET.get('slot'):
        slot = request.GET.get('slot')
        if slot not in parking.slots:
            a = {i: str(j) for i, j in parking.car_to_slot.items()}
            b = {i: str(j) for i, j in parking.slots.items()}
            return JsonResponse({'Error': 'Slot invalid/Empty!', 'car_to_slot': a, 'slots': b})
        else:
            car_number = parking.slots[slot].car_number
            a = {i: str(j) for i, j in parking.car_to_slot.items()}
            b = {i: str(j) for i, j in parking.slots.items()}
            return JsonResponse({'slot': slot, 'car_number': car_number, 'car_to_slot': a, 'slots': b})
    else:
        return JsonResponse({'Error': 'Missing or wrong parameter!'}, status=400)


