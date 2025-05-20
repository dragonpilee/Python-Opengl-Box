import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image

# Rotation angles
rotate_x = 0
rotate_y = 0
dragging = False
last_mouse_pos = [0, 0]

texture_id = None

def load_texture(path):
    img = Image.open(path)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = img.convert("RGB").tobytes()

    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.width, img.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

    return tex_id

def draw_textured_cube():
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)

    # Front face
    glTexCoord2f(0, 0); glVertex3f(-1, -1,  1)
    glTexCoord2f(1, 0); glVertex3f( 1, -1,  1)
    glTexCoord2f(1, 1); glVertex3f( 1,  1,  1)
    glTexCoord2f(0, 1); glVertex3f(-1,  1,  1)

    # Back face
    glTexCoord2f(1, 0); glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 1); glVertex3f(-1,  1, -1)
    glTexCoord2f(0, 1); glVertex3f( 1,  1, -1)
    glTexCoord2f(0, 0); glVertex3f( 1, -1, -1)

    # Top face
    glTexCoord2f(0, 1); glVertex3f(-1,  1, -1)
    glTexCoord2f(0, 0); glVertex3f(-1,  1,  1)
    glTexCoord2f(1, 0); glVertex3f( 1,  1,  1)
    glTexCoord2f(1, 1); glVertex3f( 1,  1, -1)

    # Bottom face
    glTexCoord2f(1, 1); glVertex3f(-1, -1, -1)
    glTexCoord2f(0, 1); glVertex3f( 1, -1, -1)
    glTexCoord2f(0, 0); glVertex3f( 1, -1,  1)
    glTexCoord2f(1, 0); glVertex3f(-1, -1,  1)

    # Right face
    glTexCoord2f(1, 0); glVertex3f( 1, -1, -1)
    glTexCoord2f(1, 1); glVertex3f( 1,  1, -1)
    glTexCoord2f(0, 1); glVertex3f( 1,  1,  1)
    glTexCoord2f(0, 0); glVertex3f( 1, -1,  1)

    # Left face
    glTexCoord2f(0, 0); glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0); glVertex3f(-1, -1,  1)
    glTexCoord2f(1, 1); glVertex3f(-1,  1,  1)
    glTexCoord2f(0, 1); glVertex3f(-1,  1, -1)

    glEnd()
    glDisable(GL_TEXTURE_2D)

def key_callback(window, key, scancode, action, mods):
    global rotate_x, rotate_y
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_LEFT:
            rotate_y -= 5
        elif key == glfw.KEY_RIGHT:
            rotate_y += 5
        elif key == glfw.KEY_UP:
            rotate_x -= 5
        elif key == glfw.KEY_DOWN:
            rotate_x += 5
        elif key == glfw.KEY_ESCAPE:
            glfw.set_window_should_close(window, True)

def mouse_button_callback(window, button, action, mods):
    global dragging
    if button == glfw.MOUSE_BUTTON_LEFT:
        dragging = action == glfw.PRESS

def cursor_position_callback(window, xpos, ypos):
    global last_mouse_pos, rotate_x, rotate_y, dragging
    if dragging:
        dx = xpos - last_mouse_pos[0]
        dy = ypos - last_mouse_pos[1]
        rotate_x += dy * 0.5
        rotate_y += dx * 0.5
    last_mouse_pos[0] = xpos
    last_mouse_pos[1] = ypos

def main():
    global texture_id

    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)

    window = glfw.create_window(800, 600, "3D Textured Cube with Mouse and Keyboard", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glfw.set_key_callback(window, key_callback)
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_cursor_pos_callback(window, cursor_position_callback)

    glEnable(GL_DEPTH_TEST)
    glClearColor(0.1, 0.1, 0.1, 1)

    texture_id = load_texture("crate.png")  # <-- Make sure crate.png is in your folder

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 800 / 600, 0.1, 100)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -6)
        glRotatef(rotate_x, 1, 0, 0)
        glRotatef(rotate_y, 0, 1, 0)

        draw_textured_cube()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
