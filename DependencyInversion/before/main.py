class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class ElectricPowerSwitch:

    def __init__(self, lightbulb: LightBulb):
        self.lightbulb = lightbulb
        self.on = False

    def press(self):
        if self.on:
            self.lightbulb.turn_off()
            self.on = False
            return
        self.lightbulb.turn_on()
        self.on = True


l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()
