class Mouse:

    # Start the mouse off the screen so that it shouldnt be on top of anything
    position = (-1, -1)

    # Start off not draggin
    drag_start_pos = None

    def set_mouse_pos(self, x, y):
        """Set the mouse position."""

        self.position = (x, y)

    def drag_start(self, x, y):
        """Called to triger the start of a drag."""

        self.drag_start_pos = (x, y)

    def drag_end(self, x, y):
        """Called to potentially end a drag. Returns true if it was a drag."""

        was_drag = self.drag_start_pos != None and self.drag_start_pos != (x, y)

        # Clear the drag.
        self.drag_start_pos = None

        return was_drag

    def is_drag(self):
        """Returns whether the mouse is currently being dragged."""

        return self.drag_start_pos != None
