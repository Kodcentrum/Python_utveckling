import math

bug = Actor("bug")
bug.pos = 170, 80
bug.outside = False

WIDTH = 480
HEIGHT = 360
GREEN = (0, 255, 0)


def draw():
    screen.clear()
    screen.fill(GREEN)
    screen.blit("track", (0, 0))
    bug.draw()


def update():
    move(bug, 1)
    stop_at_edge(bug)
    if touching_color(bug, GREEN):
        if not bug.outside:
            print("Outside")
        bug.outside = True
    else:
        if bug.outside:
            print("Inside")
        bug.outside = False


def on_key_down(key):
    if key == keys.LEFT:
        bug.angle += 15
    elif key == keys.RIGHT:
        bug.angle -= 15


def move(sprite, steps):
    radians = math.pi / 180.0 * sprite.angle
    dx = steps * math.cos(radians)
    dy = steps * math.sin(radians)
    sprite.left += dx
    sprite.top -= dy


def stop_at_edge(sprite):
    if sprite.right >= WIDTH:
        sprite.right = WIDTH
    elif sprite.left <= 0:
        sprite.left = 0
    if sprite.bottom >= HEIGHT:
        sprite.bottom = HEIGHT
    elif sprite.top <= 0:
        sprite.top = 0


def touching_color(sprite, color):
    def _scan_y(dx):
        # Scan the contour of the sprite from top to middle
        for y in range(ymin, halfheight + 1):
            if sprite._surf.get_at((x, y))[3] == 0:  # If transparent
                continue
            worldx = int(sprite.left + x - dx)
            worldy = int(sprite.top + y - 1)
            return screen.surface.get_at((worldx, worldy)) == color
        # Scan the contour of the sprite from bottom to middle
        for y in range(ymax, halfheight - 1, -1):
            if sprite._surf.get_at((x, y))[3] == 0:
                continue
            worldx = int(sprite.left + x - dx)
            worldy = int(sprite.top + y + 1)
            return screen.surface.get_at((worldx, worldy)) == color
        return False

    xmin, ymin, xmax, ymax = sprite._surf.get_bounding_rect()
    halfwidth = int(0.5 * (xmax - xmin))
    halfheight = int(0.5 * (xmax - xmin))
    # Scan the contour of the sprite from left to middle
    for x in range(xmin, halfwidth + 1):
        if _scan_y(dx=-1):
            return True
    # Scan the contour of the sprite from right to middle
    for x in range(xmax, halfwidth - 1, -1):
        if _scan_y(dx=+1):
            return True
    return False
