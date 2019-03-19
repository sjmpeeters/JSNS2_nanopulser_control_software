#!/usr/bin/env python
#
# pulser_exception:
#
# PulserException
#
# Exceptions raised by the pulser modules
#
# Author: James Waterfield
#         <j.waterfield@sussex.ac.uk>
#
# History:
# 2016/10/21: First instance
#
###########################################
###########################################


class PulserException(Exception):
    """General exception for the Pulser command modules"""

    def __init__(self, error):
        Exception.__init__(self, error)


class PulserSerialException(Exception):
    """Exception when communicating with the Serial Port"""

    def __init__(self, error):
        Exception.__init__(self, error)


class ThreadException(Exception):
    """Exception raised specific to threading issues"""

    def __init__(self, error):
        Exception.__init__(self, error)
