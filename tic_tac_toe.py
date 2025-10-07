import tkinter as tk
from tkinter import messagebox
import pygame

pygame.mixer.init()
pygame.mixer.music.load("bs_tictactoe.mp3")  
pygame.mixer.music.play(-1) 

click_sound = pygame.mixer.Sound("toy-button.mp3")

root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]


def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        click_sound.play() 
        buttons[row][col]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Game Over", f"Pemain {current_player} Menang!")
            reset_game()
        elif all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Game Over", "Seri!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player
    current_player = "X"
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = ""

# ==== Fungsi Menu ====
def show_game():
    menu_frame.pack_forget()
    game_frame.pack(padx=20, pady=20)
    reset_game()

def show_options():
    messagebox.showinfo("Option", "Maaf ya belum ada opsi tambahan 😊")

def exit_game():
    root.destroy()
    pygame.mixer.music.stop()

def back_to_menu():
    game_frame.pack_forget()
    menu_frame.pack()

# ==== Frame Menu ====
menu_frame = tk.Frame(root, bg="#87CEFA")
tk.Label(menu_frame, text="Tic Tac Toe", font=("Arial", 30, "bold"), bg="#87CEFA", fg="white").pack(pady=30)

tk.Button(menu_frame, text="Mulai", font=("Arial", 18, "bold"), width=12, 
          bg="#32CD32", fg="white", activebackground="#228B22", command=show_game).pack(pady=10)
tk.Button(menu_frame, text="Option", font=("Arial", 18, "bold"), width=12, 
          bg="#FFA500", fg="white", activebackground="#FF8C00", command=show_options).pack(pady=10)
tk.Button(menu_frame, text="Keluar", font=("Arial", 18, "bold"), width=12, 
          bg="#DC143C", fg="white", activebackground="#8B0000", command=exit_game).pack(pady=10)

menu_frame.pack(fill="both", expand=True)

# ==== Frame Game ====
game_frame = tk.Frame(root, bg="#1E3D59")

title_label = tk.Label(game_frame, text="Tic Tac Toe", font=("Arial", 20, "bold"), bg="#1E3D59", fg="white")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(game_frame, text="", font=("Arial", 26, "bold"), width=5, height=2,
                                  bg="#F0E68C", fg="black", activebackground="#FFD700",
                                  command=lambda r=r, c=c: on_click(r, c))
        buttons[r][c].grid(row=r+1, column=c, padx=5, pady=5)

back_btn = tk.Button(game_frame, text="⮌ Menu", font=("Arial", 14, "bold"),
                     bg="#FF6347", fg="white", activebackground="#CD5C5C",
                     command=back_to_menu)
back_btn.grid(row=4, column=0, columnspan=3, pady=15)

# ==== Efek Hover (Glow) ====
def add_glow_effect(widget, normal_color="#32CD32", glow_color="#90EE90", steps=10, interval=30):
    """Menambahkan efek cahaya lembut saat mouse diarahkan (hover)"""
    def hex_to_rgb(h):
        h = h.lstrip("#")
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    def rgb_to_hex(rgb):
        return "#" + "".join(f"{v:02x}" for v in rgb)

    normal_rgb = hex_to_rgb(normal_color)
    glow_rgb = hex_to_rgb(glow_color)
    diff = [(glow_rgb[i] - normal_rgb[i]) / steps for i in range(3)]

    def animate_glow(step=0):
        if step > steps:
            return
        new_rgb = [int(normal_rgb[i] + diff[i] * step) for i in range(3)]
        widget.config(bg=rgb_to_hex(new_rgb))
        widget.after(interval, lambda: animate_glow(step+1))

    def animate_fade(step=0):
        if step > steps:
            return
        new_rgb = [int(glow_rgb[i] - diff[i] * step) for i in range(3)]
        widget.config(bg=rgb_to_hex(new_rgb))
        widget.after(interval, lambda: animate_fade(step+1))

    widget.bind("<Enter>", lambda e: animate_glow())   # ketika mouse masuk
    widget.bind("<Leave>", lambda e: animate_fade())   # ketika mouse keluar

# ==== Efek Hover (Glow) ====
def add_glow_effect(widget, normal_color="#32CD32", glow_color="#90EE90", steps=10, interval=30):
    """Menambahkan efek cahaya lembut saat mouse diarahkan (hover)"""
    def hex_to_rgb(h):
        h = h.lstrip("#")
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    def rgb_to_hex(rgb):
        return "#" + "".join(f"{v:02x}" for v in rgb)

    normal_rgb = hex_to_rgb(normal_color)
    glow_rgb = hex_to_rgb(glow_color)
    diff = [(glow_rgb[i] - normal_rgb[i]) / steps for i in range(3)]

    def animate_glow(step=0):
        if step > steps:
            return
        new_rgb = [int(normal_rgb[i] + diff[i] * step) for i in range(3)]
        widget.config(bg=rgb_to_hex(new_rgb))
        widget.after(interval, lambda: animate_glow(step+1))

    def animate_fade(step=0):
        if step > steps:
            return
        new_rgb = [int(glow_rgb[i] - diff[i] * step) for i in range(3)]
        widget.config(bg=rgb_to_hex(new_rgb))
        widget.after(interval, lambda: animate_fade(step+1))

    widget.bind("<Enter>", lambda e: animate_glow())   # ketika mouse masuk
    widget.bind("<Leave>", lambda e: animate_fade())   # ketika mouse keluar


root.mainloop()
