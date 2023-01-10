from sense_hat import SenseHat

sense = SenseHat()

w = [255,255,255]
r = [255,0,0]
g = [0,255,0]
b = [0,0,255]
e = [0,0,0]

image = [
    e,e,e,e,e,e,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,g,g,e,e,e,
    e,e,e,b,b,e,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,g,g,e,e,e,
    e,e,e,b,b,e,e,e,
    e,e,e,e,e,e,e,e,

]
sense.set_pixels(image)
