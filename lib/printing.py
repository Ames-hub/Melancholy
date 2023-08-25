colours = {
    'clear': '\033[0m',
    'reset': '\033[0m',
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
}

import time
class printing():
    def __init__(self, default_colour=None):

        if default_colour != None:
            self.default_colour = default_colour
        else:
            self.default_colour = 'cyan'
        
        self.colours = {
            'reset': '\033[0m',
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
        }

    def color_text(self, text, color=None):
        if color == None:
            color = self.default_colour

        if color in self.colours:
            return f"{self.colours[color]}{text}{self.colours['reset']}"
        else:
            return text

    def bold_text(self, text):
        return f"\033[1m{text}\033[0m"

    def underline_text(self, text):
        return f"\033[4m{text}\033[0m"

    def format_text(self, text, color=None, bold=False, underline=False):
        if color:
            text = self.color_text(text, color)
        if bold:
            text = self.bold_text(text)
        if underline:
            text = self.underline_text(text)
        return text

    def delay(self, text, delay=0.1, color=None, print_faster: tuple=None) -> None:
        if print_faster:
            fast_sub, fast_delay = print_faster
        else:
            fast_sub, fast_delay = None, delay

        for char in text:
            if color:
                char_to_print = self.color_text(char, color)
            else:
                char_to_print = char

            if fast_sub and char in fast_sub:
                print(char_to_print, end='', flush=True)
                time.sleep(fast_delay)
            else:
                print(char_to_print, end='', flush=True)
                time.sleep(delay)

        print()

    def solid_color(self, text, color=None):
        if color == None:
            color = self.default_colour
        colored_text = self.color_text(text, color)
        print(colored_text)

    def partial_solid(self, text, target, target_color, default_color):
        parts = text.split(target)
        for i, part in enumerate(parts):
            if i > 0:
                print(self.color_text(target, target_color), end='')
            print(self.color_text(part, default_color), end='')
        print()