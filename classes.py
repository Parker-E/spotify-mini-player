import tkinter as tk


class TitleBar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        # Title bar
        titleBar = tk.Frame(self)
        titleBar.pack(pady=10, fill='x')
        tk.Button(titleBar, text='X', command=self.clickExit).pack(side='right')

    def clickExit(self, *args):
        print('Clicked exit')
        self.master.master.destroy()


class Login(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        # Login Frame
        self.loginContainer = tk.Frame(self)
        self.loginContainer.pack(padx=35, pady=15)

        username = tk.Frame(self.loginContainer)
        username.pack(padx=10, pady=10)
        tk.Label(username, text='Username').pack(side='left')
        self.usernameInput = tk.Entry(username, exportselection=0).pack(side='right')

        pw = tk.Frame(self.loginContainer)
        pw.pack(padx=10, pady=10)
        tk.Label(pw, text='Password').pack(side='left')
        self.passwordInput = tk.Entry(pw, exportselection=0, show='*').pack(side='right')

        tk.Button(self.loginContainer, text='Login', command=self.clickLogin).pack()

        self.master.master.bind('<Return>', self.clickLogin)

    def clickLogin(self, *args):
        print('clicked login')
        # un = self.unEntry.get()
        # pw = self.pwEntry.get()


class Player(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.pack()
        self.master.title("mini player")

        # no resizing
        self.master.resizable(False, False)
        # bg color
        self.master.tk_setPalette(background='#121212')
        # set size and location
        winX = int((self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2)
        winY = int((self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3)
        self.master.geometry("200x200+{}+{}".format(winX, winY))

        # Frames
        self.titleBar = TitleBar(self)
        self.login = Login(self)
        # pack frames
        self.titleBar.pack(side='top', fill='x')
        self.login.pack(fill='y')


if __name__ == '__main__':
    root = tk.Tk()
    # root.overrideredirect(True)
    player = Player(root)
    player.mainloop()










