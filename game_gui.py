import tkinter as tk
from tkinter import ttk, messagebox
import game_modules as mod

class GameApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Player Name")
        self.root.geometry("300x100")
        
        self.name = tk.StringVar()
        
        ttk.Label(self.root, text="Enter Player Name:").pack(pady=5)
        ttk.Entry(self.root, textvariable=self.name).pack(pady=5)
        ttk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=5)
        
        self.root.mainloop()
    
    def start_game(self):
        if not self.name.get().strip():
            messagebox.showerror("Error", "Please enter a valid name!")
            return
            
        self.root.destroy()
        MainWindow(self.name.get())

class MainWindow:
    def __init__(self, name):
        self.name = name
        self.attempt = 0
        self.life_score = mod.lifescore()
        self.enemy_numbers = []
        
        self.window = tk.Tk()
        self.window.title("Number Combat Game")
        self.window.geometry("600x400")
        
        # Game Info Frame
        info_frame = ttk.Frame(self.window)
        info_frame.pack(pady=10)
        
        self.attempt_label = ttk.Label(info_frame, text=f"Attempt: 0")
        self.attempt_label.pack(side=tk.LEFT, padx=20)
        
        self.score_label = ttk.Label(info_frame, text=f"Life Score: {self.life_score}")
        self.score_label.pack(side=tk.LEFT, padx=20)
        
        # Enemy Numbers Frame
        self.enemy_frame = ttk.Frame(self.window)
        self.enemy_frame.pack(pady=20)
        
        # Input Frame
        input_frame = ttk.Frame(self.window)
        input_frame.pack(pady=20)
        
        ttk.Label(input_frame, text="Select number to fight:").pack(side=tk.LEFT)
        self.fight_entry = ttk.Entry(input_frame, width=15)
        self.fight_entry.pack(side=tk.LEFT, padx=10)
        ttk.Button(input_frame, text="Fight!", command=self.check_fight).pack(side=tk.LEFT)
        
        # Status Frame
        self.status_label = ttk.Label(self.window, text="", foreground="red")
        self.status_label.pack(pady=10)
        
        self.start_new_attempt()
        
        self.window.mainloop()
    
    def start_new_attempt(self):
        self.attempt += 1
        if self.attempt > 20:
            self.game_over(True)
            return
            
        self.attempt_label.config(text=f"Attempt: {self.attempt}")
        self.enemy_numbers = mod.enemy(self.attempt)
        
        # Clear previous enemy numbers
        for widget in self.enemy_frame.winfo_children():
            widget.destroy()
        
        # Display new enemy numbers
        for num in self.enemy_numbers:
            ttk.Label(self.enemy_frame, text=str(num), padding=5).pack(side=tk.LEFT)
    
    def check_fight(self):
        fight_num = self.fight_entry.get()
        self.fight_entry.delete(0, tk.END)
        
        try:
            num = int(fight_num)
        except ValueError:
            self.show_error("Invalid input! Please enter a number.")
            return
            
        if num not in self.enemy_numbers:
            self.show_error("No such enemy!")
            self.game_over()
            return
            
        if num > self.life_score:
            self.status_label.config(text=f"{num} killed {self.name}!")
            self.game_over()
            return
            
        self.life_score += num
        self.score_label.config(text=f"Life Score: {self.life_score}")
        self.status_label.config(text=f"{self.name} killed {num}!", foreground="green")
        self.window.after(1000, self.start_new_attempt)
    
    def show_error(self, message):
        self.status_label.config(text=message, foreground="red")
    
    def game_over(self, victory=False):
        if victory:
            message = f"{self.name} saved letter-kind!"
        else:
            message = f"{self.name} was defeated!"
        
        # Save game status
        filename = mod.filename()
        with open(filename, "w") as f:
            f.write("***Game status***\n")
            f.write(f"Player name: {self.name}\n")
            f.write(f"Final score: {self.life_score}\n")
            f.write(f"Total attempts: {self.attempt}\n")
            f.write(message)
        
        # Show final message
        final_text = (
            f"Game Status\n"
            f"Player name: {self.name}\n"
            f"Total attempts: {self.attempt}\n"
            f"Final life score: {self.life_score}\n"
            f"{message}"
        )
        messagebox.showinfo("Game Over", final_text)
        self.window.destroy()

if __name__ == "__main__":
    GameApp()