class Mouse:
    # Start the mouse off the screen so that it shouldnt be on top of anything
    position = (-1, -1)

    # Start off not draggin
    drag_start_pos = None

    def drag_start(self):
        """Called to trigger the start of a drag."""

        self.drag_start_pos = self.position

    def drag_end(self):
        """Called to potentially end a drag. Returns true if it was a drag."""

        was_drag = self.drag_start_pos != self.position

        # Clear the drag.
        self.drag_start_pos = None

        return was_drag

    def is_drag(self):
        """Returns whether the mouse is currently being dragged."""

        return self.drag_start_pos != None
