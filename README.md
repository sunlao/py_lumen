# Overview
pythonic light controller via rasberry py for art projects. Designed for WS2812 LED usage via the module rpi-ws281x 

## Modules and Classes

## Patterns

The pattern module are resuable assertions of Leds by `fixtures` and `zones`.  Some examples of patterns are:

- activate
- flash
- chase
- shuffle by color group 

## Control

The Control module asserts led patterns for a `light_rig` class. A light_rig is a class that asserts lighting componets called fixtures (see below). Patterns can organzied into a `steps` class. Steps can be orgnized by the `sequence` class.  A simple sequences may assert a pattern directly. A `scene` is the final class in the controller which is a collection of sequences.  Scenes are what is executed by services. Examples of a simple sequence 

- Turn Fixture Off
- Flash Fixture Single Color

Example of complex sequence `Create Target`.

- Step 1 - Activate 1 zone: "rings 1-3"
- Step 2 - Activate 2 zones: "rings 1-3" and "rings 4-6" 
- Step 3 - Activate 3 zones: "rings 1-3", "rings 4-6" and "rings 7-9" 
- Turn Fixture Off

##  Models

Models are stored in `src.models`

## Fixtures 

A Lighting component is called a `fixture` and can be grouped by `Fixtures`. A fixture is locked on assertion to ensure only one call can be made it at a time. Current fixtures instantiated in the `src.control.light_rig` class:

- Two 24 Bits WS2812 RGB LED Ring =  https://www.amazon.com/dp/B09YTGCRV1
- One 241 LEDs 9 Rings WS2812B 5050 RGB = https://www.amazon.com/dp/B083VWVP3J

### Leds and Zones

Fixtures have `LED`s that are numbered and can be organized into `Zones`. 

## Colors 

A `Color` is a specific assertion of `RGB`.  A collection colors can be grouped into a `ColorGroup` 

# Run

rpi-ws281x requires root level priveleges access.

run scene manually
 - sudo env PYTHONPATH=/home/cp/git/py_lumen/src   /home/cp/git/py_lumen/.venv/bin/python -m control.scene 

run color tune manually
 - sudo env PYTHONPATH=/home/cp/git/py_lumen/src   /home/cp/git/py_lumen/.venv/bin/python -m control.color_tune 


## Startup service

- sudo nano /etc/systemd/system/py_lumen.service
- sudo nano /etc/systemd/system/py_lumen_audio.service

## Service Commands

- sudo systemctl enable py_lumen_audio
- sudo systemctl enable py_lumen.service
- sudo systemctl disable py_lumen_audio
- sudo systemctl disable py_lumen.service
- sudo systemctl start py_lumen_audio
- sudo systemctl start py_lumen.service
- sudo systemctl stop py_lumen_audio
- sudo systemctl stop py_lumen.service

# Testing
Tox runs executes testing activities using the 'tox.ini'.  All testing tools reference use the 'tox.ini' to manage their configs.

## Formatting, Linting, and Code Style

Tox executes the following commands:

```bash
black src tests
pylint --rcfile=tox.ini src
pylint --rcfile=tox.ini --disable=C0103 tests
pycodestyle src tests
```

The goal is to maintain PEP 8 compliance and Python best practices. We use Make to orchestrate CI execution in GitHub Actions. GitHub Actions will automatically apply any black formatting changes as part of a run.

## Execution

Test are executed by pytest and stored in `/tests/pytest`. Pytest uses with fixtures stored in `/tests/fixtures` and managed by `/tests/conftest.py`. Code coveage is performed by module `coverage` and used when pytest is executed by tox. 

# Virtual Environments

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-test.txt
```

# System Environment Variables

```bash
export PYTHONPATH={path}/py_lumen/src:$PYTHONPATH
export PYTHONPATH={path}/py_lumen/tests:$PYTHONPATH
export ENV=prod
```
