import tkinter as tk
import random

class FloppyBird:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Floppy Bird")
        self.canvas = tk.Canvas(self.root, width=400, height=600, bg='skyblue')
        self.canvas.pack()

        self.start_button = tk.Button(self.root, text="Start Game", font=("Arial", 16), command=self.start_game)
        self.start_button.place(x=150, y=270)

        self.root.mainloop()

    def start_game(self):
        self.start_button.destroy()
        self.canvas.delete("all")

        self.bird = self.canvas.create_oval(50, 250, 80, 280, fill='yellow')
        self.bird_speed = 0

        self.pipe_width = 60
        self.pipe_gap = 150
        self.pipe_x = 400
        self.pipes = []
        self.passed_pipe = False  # Track whether bird passed the pipe
        self.create_pipes()

        self.score = 0
        self.score_text = self.canvas.create_text(200, 30, text="Score: 0", font=("Arial", 20), fill="white")

        self.game_running = True
        self.root.bind("<space>", self.jump)
        self.move()

    def create_pipes(self):
        pipe_height = random.randint(100, 300)
        self.pipe_top = self.canvas.create_rectangle(
            self.pipe_x, 0, self.pipe_x + self.pipe_width, pipe_height, fill="green"
        )
        self.pipe_bottom = self.canvas.create_rectangle(
            self.pipe_x, pipe_height + self.pipe_gap, self.pipe_x + self.pipe_width, 600, fill="green"
        )
        self.pipes = [self.pipe_top, self.pipe_bottom]
        self.passed_pipe = False

    def jump(self, event):
        if self.game_running:
            self.bird_speed = -10

    def move(self):
        if not self.game_running:
            return

        self.bird_speed += 1
        self.canvas.move(self.bird, 0, self.bird_speed)

        for pipe in self.pipes:
            self.canvas.move(pipe, -5, 0)

        self.check_collision()
        self.check_score()

        pipe_coords = self.canvas.coords(self.pipes[0])
        if pipe_coords[2] < 0:
            self.canvas.delete(self.pipes[0])
            self.canvas.delete(self.pipes[1])
            self.create_pipes()

        self.root.after(30, self.move)

    def check_collision(self):
        bird_coords = self.canvas.coords(self.bird)
        top_coords = self.canvas.coords(self.pipes[0])
        bottom_coords = self.canvas.coords(self.pipes[1])

        if (bird_coords[2] > top_coords[0] and bird_coords[0] < top_coords[2]):
            if (bird_coords[1] < top_coords[3] or bird_coords[3] > bottom_coords[1]):
                self.end_game()
        if bird_coords[3] >= 600 or bird_coords[1] <= 0:
            self.end_game()

    def check_score(self):
        if not self.passed_pipe:
            pipe_coords = self.canvas.coords(self.pipes[0])
            bird_coords = self.canvas.coords(self.bird)

            if bird_coords[0] > pipe_coords[2]:
                self.score += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                self.passed_pipe = True

    def end_game(self):
        self.game_running = False
        self.canvas.create_text(200, 250, text="Game Over", font=("Arial", 24), fill="red")
        self.play_again_button = tk.Button(self.root, text="Play Again", font=("Arial", 14), command=self.restart_game)
        self.play_again_button.place(x=150, y=300)

    def restart_game(self):
        self.play_again_button.destroy()
        self.canvas.delete("all")
        self.start_game()


# Run the game
obj = FloppyBird()
obj.start()
