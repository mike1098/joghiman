# joghiman (an upcycling project)
A micropython code to make Joghurt ;-)

As my original Joghurt Maker quit its duty I was curious how it was built so I opened it. Inside was a microcontroller with a very bare schematic. The power came direct from 220V AC and the microcontroller was only managing the runtime but not the temperature. Temperature was controlled by a simple bimetal switch which is controlling the temperature not very accurate and also temp was always too high.
Only the microcontroller was not working, the heating and the bimetal switch was intact. So I decided to replace the microcontroller with an ESP8266 and control temperature with a OneWire Temp Sensor which has better accuracy. As a power supply I used an old wall power supply from a smart device and stripped the casing. The heating elements are switched by a solid state relais but still in series with the bi metal switch for safety.


## The PCB from the front

 At the far right you see the reset switch, followed by the solid sate connector, the connector for the OneWire and the connector to program the ESP8266. In the middle you see the ESP8266. To connect the ESP8266 with the PCB I used thread wire. On the left side of the microcontroller is the jumper to put the ESP8266 in to program mode, followed by the connector for the original keyboard and the connectior to the powersupply.

![PVB Back](pics/pcb_front.jpg)

## The PCB from the back

At the the top you see the power controller.
![PCB Front](pics/pcb_back.jpg)

## Joghiman from inside
At the far right top you see the PCB with the ESP8266. I connect the original key board but currently I use only the LED´s to show the status. At the right middle you see the solid state relais, in the middle the bi metal switch and at the left middle the power supply. The four whit elemnts are the heating.

![Inside Joghiman](pics/inside.jpg)

## Joghiman in action

![Total](pics/total.jpg)

This shows the Joghiman in action. The LED´s from left to right is power, wlan and heating on. I use water as a reference fluid to measure the temperature with the OneWire temp sensor. The temp is exact on 37°C. The quality of my Joghurt is much better after these modifications.