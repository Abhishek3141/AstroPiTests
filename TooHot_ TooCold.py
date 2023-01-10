from sense_hat import SenseHat

sense = SenseHat()

temperatureFloat = sense.get_temperature()

temperatureFloat = round(temperatureFloat,2)

temperatureString = str(temperatureFloat)

if temperatureFloat > 33:
    sense.show_message("It's Hot", text_colour: (255,0,0))
elif 25 < temperatureFloat <= 33:
    sense.show_message("It's Ok", text_colour: (0,255,0))
else: 
    sense.show_message("It's Cold", text_colour: (0,0,255))

