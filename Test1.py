from sense_hat import SenseHat

sense = SenseHat()

while True: 
    acceleration = sense.get_acceleration_raw()
    x = acceleration['x']

    x=abs(x)
