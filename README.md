# OpenGL Textured Cube

## Overview
A simple, interactive 3D textured cube application built with Python, OpenGL, and GLFW. The application displays a rotating cube that can be manipulated using both keyboard controls and mouse movements.

![OpenGL Cube Demo](https://github.com/yourusername/opengl-cube/raw/main/screenshot.png)

## Features
- 3D textured cube rendering
- Interactive rotation with keyboard controls
- Mouse-based rotation via click and drag
- Texture mapping from an image file

## Requirements
- Python 3.x
- OpenGL
- GLFW
- PIL (Python Imaging Library) / Pillow

## Installation

### 1. Clone the repository
git clone https://github.com/yourusername/opengl-cube.git
cd opengl-cube

### 2. Install dependencies
pip install pyopengl pyopengl-accelerate glfw pillow

### 3. Prepare texture file
Ensure you have a texture file named crate.png in the project directory. If you don't have one, you can use any image file but remember to rename it to crate.png or update the code to use your file's name.

## Usage

Run the application:
python opengl_cube.py

### Controls
- Arrow Keys: Rotate the cube (Up, Down, Left, Right)
- Left Mouse Button + Drag: Rotate the cube following mouse movement
- ESC: Exit the application

## How It Works

The application uses:
- GLFW for window creation and input handling
- OpenGL for 3D rendering
- PIL/Pillow for loading texture images

The cube is drawn with texture coordinates mapping each face to the loaded texture. The rotation state is controlled by global variables that are updated based on user input.

## Code Structure

- Initialization: Sets up GLFW, creates a window, and initializes OpenGL
- Texture Loading: Loads and configures the texture from an image file
- Input Callbacks: Handles keyboard and mouse inputs
- Drawing: Renders the textured cube with proper transformations
- Main Loop: Updates the display and processes events

## Customization

- Change the texture by replacing crate.png with another image
- Modify the cube dimensions by changing the vertex coordinates
- Adjust the rotation sensitivity by modifying the multipliers in the mouse callback

## License

[MIT License](LICENSE)

## Acknowledgements

- The OpenGL and GLFW communities
- Contributors to the PyOpenGL and Pillow projects

---

Created by [Your Name]
