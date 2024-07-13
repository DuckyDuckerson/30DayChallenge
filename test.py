
import curses

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

        if key == curses.KEY_UP and current_selection > 0 or key in [107] and current_selection > 0:
            current_selection -= 1
        elif key == curses.KEY_DOWN and current_selection < len(options) - 1 or key in [106] and current_selection < len(options) - 1:
            current_selection += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return options[current_selection]


def test_sub_menu(stdscr):
    curses.curs_set(0)

    options = ["Item One", "Item Two", "Item Three", "Exit"]

    selected_option = display_menu(stdscr, options)

    stdscr.addstr(0, 0, f"You selected: {selected_option}")
    stdscr.refresh()
    stdscr.getch()
   

def test_menu(stdscr):
    curses.curs_set(0)

    options = ["Start Game", "Submenu", "Options", "Exit",]
    menu_title = "This is a Menu"

    selected_option = display_menu(stdscr, options, menu_title)

    if selected_option == "Submenu":
        test_sub_menu(stdscr)

curses.wrapper(test_menu)