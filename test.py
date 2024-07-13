
import curses

def display_menu(stdscr, options):
    # Clear screen
    stdscr.clear()

    # Initialize the current selection
    current_selection = 0

    # Display menu and handle user input
    while True:
        # Display title
        stdscr.addstr(0, 0, "Pokémon Menu")
        stdscr.addstr(1, 0, "-" * 20)

        # Display all options
        for idx, option in enumerate(options):
            y = idx + 2  # Start options from the third line

            if idx == current_selection:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, 0, f"> {option}")
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, 0, f"  {option}")

        # Refresh the screen
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        if key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1
        elif key == curses.KEY_DOWN and current_selection < len(options) - 1:
            current_selection += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # Return the selected option
            return options[current_selection]

def main(stdscr):
    # Don't display cursor
    curses.curs_set(0)

    # Define menu options
    options = ["Start Game", "Load Game", "Options", "Exit"]

    # Display menu and get selection
    selected_option = display_menu(stdscr, options)

    # Clear screen
    stdscr.clear()

    # Display result
    stdscr.addstr(0, 0, f"You selected: {selected_option}")
    stdscr.refresh()
    stdscr.getch()

# Initialize curses and call main function
curses.wrapper(main)