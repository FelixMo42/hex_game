class Mouse:
    def set_mouse_pos(self, x, y):
        """Set the mouse position."""

        self.mouse_pos = (x, y)

    def drag_start(self, x, y):
        """Called to triger the start of a drag."""

        self.drag_start_pos = (x, y)

    def drag_end(self, x, y):
        """Called to potentially end a drag. Returns true if it was a drag."""

        was_drag = self.drag_start_pos != (x, y)

        del self.drag_start_pos

        return was_drag
