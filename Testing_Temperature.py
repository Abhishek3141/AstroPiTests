from sense_hat import SenseHat

sense = SenseHat()

temperatureFloat = sense.get_temperature()

temperatureFloat = round(temperatureFloat,2)

temperatureString = str(temperatureFloat)

sense.show_message(temperatureString)
