import network
import machine
import webrepl

wlan_led_pin = machine.Pin(13, machine.Pin.OUT, value=1)
wlan_led = machine.Signal(wlan_led_pin, invert=True)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print(f'Connected? {wlan.isconnected()}\n')
print('connecting to network...')
wlan.connect('<SSID>', '<PASSWORD>')
while not wlan.isconnected():
    pass
print(f'Connected? {wlan.isconnected()}\n')
print('network config:')
print(f'IP: {wlan.ifconfig()[0]}')
print(f'Netmask: {wlan.ifconfig()[1]}')
print(f'Gatway: {wlan.ifconfig()[2]}')
print(f'DNS: {wlan.ifconfig()[3]}')

if wlan.isconnected():
    wlan_led.on()
    webrepl.start()
