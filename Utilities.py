import ctypes
import os
from time import sleep

RESET = "\033[0;0m"
BLACK = "\033[0;30m"
DARK_GRAY = "\033[1;30m"
RED = "\033[0;31m"
LIGHT_RED = "\033[1;31m"
GREEN = "\033[0;32m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[0;33m"
ROSE = "\033[1;35m"
BLUE = "\033[0;34m"
LIGHT_BLUE = "\033[1;34m"
MAGENTA = "\033[0;35m"
LIGHT_MAGENTA = "\033[1;35m"
CYAN = "\033[0;36m"
LIGHT_CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
LIGHT_GRAY = "\033[0;37m"


class Utilities:

    def __init__(self):

        self.os_name = os.name

        # To use the colors properly in the Windows CMD
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

        self.RESET = RESET
        self.BLACK = BLACK
        self.DARK_GRAY = DARK_GRAY
        self.RED = RED
        self.LIGHT_RED = LIGHT_RED
        self.GREEN = GREEN
        self.LIGHT_GREEN = LIGHT_GREEN
        self.YELLOW = YELLOW
        self.ROSE = ROSE
        self.BLUE = BLUE
        self.LIGHT_BLUE = LIGHT_BLUE
        self.MAGENTA = MAGENTA
        self.LIGHT_MAGENTA = LIGHT_MAGENTA
        self.CYAN = CYAN
        self.LIGHT_CYAN = LIGHT_CYAN
        self.WHITE = WHITE
        self.LIGHT_GRAY = LIGHT_GRAY

    # Messages (Blueprints to make things easier)
    def info(self, message, time_to_sleep=0, clear=False):

        print(self.YELLOW + "[" + self.BLUE + "i" + self.YELLOW + "] " + self.CYAN + message + self.WHITE)
        sleep(time_to_sleep)

        if clear:
            self.clear()

    def error(self, message, time_to_sleep=0, clear=False):

        print(self.YELLOW + "[" + self.RED + "-" + self.YELLOW + "] " + self.CYAN + message + self.WHITE)
        sleep(time_to_sleep)

        if clear:
            self.clear()

    def success(self, message, time_to_sleep=0, clear=False):

        print(self.YELLOW + "[" + self.GREEN + "+" + self.YELLOW + "] " + self.CYAN + message + self.WHITE)
        sleep(time_to_sleep)

        if clear:
            self.clear()

    def warning(self, message, time_to_sleep=0, clear=False):

        print(self.YELLOW + "[" + self.LIGHT_RED + "!" + self.YELLOW + "]" + self.CYAN + message + self.WHITE)
        sleep(time_to_sleep)

        if clear:
            self.clear()

    def clear(self):

        # for windows
        if self.os_name == 'nt':
            _ = os.system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = os.system('clear')
