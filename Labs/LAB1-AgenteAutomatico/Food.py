# The "Food" class
# -*- coding: utf-8 -*-
import random
global img;

class Food():
    def __init__(self, x, y, vel,pos):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 1.0
        self.maxforce = 0.01
        self.contador = 0
        self.i=pos

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)


    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading()#+PI / 2
        fill(0)
        noStroke()
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            img = loadImage("imagenes/img{}.png".format(self.i))
            image(img,0,0,28,28)

            
            # beginShape()
            # vertex(0, -self.r * 2)
            # vertex(-self.r, self.r * 2)
            # vertex(self.r, self.r * 2)
            # endShape(CLOSE)

            
    def getPosition(self):
        return self.position
    
    def collision(self):
        self.contador = self.contador + 1
        #change the food position
        #vel = PVector(0,0)
        self.position = PVector(random.randint(0,620), random.randint(0,340))
       # print("Comida: " + str(food.getContador()) )
        self.i=random.randint(1,5)
    
    
    def getContador(self):
        return self.contador
    
