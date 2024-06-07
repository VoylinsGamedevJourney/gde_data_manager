# Godot data manager

This is a simple GDExtension for Godot which I use for [GoZen](https://github.com/VoylinsGamedevJourney/GoZen).

## Usage

Extend from DataManager and use the `save_data` and `load_data` functions. All normal variables will be saved except for variables starting with an underscore and const variables.

## Why a GDExtension?

The main reason is just because I use this method for saving data in all my projects so just having a plug and play option seems like the best and easiest solution. Just copy the GDExtension into you application in the correct folder together with the .gdextension file and you are good to go.

