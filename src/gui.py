import pyglet
from .camera import Camera
from .polydraw import draw_polygon

class Gui:
    camera = Camera()
    
    def __init__(self):
        parts = ["testing", "cool"]

        self.buttons = [] 
        
        x = 0

        for part in parts :
            label = pyglet.text.Label(
                " " + part + " ",
                anchor_y="top",
                anchor_x="left",
                x = x
            )

            self.buttons.append(label)

            x += label.content_width


    def draw(self):
        (w, h) = self.size

        size = self.buttons[0].content_height + 3 

        batch = pyglet.graphics.Batch()

        draw_polygon([
            (0, h     ),
            (w, h     ),
            (w, h - size),
            (0, h - size)
        ], (50, 50, 50), batch)

        for button in self.buttons:
            draw_polygon([
                (button.x, h),
                (button.x + button.content_width, h),
                (button.x + button.content_width, h - size),
                (button.x, h - size),
            ], (60, 60, 60), batch)

        batch.draw()

        for button in self.buttons:
            button.y = h
            button.draw()
            
