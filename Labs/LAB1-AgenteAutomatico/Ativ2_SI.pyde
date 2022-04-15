# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food
import random
import math

#random.randint()
def setup():
    global vehicle
    size(680, 390)
    velocity = PVector(1, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    global food 
    vel = PVector(0,0)
    food = Food(random.randint(0,640), random.randint(0,360), vel,2) 


def draw():
    background(231,253,255)
    mouse = PVector(mouseX, mouseY)
    #acc = PVector(1,1)
    #vehicle.applyForce(acc)
    vehicle.update()
    vehicle.display()
    food.update()
    food.display()
    #print("Comida: " + str(food.getContador()) )
    target = food.getPosition()
    vehicle.arrive(target)
    count = food.contador
    texto = "Plaga espatanda:"
    text (texto, 10,15)
    text(count, 105,15)
    if (food.getPosition().dist(vehicle.getPosition()) <= 4):
        food.collision()
