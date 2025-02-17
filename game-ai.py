import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []

        self.create_buttons()
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.master, text=" ", font=('Arial', 24), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O"
                self.ai_move()

    def ai_move(self):
        available_moves = [i for i in range(9) if self.board[i] == " "]
        move = self.minimax(self.board, "O")  # AI plays as "O"
        self.board[move] = "O"
        self.buttons[move].config(text="O")
        if self.check_winner():
            messagebox.showinfo("Game Over", "Player O wins!")
            self.reset_game()
        elif " " not in self.board:
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
        else:
            self.current_player = "X"

    def minimax(self, board, player):
        available_moves = [i for i in range(9) if board[i] == " "]
        if self.check_winner() == "X":
            return -1
        elif self.check_winner() == "O":
            return 1
        elif not available_moves:
            return 0

        if player == "O":
            best_score = -float('inf')
            best_move = random.choice(available_moves)
            for move in available_moves:
                board[move] = "O"
                score = self.minimax(board, "X")
                board[move] = " "
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move
        else:
            best_score = float('inf')
            best_move = random.choice(available_moves)
            for move in available_moves:
                board[move] = "X"
                score = self.minimax(board, "O")
                board[move] = " "
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_move

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
            (0, 4, 8), (2, 4, 6)              # diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return self.board[combo[0]]
        return None

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
