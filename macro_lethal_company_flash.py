"""Tool to help with Lethal Company Flash.

TODO: Switch from direct keys, like F1, to something using a <LEADER> key, like
`,,`.
    Just like Vim does it.
    An issue would be for longer sequences, like `,,ef` on top of `,,e`.
TODO: Refactor to a CLI tool.
    TODO: Refactor the radar boster name to be a command line argument.
        e.g. `python macro_lethal_company_flash.py --radar-booster="Radar Booster"`
"""
import logging
import os
from typing import Final
from typing import NoReturn
from typing import Callable
from dataclasses import dataclass
from dataclasses import field

import keyboard


LOOP_DELAY: Final[float] = 0.1  # seconds


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
    ]
)


@dataclass
class Macro:
    """Macro class."""
    name: str
    keys: tuple[str, ...]
    help_text: str
    function: Callable[[], None]

    def print_help(self) -> None:
        """Print help text."""
        # print(f'Press {SWITCH_KEY} to run "switch" macro.')
        # Press F1, F2, or F3 to run <NAME> macro: <HELP_TEXT>
        print(f'Press {self.keys} to run "{self.name}" macro:')
        print(f'    {self.help_text}')

    def set_hotkeys(self) -> None:
        """Set hotkeys."""
        for key in self.keys:
            keyboard.add_hotkey(key, self.function)



@dataclass
class Settings:
    """Settings class."""
    debug: bool = False
    radar_booster_name: str = ''
    macros: list[Macro] = field(default_factory=list)


# Globals
RADAR_BOOSTER_NAME: Final[str] = input('Radar Booster Name: ')


def flash(radar_booster: str) -> None:
    """Type out flash macro."""
    keyboard.write('flash ')
    keyboard.write(radar_booster)
    keyboard.press_and_release('enter')
    # guard against flashlight purchases
    # WARNING: This causes an annoying sound to be played, every time.
    # time.sleep(0.1)
    # keyboard.write('d')
    # keyboard.press_and_release('enter')


def ping() -> None:
    """Type out ping macro."""
    keyboard.write('ping ')
    keyboard.write(RADAR_BOOSTER_NAME)
    keyboard.press_and_release('enter')


def switch() -> None:
    """Type out switch macro."""
    keyboard.write('switch')
    keyboard.press_and_release('enter')


def view_monitor() -> None:
    """Toggle monitor view."""
    keyboard.write('view monitor')
    keyboard.press_and_release('enter')


def toggle_debug(settings: Settings) -> None:
    """Toggle debug."""
    settings.debug = not settings.debug
    logging.getLogger().setLevel(logging.DEBUG if settings.debug else logging.INFO)

    os.system('clear')
    print(f'DEBUG: {"ON" if settings.debug else "OFF"}')


def main() -> NoReturn:
    """Main function."""
    settings: Settings
    macros: list[Macro] = [
        # System
        Macro(
            name='quit',
            keys=('F12',),
            help_text='Quit the program.',
            function=lambda: os._exit(0),
        ),
        Macro(
            name='debug',
            keys=('F11',),
            help_text='Toggle debugging.',
            function=lambda: toggle_debug(settings),
        ),
        # Basic
        Macro(
            name='view monitor',
            keys=('F5',),
            help_text='Toggle monitor view.',
            function=view_monitor,
        ),
        Macro(
            name='switch',
            keys=('F1',),
            help_text='Type out switch macro.',
            function=switch,
        ),
        # Radar Booster
        Macro(
            name='flash',
            keys=('F2',),
            help_text='Type out flash macro.',
            function=lambda: flash(RADAR_BOOSTER_NAME),
        ),
        Macro(
            name='ping',
            keys=('F3',),
            help_text='Type out ping macro.',
            function=ping,
        ),
    ]
    settings = Settings(
        radar_booster_name=RADAR_BOOSTER_NAME,
        macros=macros,
    )

    # Verification
    # * Check that no hotkeys are duplicated.
    maps: dict[str, Macro] = {}
    for macro in settings.macros:
        for key in macro.keys:
            if key in maps:
                raise ValueError(
                    f'Hotkey "{key}" is duplicated on macros '
                    f'"{maps[key].name}" and "{macro.name}".'
                )
            maps[key] = macro

    # Set hotkeys
    for macro in settings.macros:
        macro.set_hotkeys()

    # Print help text
    print()
    for macro in settings.macros:
        macro.print_help()
        print()

    input('Press ENTER to quit.\n')
    os._exit(0)


if __name__ == '__main__':
    raise SystemExit(main())
