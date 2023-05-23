# README

This script allows you to choose at random a manicure comprising a base colour, a topper and/or a top coat.
You can easily edit your list of polishes and add or remove different polish types.

## Use
It is a simple python script you can execute in CLI. The script will first select at random a base polish type between several options then a specific polish in the selected type. It then asks you if you want to roll for a topper, then a top coat. The topper choice defaults to yes because it's always better to add shiny stuff on your nails.

## Variables
The lists of nail polishes types and top coats types are defined in arrays at the beginning of the main script.
The lists of specific nail polishes are found in text files. The file is placed in the "files" folder and named after the polish type (for example: multichrome.txt for multichrome nail polishes). You could of course use a .csv file, just change the separator in the split in the main script if you use commas or semicolons for example.

## Glossary
- A "taco" is a top coat: a transparent polish you put over your manicure to harden and protect it.
- A creme polish is an opaque colour with no particular effect.
- A linear holographic polish is a polish containing a lot of holographic glitter.
- A multichrome polish is a polish with the colour shifting depending on the light.
- A topper is a transparent polish containing glitter or foils for pretty, shiny effects.
This has absolutely no impact on the script usage but I thought it could be useful.
