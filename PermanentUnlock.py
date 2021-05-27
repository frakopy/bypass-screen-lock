import ctypes
ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
input('{Presiona enter para salir}')
ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
