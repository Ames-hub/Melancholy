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

    def bold_text(self, text):
        return f"\033[1m{text}\033[0m"

    def underline_text(self, text):
        return f"\033[4m{text}\033[0m"

    def format_text(self, text, colour=None, bold=False, underline=False):
        if colour:
            text = self.colour_text(text, colour)
        if bold:
            text = self.bold_text(text)
        if underline:
            text = self.underline_text(text)
        return text

    def delay(self, text, delay=0.1, colour=None, print_faster: tuple=None) -> None:
        if print_faster:
            fast_sub, fast_delay = print_faster
        else:
            fast_sub, fast_delay = None, delay

        printed_text = ""
        try:
            for char in text:
                printed_text += char
                if colour:
                    char_to_print = self.colour_text(char, colour)
                else:
                    char_to_print = char

                if fast_sub and char in fast_sub:
                    print(char_to_print, end='', flush=True)
                    if char != " ":
                        time.sleep(fast_delay)
                else:
                    print(char_to_print, end='', flush=True)
                    if char != " ":
                        time.sleep(delay)
            print()
        except KeyboardInterrupt:
            remaining_text = text[len(printed_text):]
            if colour:
                remaining_text = self.colour_text(remaining_text, colour)
            print(remaining_text, flush=True)

    def partial_solid(self, text, targets, target_colours, default_colour):
        # Create a list of tuples, each containing a target word and its color
        targets_with_colours = list(zip(targets, target_colours))

        # Sort the list by the length of the target words, in descending order
        targets_with_colours.sort(key=lambda x: len(x[0]), reverse=True)

        # Split the text by the target words and color the parts in the default color
        parts = [self.colour_text(part, default_colour) for part in text.split(targets_with_colours[0][0])]

        # Color the target words in their respective colors and join the parts back together
        text = self.colour_text(targets_with_colours[0][0], targets_with_colours[0][1]).join(parts)

        # Repeat the process for the remaining target words
        for target, colour in targets_with_colours[1:]:
            parts = [self.colour_text(part, default_colour) for part in text.split(target)]
            text = self.colour_text(target, colour).join(parts)

        print(text)

    def solid_colour(self, text, colour=None):
        if colour == None:
            colour = self.default_colour
        coloured_text = self.colour_text(text, colour)
        print(coloured_text)

    def colour_text(self, text, colour=None):
        if colour == None:
            colour = self.default_colour

        if colour in self.colours:
            return f"{self.colours[colour]}{text}{self.colours['reset']}"
        else:
            return text