# Overview
Pythonic light controller via raspberry py for art projects. Designed for WS2812 LED usage via the module rpi-ws281x 

## Modules and Classes

### Rig

The `rig` module defines the physical lighting installation with the following classes

- `LightArray` creates the `PixelStrip` hardware edge from the rpi-ws281x third party library.
- `Palette` defines reusable color constants and color groups.
- `Rack` defines the configured fixtures for the installation.

#### Fixtures

A lighting component is called a `Fixture`. A fixture owns an LED address range and a fixture-level lock.

Fixture locks are used as write policy:

- same fixture = serialized writes
- different fixtures = concurrent writes

Fixtures can contain `Zones`. Zones are named LED subranges used when patterns need to target part of a fixture.

Current configured fixtures:

- Two 24 Bits WS2812 RGB LED Ring = https://www.amazon.com/dp/B09YTGCRV1
- One 241 LEDs 9 Rings WS2812B 5050 RGB = https://www.amazon.com/dp/B083VWVP3J

### Patterns

The `patterns` module defines reusable fixture-level light activity.

Patterns write LED values against fixtures or zones. Examples:

- activate
- flash
- chase
- chase multi
- shuffle
- shuffle by color group

Patterns respect fixture locks so concurrent steps can safely target different fixtures.

### Control

The `control` module organizes pattern calls into executable `Sequences`.  

Sequences step through patterns across the rack. For example, a chase step can run a big-ring `chase_multi` pattern while the small fixtures run their own chase pattern concurrently.

A scene is the top-level execution of a collection of sequences organized for execution by the OS services. 

### Models

Models are stored in `src.models`. They are frozen pydantic models for sharing data across classes.

- `Colors` defines a named RGB color.
    - `RGB` defines color channel values.
    - `ColorGroup` defines a tuple of colors.
- `Fixture` defines a lighting component with LEDs and a lock.
    - `Fixtures` defines a configured collection of fixtures.
    - `Leds` defines a fixture LED range and optional zone and gobo groups.
    - `Zone` defines a named LED subrange.
    - `Gobo` collection frames to make moving patterns
    - `Frame` collection of led's that make a specific pattern for a gobo

## Run

rpi-ws281x requires root level privileges access.

run scene manually
 - sudo env PYTHONPATH=/home/cp/git/py_lumen/src   /home/cp/git/py_lumen/.venv/bin/python -m exe

### Startup service

- sudo nano /etc/systemd/system/py_lumen.service
- sudo nano /etc/systemd/system/py_lumen_audio.service

### Service Commands

- sudo systemctl enable py_lumen_audio
- sudo systemctl enable py_lumen.service
- sudo systemctl disable py_lumen_audio
- sudo systemctl disable py_lumen.service
- sudo systemctl start py_lumen_audio
- sudo systemctl start py_lumen.service
- sudo systemctl stop py_lumen_audio
- sudo systemctl stop py_lumen.service
- sudo systemctl daemon-reload

## Testing
Tox runs executes testing activities using the 'tox.ini'.  All testing tools reference use the 'tox.ini' to manage their configs.

### Formatting, Linting, and Code Style

Tox executes the following commands:

```bash
black src
pylint --rcfile=tox.ini src
pycodestyle src
```

The goal is to maintain PEP 8 compliance and Python best practices. We use Make to orchestrate CI execution in GitHub Actions. GitHub Actions will automatically apply any black formatting changes as part of a run.

### Security Safety

Tox executes the following commands:

```bash
bandit -r src
pip-audit -r requirements.txt
```

## Virtual Environments

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-test.txt
```

## System Environment Variables

```bash
export PYTHONPATH={path}/py_lumen/src:$PYTHONPATH
export PYTHONPATH={path}/py_lumen/tests:$PYTHONPATH
```
