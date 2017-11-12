import spidev
import time


def analog_read(channel):
    r = spi.xfer2([0x06, channel << 6, 0])
    adc_out = ((r[1] & 0x0f) << 8) | r[2]
    return adc_out


try:
    while True:
        print('value')
        time.sleep(1)
except Exception as e:
    print "%s end\n" % e.args
