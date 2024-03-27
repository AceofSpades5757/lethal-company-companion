A companion application to assist with the lengthy keypresses in the terminal.

# Features

* `view monitor` command
* `switch` command
* TODO `switch <USERNAME>` command
* `flash <RADAR_BOOSTER>` command
* `ping <RADAR_BOOSTER>` command

# Current State

Currently, it's a simple command line application that allow for certain keys to act as shortcuts for Lethal Company.

## Installation

* Windows: `py -m pip install git+https://github.com/AceofSpades5757/lethal-company-companion`
* Linux: `python -m pip install git+https://github.com/AceofSpades5757/lethal-company-companion`

## Usage

`lcc run` to start the application.

`lcc help` or `lcc --help` to start the application.

It allows for an optional argument `--radar-booster` to be passed in to specify the radar booster to use.

* <kbd>F1</kbd> - `switch` command
* <kbd>F2</kbd> - `flash <RADAR_BOOSTER>` command
* <kbd>F3</kbd> - `ping <RADAR_BOOSTER>` command
* TODO - `switch <USERNAME>` command TODO
* <kbd>F5</kbd> - `view monitor` command
* <kbd>F11</kbd> - Toggle debug mode for additional logging, etc.
* <kbd>F12</kbd> - Quit the application

# Desired State

There were plans for a floating GUI to be made with some different options, but I haven't had the time or interest to work on it. Feel free to reach out if this really interests you.

* List of players that could be modified.
  * Would allow certain sets of commands/options so switching to a specific player would be easier, especially in larger groups.
* List of radar boosters that could be modified and selected.
  * Would allow for easier switching between radar boosters.
  * Would be a lot simpler than than the idea behind a list of players.
* A `<LEADER>` key similar to Vim's leader key.
  * Would allow you to arbitrarily set a key to be the leader key.
  * Would allow you to type `<LEADER> + <COMMAND>` to run a command: e.g. `\s1` to switch to player 1 or `\f` to flash the selected radar booster.
