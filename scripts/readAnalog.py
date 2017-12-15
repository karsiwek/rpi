from smbus import SMBus

bus = SMBus(1)

bus.write_byte(0x48, 0 )

print(bus.read_byte(0x48))

