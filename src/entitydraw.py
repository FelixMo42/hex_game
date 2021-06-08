import pyglet

def draw_sprite(entity):
    """ Draw this entity onscreen by creating a sprite and drawing it
    """
    image = pyglet.image.load('static/' + img_name)
    sprite = pyglet.sprite.Sprite(image, 0, 0)
    
    pixel_cord = cord_to_pixel(entity.cord, 60)
    sprite.x = pixel_cord[0]
    sprite.y = pixel_cord[1]
    sprite.draw()
