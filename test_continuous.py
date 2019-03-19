#This script will pulse the the specified channel for at the specified intensity and rate continuously
import serial_command
import argparse
import time


if __name__ == '__main__':
    try:
	    parser = argparse.ArgumentParser()
	    parser.add_argument("-p", dest="pulse_height", type=int,
				help="pulse_height")
	    parser.add_argument("-d", dest="pulse_delay", type=float,
				help="pulse_number")
	    parser.add_argument("-c", dest="channel", type=int,
				help="channel number")
	    args = parser.parse_args()
	    sc = serial_command.SerialCommand()
	    sc.set_channel(args.channel)
	    print "Set channel"
	    time.sleep(1)
	    sc.set_pulse_height(args.pulse_height)
	    print "Set Pulse Height"
	    time.sleep(1)
	    sc.set_pulse_delay(args.pulse_delay)
	    print "Set Pulse Delay"
	    time.sleep(1)
	    sc.set_trigger_delay(80)
	    print "Set trigger delay"
	    time.sleep(1)
	    sc.set_fibre_delay(0)
	    print "Set fibre delay"
	    time.sleep(1)
	    sc.fire_continuous() 
	    print "Fire"
	    while True:
                continue
    except KeyboardInterrupt:
	    print "Stopping"
            sc.stop()



