#This script will pulse the the specified channel for at the specified intensity and rate for a specified number of pulses
import serial_command
import argparse
import time


if __name__ == '__main__':
    try:
	    parser = argparse.ArgumentParser()
	    parser.add_argument("-n", dest="pulse_num", type=int,
				help="pulse_number")
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
	    sc.set_pulse_number(1000)
	    print "Set Pulse Number"
	    time.sleep(1)
	    sc.set_pulse_delay(args.pulse_delay)
	    print "Set Pulse Delay"
	    time.sleep(1)
	    sc.set_trigger_delay(800)
	    print "Set trigger delay"
	    time.sleep(1)
	    sc.set_fibre_delay(10)
	    print "Set fibre delay"
	    time.sleep(1)
	    npulses = 0
	    sc.fire()
	    npulses += 1000.
	    if args.pulse_num % 1000. != 0.:
	        raise ValueError("Pulse Number must be a multiple of 1000")
	    fire = True
	    while fire and npulses < args.pulse_num:
	        if sc.check_firing():
		    pass
	        else:
		    npulses += 1000.
		    sc.fire()
	        print "Number of pulses", npulses, "time active", args.pulse_delay*1e-3*npulses
    except KeyboardInterrupt:
        print "Stopping"
        sc.stop()
