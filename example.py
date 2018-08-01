from ultimaker3 import Ultimaker3
import time

api = Ultimaker3("192.168.137.127", "Test script")
api.loadAuth("auth.data")

# Get all the system data
system = api.get("api/v1/system").json()
print(system["name"])
# Change the system name
#result = api.put("api/v1/system/name", data="MyUltimaker3")
#print(result.json())


# Set the target hotend temperature to 100C, and then back to 0.
#print(api.get("api/v1/printer/heads/0/extruders/0/hotend/temperature").json())
#result = api.put("api/v1/printer/heads/0/extruders/0/hotend/temperature/target", data=100.0).json()
#print(api.get("api/v1/printer/heads/0/extruders/0/hotend/temperature").json())
#result = api.put("api/v1/printer/heads/0/extruders/0/hotend/temperature/target", data=0.0).json()
#print(api.get("api/v1/printer/heads/0/extruders/0/hotend/temperature").json())

# Change the LEDs
api.put("api/v1/printer/led", data={"brightness": 100.0, "saturation": 90.0, "hue": 255.0})

class leds:
    brightness = 100.0
    saturation = 90.0
    hue = 0.0

um3Leds = leds()
x = 0
y = 0

while x < 255:
    while y < 255:
        api.put("api/v1/printer/led", data={"brightness": um3Leds.brightness, "saturation": um3Leds.saturation, "hue": um3Leds.hue})
        um3Leds.hue += 10
        y += 10
        time.sleep(0.5)
    um3Leds.saturation += 10
    api.put("api/v1/printer/led", data={"brightness": um3Leds.brightness, "saturation": um3Leds.saturation, "hue": um3Leds.hue})
    x += 10
    time.sleep(0.5)
# Start a print job.
#result = api.post("api/v1/print_job", files={"file": ("UM3_Box_20x20x10.gcode", open("UM3_Box_20x20x10.gcode", "rb"))})
#print(result.content)

# Pause the print
#api.put("api/v1/print_job/state", data={"target": "pause"})

# Resume the print
#api.put("api/v1/print_job/state", data={"target": "print"})

# Abort the print
#api.put("api/v1/print_job/state", data={"target": "abort"})


# Camera can be found here http://192.168.137.127:8080/?action=stream
