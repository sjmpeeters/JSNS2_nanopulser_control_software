#######################
# parameters.py:
#  Any parameters that may need checking
#
import math

max_pulse_number = 65025
max_fine_trigger_delay   = 63.75  # ns
max_course_trigger_delay = 1275  # ns


def pulse_number(number):
    adjusted = False
    if type(number) != int:
        raise Exception("Pulse Number must be an integer")
    if number > max_pulse_number:
        raise Exception("Pulse Number must be < %d. You set %d" %
                        (65025, number))
    hi = -1
    lo = -1
    diff = 100000  # bigger than max pn
    for i in range(1, 256):
        # assume hi is i
        lo_check = number/i
        if lo_check > 255:
            lo_check = 255
        check = i * lo_check
        if math.fabs(check - number) < diff:
            diff = math.fabs(check - number)
            hi = i
            lo = lo_check
        if check == number:
            break
    actual_par = hi * lo
    if actual_par != number:
        adjusted = True
    return adjusted, actual_par, hi, lo


def course_trigger_delay(delay):
    adjusted = False
    delay = float(delay)
    if delay > max_course_trigger_delay or delay < 0:
        raise Exception("Course trigger Delay must be >%s and <%s" %
                        (0, max_course_trigger_delay))
    parameter = int(round(delay)/5)
    adj_delay = parameter * 5
    if delay != adj_delay:
        adjusted = True
    return adjusted, adj_delay, parameter


def fine_trigger_delay(delay):
    adjusted = False
    delay = float(delay)
    if delay > max_fine_trigger_delay or delay < 0:
        raise Exception("Fine trigger delay must be >%s and <%s" %
                        (0, max_fine_trigger_delay))
    parameter = int(round(delay * 4.))
    adj_delay = float(parameter) / 4.
    if delay != adj_delay:
        adjusted = True
    return adjusted, adj_delay, parameter
