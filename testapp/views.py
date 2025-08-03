from django.shortcuts import render
house = house.objects.get(my="kumkum")
room = house.room.all()  # Access books using the related_name

for room in rooms:
    print(f"{room.title} by {room.furniture}")


# Create your views here.
