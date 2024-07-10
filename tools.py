from compilation import compile_c_code
import ctypes


compile_c_code("support.c", "support.so")
lib = ctypes.cdll.LoadLibrary("./support.so")

lib.print_message.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
lib.print_message.restype = None


def print_message(message, speed, newline):
    lib.print_message(message.encode('utf-8'), speed, newline)
