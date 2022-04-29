# -*- coding: utf-8 -*-
# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# The "Vehicle" class
global img2
class Vehicle():
    def __init__(self, x, y, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 5
        self.maxforce = 0.2

    # Método para actualizar la ubicación
    def update(self):
        # actualizar velocidad
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)
        

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)



    # Un método que calcula una fuerza de dirección hacia un objetivo
    # STEER = VELOCIDAD MENOS DESEADA
    def arrive(self, target):

        # Un vector que apunta desde la ubicación hasta el objetivo.
        desired = target - self.position
        d = desired.mag()

        # Escala con amortiguación arbitraria dentro de 100 píxeles
        if (d < 100):
            m = map(d, 0, 100, 0, self.maxspeed)
            desired.setMag(m)
        else:
            desired.setMag(self.maxspeed)

        # Steering = Desired minus velocity
        steer = desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)



    def boundaries(self, d):

        desired = None

        if self.position.x < d:
            desired = PVector(self.maxspeed, self.velocity.y)
        elif self.position.x > width - d:
            desired = PVector(-self.maxspeed, self.velocity.y)

        if self.position.y < d:
            desired = PVector(self.velocity.x, self.maxspeed)
        elif self.position.y > height - d:
            desired = PVector(self.velocity.x, -self.maxspeed)

        if desired:
            desired.normalize()
            desired.mult(self.maxspeed)
            steer = desired - self.velocity
            steer.limit(self.maxforce)
            self.applyForce(steer)
            
            
            
    def display(self):
        # Dibuja un triángulo girado en la dirección de la velocidad.
        theta = self.velocity.heading() + PI / 2
        fill(0,0,0)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            #size(640, 360)
            img2 = loadImage("imagenes/robot6.png")
            image(img2,0,0,40,40)
            
            
    def getPosition(self):
        return self.position
    
    
