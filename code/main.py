try:
  import usocket as socket
except:
  import socket
import onewire, ds18x20
import time
import machine

heating_led_pin = machine.Pin(12,machine.Pin.OUT, value=0)
heater_pin = machine.Pin(16,machine.Pin.OUT, value=0)
heating_led = machine.Signal(heating_led_pin, invert=True)
heater = machine.Signal(heater_pin, invert=False)
ow_pin = machine.Pin(4,machine.Pin.OUT)
ow_ds = ds18x20.DS18X20(onewire.OneWire(ow_pin))

roms = ow_ds.scan()
print('found devices:', roms)

temp=37.000
hyst_low=0
hyst_high=0
max_runtime=12

def format_seconds_to_hhmmss(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    #return "%02i:%02i:%02i" % (hours, minutes, seconds)
    return f'{hours:02}:{minutes:02}:{seconds:02}'

run_me = True

while run_me:
    run_time = time.time()
    if run_time/3600 > max_runtime:
    #if run_time > 30:
        print('!!!!!!!!!!!!!!Stop joghiman!!!!!!!!!!!!!!!!!')
        heating_led.off()
        heater.off()
        #time.sleep(5)
        #continue
        #machine.deepsleep()
        run_me = False
        break
    print(f'Run Time: {format_seconds_to_hhmmss(run_time)}')
    #time.time()
    #Get the onewire sensor values
    ow_ds.convert_temp()
    # We need to wait before we can access the data
    time.sleep_ms(750)
    jogh_temp = ow_ds.read_temp(bytearray(b'(\xff\x84\xca\x80\x14\x02\xb7'))
    print(f'Joghurt Temp:{jogh_temp}')
    if jogh_temp < temp + hyst_high:
        heating_led.on()
        heater.on()
    elif jogh_temp > temp - hyst_low:
        heating_led.off()
        heater.off()
    time.sleep(5)

#Ensure that heater is off
heating_led.off()
heater.off()
#Fading Heater LED to show that we are finshed
pwm0 = machine.PWM(machine.Pin(12))
pwm0.freq(100)
duty=300
denom=5
pwm0.duty(duty)
print('!!!!!!!!!!!!!!!! FINISHED !!!!!!!!!!!!!!!!!!!!')
while True:
    while (duty < 1023):
        time.sleep(denom/duty)
        duty += 1
        pwm0.duty(duty)
    while (duty > 300):
        time.sleep(denom/duty)
        duty -= 1
        pwm0.duty(duty)
pwm0.deinit()
