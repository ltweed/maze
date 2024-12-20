import ctypes
import sys
from graphics import Window, Line, Point
from cell import Cell

# Set DPI awareness (Windows only)
if sys.platform == "win32":  # Check if the platform is Windows
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except AttributeError:
        print("DPI awareness setting is not supported on this system.")
    except Exception as e:
        print(f"Failed to set DPI awareness: {e}")

def main():
    # Create a window instance
    win = Window(1600, 1200)  # Use a larger resolution

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)
    win.wait_for_close()

if __name__ == "__main__":
    main()

