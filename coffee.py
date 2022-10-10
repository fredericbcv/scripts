#!python

import ctypes

'''
API documentation:
https://msdn.microsoft.com/en-us/library/windows/desktop/aa373208(v=vs.85).aspx
'''
ES_AWAYMODE_REQUIRED    = 0x00000040
ES_CONTINUOUS           = 0x80000000
ES_DISPLAY_REQUIRED     = 0x00000002
ES_SYSTEM_REQUIRED      = 0x00000001

try:
    # Prevent sleep mode
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | \
        ES_DISPLAY_REQUIRED | \
        ES_SYSTEM_REQUIRED
        )

    print('Insomnia in progress... ')

    # Wait forever
    while True:
        pass

except KeyboardInterrupt:
    # Clear EXECUTION_STATE flags
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS
        )
    print("It's time to go to sleep :)",end='')
else:
    raise e