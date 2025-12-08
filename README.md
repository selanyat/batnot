# Batnot

Batnot is a simple script to send a notification when battery is below 30 percent.
It was built with hyprland in mind.

Are there other alternatives well implemented and maintained?? Most likely, more like a yes. But I'm still building one on my own anyways.

## Features
- Low battery notification (Visual)
- '*Low battery please charge* notification in morse code' (Audio notification)

## Installation
- Clone the repository
```bash
git clone git@github.com:selanyat/batnot.git
cd batnot
```
- Create a virtual environment
```bash
python -m venv batnot
source ./batnot/bin/activate
```
- Install dependencies
```bash
pip install -r reqirements.txt
```

## Usage
- Make file executable
```bash
chmod +x batnot.py
```
- Open your hyprland config file
- Execute once on startup and run in background
```jsonc
exec_once = bash -c "sleep 300 && /path/to/intepretor path/to/batnot.py"
# Sleep is completely optional
```
>[!NOTE]
>A notification utility such as `mako` or `dunst` must be installed on your PC for this to work.<br>
>See [mako on arch wiki](https://man.archlinux.org/man/mako.5.en)<br>
>See [dunst website](https://dunst-project.org)<br>
>I can't assure compatibility with other notification daemons


## Credits
- The notification sound was generated on [online sound.net](https://onlinesound.net/morse-code-generator)

