from smbus import SMBus
import time

bus = SMBus(1)

print("read the ad")

#bus.write_byte(0x48, 0)

while True:
	time.sleep(1)
	print(5*(bus.read_byte(0x48)/255.0))
