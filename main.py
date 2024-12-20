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
    if win is None:
        print("Failed to create a window.")
        return
    print("Window created...")
    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)
    print("Cell 1 created...")

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(100, 50, 150, 100)
    print("Cell 2 created...")

    c1.draw_move(c2)
    print("Cell 1 moved to Cell 2...")

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(100, 100, 150, 150)
    print("Cell 3 created...")

    c2.draw_move(c3)
    print("Cell 2 moved to Cell 3...")

    c4 = Cell(win)
    c4.has_left_wall = False
    c4.draw(150, 100, 200, 150)
    print("Cell 4 created...")

    c3.draw_move(c4, True)
    print("Cell 3 moved to Cell 4...")
    win.wait_for_close()

if __name__ == "__main__":
    main()

