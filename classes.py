import os
import tkinter as tk
import spotipy
import spotipy.util as util
import json

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = 'http://localhost/'


def getTokenCache():
    cd = os.getcwd()
    for root, dirs, files in os.walk(cd):
        for file in files:
            if '.cache-' in file:
                return True
                # with open(file, 'r') as cacheFile:
                #     return json.load(cacheFile)
    return -1


class PlayerController():
    def __init__(self, *args, **kwargs):
        self.token = ''
        self.spController = None

    def getToken(self, username):
        if not self.token:
            scope = ('user-library-read playlist-read-private playlist-read-collaborative user-read-playback-state user-read-private user-modify-playback-state user-read-currently-playing streaming')
            self.token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)
            self.spController = spotipy.Spotify(auth=self.token)
        return self.token

    def refreshToken(self):
        cache = getTokenCache()
        if cache != -1:
            self.spController = spotipy.Spotify(auth=self.token)
        pass

    def getPlayback(self):
        pass

    def setPlayback(self):
        pass

    def getVolume(self):
        pass

    def setVolume(self):
        pass

    def getPlaylist(self):
        pass

    def addToPlaylist(self):
        pass

    def getPlaylists(self):
        pass

    def playSong(self):
        pass

    def playPlaylist(self):
        pass

    def playRadio(self):
        pass

    def setPlayerOptions(self):
        pass

    def nextSong(self):
        pass

    def prevSong(self):
        pass

    def getSongInfo(self):
        pass


class FrameController():
    def __init__(self, *args, **kwargs):
        self.frame = args[0]

    def switchMainFrame(self, old, new):
        pass



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
        self.usernameInput = tk.Entry(username, exportselection=0)
        self.usernameInput.pack(side='right')
        self.usernameInput.focus_set()

        tk.Button(self.loginContainer, text='Login', command=self.clickLogin).pack()

        self.master.master.bind('<Return>', self.clickLogin)

    def clickLogin(self, *args):
        print('clicked login')
        username = self.usernameInput.get()
        self.master.controller.getToken(username)


class App(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.pack()
        self.master.title("mini player")
        self.pController = PlayerController()
        self.pController.refreshToken()

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
    app = App(root)
    app.mainloop()










