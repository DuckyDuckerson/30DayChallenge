from support.compilation import compile_c_code
import ctypes
import curses

compile_c_code("support/support.c", "support/support.so")
lib = ctypes.cdll.LoadLibrary("./support/support.so")

lib.print_message.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
lib.print_message.restype = None


def print_message(message, speed, newline):
    lib.print_message(message.encode('utf-8'), speed, newline)

def display_menu(stdscr, options, menu_title="Menu"):
    stdscr.clear()

    current_selection = 0

    while True:
        stdscr.addstr(0, 0, menu_title)
        stdscr.addstr(1, 0, "-" * 20)

        for idx, option in enumerate(options):
            y = idx + 2

            if idx == current_selection:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, 0, f"> {option}")
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, 0, f"  {option}")

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_selection > 0 or key in [106, 75] and current_selection > 0:
            current_selection -= 1
        elif key == curses.KEY_DOWN and current_selection < len(options) - 1 or key in [107, 74] and current_selection <len(options):
            current_selection += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return options[current_selection]

