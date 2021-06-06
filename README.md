# hex_game
TODO: find a better name

## Game Idea

Start with one main character that you can control in a dark, creepy world with a single light. Do some stuff and befriend some people to expand the influence of the light (while avoiding obstacles that can kill you) and get more friends you can play with. At the end escape using the power of friendship or something.

## Desired Elements

* Unlockable characters with stories of their own, characters interact and form relationships
* Some sort of choose-your-own-adventure style interactivity
* Build a base
* *Some* graphically rich elements, such as images that pop up when you hover over an object or tile. These could be pictures of objects or snapshots of what your environment looks like.

## Running/testing

You'll need the Pyglet game library: `pip install pyglet --user`

To run the game, you can simply cd to this `hex_game` directory and run `python3 ./`

## Keyboard Shortcuts

- N: create a new world and start over, as opposed to the saved state that was loaded by default.
- S: Keyboard shortcut to save the current state (will probably be changed in the future)

## Moving Around

Click and drag to move the camera and see different parts of the canvas. Scroll the mouse wheel to zoom in or out.

Player movement will be via mouse, although A and D keys are currently able to move player left and right, they will be disabled once mouse movement is enabled.