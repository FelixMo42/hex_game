import pyglet
from src.polydraw import draw_polygon

def is_over_button(button, x, y):
    """Cheacks if the given (x, y) is over the button."""

    return (
        x >= button.x and x <= button.x + button.content_width and
        y <= button.y and y >= button.y - button.content_height
    )

class Gui:
    x = 0
    buttons = []

    def draw(self, mouse_pos):
        """Draw the gui given thecurrent mouse position."""

        (w, h) = self.size
        (x, y) = mouse_pos

        size = self.buttons[0].content_height + 3 

        batch = pyglet.graphics.Batch()

        # Add the big bar under the buttons
        draw_polygon([
            (0, h     ),
            (w, h     ),
            (w, h - size),
            (0, h - size)
        ], (50, 50, 50), batch)

        for button in self.buttons:
            draw_polygon(
                [
                    (button.x                       , h),
                    (button.x + button.content_width, h),
                    (button.x + button.content_width, h - size),
                    (button.x                       , h - size),
                ],
                (80, 80, 80) if is_over_button(button, x, y) else (60, 60, 60),
                batch
            )

        batch.draw()

        # Draw the text for the buttons.
        for button in self.buttons:
            button.y = h
            button.draw()

    def is_over(self, mouse_pos):
        """Returns true if mouse is over the gui."""

        return False

    def button(self, name):
        def decorator(func):
            button = pyglet.text.Label(
                " " + name + " ",
                anchor_y="top",
                anchor_x="left",
                x = self.x
            )

            button.func = func

            self.buttons.append(button)

            self.x += button.content_width
            
            return lambda func: func

        return decorator

    def click(self, game):
        """Click that gui."""
        
        (x, y) = game.mouse.position

        for button in self.buttons:
            if is_over_button(button, x, y):
                return button.func(game)
        
            
