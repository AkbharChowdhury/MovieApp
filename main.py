import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox, Treeview
from db import Database
from helper import Helper
from movie import Movie
from movie_genres import MovieGenres

db = Database()
movieGenre: MovieGenres = MovieGenres()


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Cinema Ticket Machine - List Movies')
        win_size = {'w': 1100, 'h': 300}
        master.geometry(f"{win_size.get('w')}x{win_size.get('h')}")
        self.create_widgets()

        # Populate initial list
        self.populate_list()

    def clear_list(self):
        for item in self.movie_list.get_children():
            self.movie_list.delete(item)

    def genre_selected(self, event):
        movieGenre.genre = self.cbGenre.get()
        self.populate_list()

    def title_text_search(self, evt):
        movieGenre.title = self.movie_entry.get()
        self.populate_list()

    def buttons(self):
        self.btn_list_movies = Button(
            self.master, text="list movies".title(), width=12)
        self.btn_list_movies.grid(row=0, column=0, pady=20)

        self.btn_show_times = Button(
            self.master, text="show times".title(), width=12)
        self.btn_show_times.grid(row=0, column=1)

        self.btn_purchase_ticket = Button(
            self.master, text="purchase ticket".title(), width=12)
        self.btn_purchase_ticket.grid(row=0, column=2)

        self.btn_show_receipt = Button(
            self.master, text="show receipt".title(), width=12)
        self.btn_show_receipt.grid(row=0, column=3)

    def movie_table(self):
        columns = Movie.columns()
        col_length = tuple([f"c{i}" for i, column in enumerate(columns, start=1)])

        self.movie_list = Treeview(self.master, column=col_length, show='headings', height=5)

        for i, column in enumerate(columns, start=1):
            self.movie_list.column(f"# {i}", anchor=CENTER)
            self.movie_list.heading(f"# {i}", text=column.capitalize())

        self.movie_list.grid(row=3, column=0, columnspan=3,
                             rowspan=4, pady=20, padx=20)

        scrollbar = Scrollbar(self.master)
        scrollbar.grid(row=3, column=3)
        self.movie_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.movie_list.yview)

    def create_widgets(self):

        self.movie_label = Label(
            self.master, text='movie title:'.title(), font=('bold', 14))
        self.movie_label.grid(row=1, column=0, sticky=tk.W)
        self.movie_entry = tk.Entry(
            self.master)
        self.movie_entry.grid(row=1, column=1)
        self.movie_entry.bind("<KeyRelease>", self.title_text_search)

        self.lblGenre = Label(
            self.master, text='Genre', font=('bold', 14))
        self.lblGenre.grid(row=1, column=2, sticky=tk.W)
        self.cbGenre = Combobox(self.master, state='readonly', width=20)
        movie_genres = [genre for genre in db.fetch_genres()]
        movie_genres.insert(0, MovieGenres.default_genre())
        self.cbGenre['values'] = movie_genres
        self.cbGenre.current(0)
        self.cbGenre.grid(row=1, column=3)
        self.cbGenre.bind('<<ComboboxSelected>>', self.genre_selected)

        self.movie_table()

        self.buttons()

    def populate_list(self):
        self.clear_list()
        for row in db.show_movie_list(movieGenre):
            title = row[0]
            duration = Helper.calc_duration(int(row[1]))
            rating = row[2]
            genre = row[3]
            movie_list = (title, duration, rating, genre)
            self.movie_list.insert('', 'end', text="1", values=movie_list)


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
