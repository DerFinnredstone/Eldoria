import tkinter as tk

# Größe des Spielbereichs
GAME_WIDTH = 800
GAME_HEIGHT = 600

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=GAME_WIDTH, height=GAME_HEIGHT)
        self.canvas.pack()

        self.player = self.canvas.create_rectangle(50, 50, 100, 100, fill='blue')

        # Bewegungsgeschwindigkeit des Spielers
        self.player_speed = 5

        self.canvas.bind('<KeyPress>', self.handle_key_press)
        self.canvas.bind('<KeyRelease>', self.handle_key_release)
        self.canvas.focus_set()
        self.canvas.after(16, self.update)

    def handle_key_press(self, event):
        if event.keysym == 'Up':
            self.move_player(0, -self.player_speed)
        elif event.keysym == 'Down':
            self.move_player(0, self.player_speed)
        elif event.keysym == 'Left':
            self.move_player(-self.player_speed, 0)
        elif event.keysym == 'Right':
            self.move_player(self.player_speed, 0)

    def handle_key_release(self, event):
        # Stoppen der Bewegung des Spielers beim Loslassen der Taste
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            self.move_player(0, 0)

    def move_player(self, dx, dy):
        self.canvas.move(self.player, dx, dy)

    def update(self):
        self.canvas.update()
        self.canvas.after(16, self.update)

root = tk.Tk()
root.title("Eldoria - Mein Spiel")

game = Game(root)

root.mainloop()
