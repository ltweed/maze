from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Create the root widget
        self.__root = Tk()

        # Set the title of the window
        self.__root.title("Tkinter Window")

        # Create a canvas and save it as a data member
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)

        # Initialize the running state
        self.__running = False

        # Handle the "delete window" action
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        # Redraw the graphics in the window
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        # Set the running state to True
        self.__running = True

        # Keep redrawing while running
        while self.__running:
            self.redraw()

    def close(self):
        # Set the running state to False
        self.__running = False

# Main function
def main():
    # Create a window instance
    win = Window(800, 600)
    # Wait for the window to close
    win.wait_for_close()

if __name__ == "__main__":
    main()
