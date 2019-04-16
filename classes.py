import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import time
from controllers import *


class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(fill='both')
        self.master.title("mini player")
        # no resizing
        self.master.resizable(False, False)
        # window bg color
        self.master.tk_setPalette(background='#121212')
        # set size and location
        self.winX = int((self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2)
        self.winY = int((self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3)
        self.master.geometry("300x300+{}+{}".format(self.winX, self.winY))

        # initialize frame controller
        self.fController = FrameController(self)

        # Pack parent frames
        self.titleBar = TitleBar(self)
        self.titleBar.pack(side='top', fill='x')
        self.mainContainer = MainContainer(self)
        self.mainContainer.pack(fill='both')

    def exit(self):
        return self.master.destroy()


class TitleBar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # Title bar
        titleBar = tk.Frame(self)
        titleBar.pack(fill='x')
        tk.Button(titleBar, text='X', command=self.clickExit).pack(side='right')

    def clickExit(self, *args):
        print('Clicked exit')
        self.master.exit()


class MainContainer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # initialize player controller
        self.pController = PlayerController()

        # check if we have token
        if self.pController.refreshToken():
            self.player = Player(self)
            self.player.pack(fill='both')
            self.master.fController.resizeWindow('600', '300')
            self.player.updateSongInfo()
        else:
            # pack login
            self.login = Login(self)
            self.login.pack(fill='y')
        pass


class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
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
        self.master.master.controller.getToken(username)


# info = {
#     'artistName': result['item']['artists'][0]['name'],
#     'durationms': result['item']['duration_ms'],
#     'progressms': result['progress_ms'],
#     'songName': result['item']['name'],
#     'isPlaying': result['is_playing']
# }
class Player(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pController = self.master.pController
        self.songInfo = False
        # body content container
        self.playerContentContainer = tk.Frame(self)
        self.playerContentContainer.pack(side='top', fill='both')
        # album art
        self.albumArtContainer = tk.Frame(self.playerContentContainer)
        self.albumArtContainer.pack(padx=20, side='left')
        defaultPhoto = ImageTk.PhotoImage(Image.open('resources/img/default-artwork.png').resize((140, 140), Image.ANTIALIAS))
        self.albumArt = tk.Label(self.albumArtContainer, image=defaultPhoto)
        self.albumArt.image = defaultPhoto
        self.albumArt.pack()
        # song info container
        self.songInfoContainer = tk.Frame(self.playerContentContainer, width=400)
        self.songInfoContainer.pack(fill='both')
        # song info
        self.songInfo = tk.Frame(self.songInfoContainer)
        self.songInfo.pack(side='top', fill='x')
        self.artistLabel = tk.Label(self.songInfo, text='Artist')
        self.artistLabel.pack(fill='x', side='left')
        self.songLabel = tk.Label(self.songInfo, text='- Song')
        self.songLabel.pack(padx=5, side='left')
        # volume slider
        self.volumeSliderStyle = ttk.Style()
        self.volumeSlider = ttk.Scale(self.songInfoContainer, orient='horizontal', length='200', from_=0, to_=100)
        self.volumeSlider.pack(pady=(50, 10), padx=5, side='left')
        # footer container
        self.playerFooterContainer = tk.Frame(self)
        self.playerFooterContainer.pack(expand=True, side='bottom', fill='both')
        # song progress bar
        self.progressBar = tk.Frame(self.playerFooterContainer, bg='#666666', width=600, height=4)
        self.progressBar.pack(side='top', pady=20)
        # control buttons container
        self.controlButtonsContainer = tk.Frame(self.playerFooterContainer, width=300)
        self.controlButtonsContainer.pack(side='left', fill='both', pady=20)
        # prev next buttons
        self.prevButton = tk.Button(self.controlButtonsContainer, text='<prev>', command=self.prevSong)
        self.prevButton.pack(side='left')
        self.nextButton = tk.Button(self.controlButtonsContainer, text='<next>', command=self.nextSong)
        self.nextButton.pack(side='right')
        # play/pause container and buttons
        self.playPauseContainer = tk.Frame(self.controlButtonsContainer)
        self.playPauseContainer.pack(pady=5)
        self.playButton = tk.Button(self.playPauseContainer, text='<play>', command=self.playPauseSong)
        self.playButton.pack()
        self.pauseButton = tk.Button(self.playPauseContainer, text='<pause>', command=self.playPauseSong)
        self.setPlaybackButtonState()

    def updateSongInfo(self):
        self.songInfo = self.pController.getSongInfo()
        self.artistLabel['text'] = self.songInfo['artistName']
        self.songLabel['text'] = '- ' + self.songInfo['songName']
        newAlbumArt = self.pController.getAlbumImage(self.songInfo['albumArt'])
        self.albumArt['image'] = newAlbumArt
        self.albumArt.image = newAlbumArt

    def setPlaybackButtonState(self):
        if self.pController.playbackState is None:
            self.pController.getPlayback()
        if self.pController.playbackState:
            self.master.master.fController.swapFrame(self.playButton, self.pauseButton)
        else:
            self.master.master.fController.swapFrame(self.pauseButton, self.playButton)
        pass

    def playPauseSong(self):
        if self.pController.playbackState:
            self.pController.setPlayback(not self.pController.playbackState)
            self.setPlaybackButtonState()
        else:
            self.pController.setPlayback(not self.pController.playbackState)
            self.setPlaybackButtonState()
        pass

    def nextSong(self):
        self.pController.nextSong()
        time.sleep(.3)
        self.updateSongInfo()
        pass

    def prevSong(self):
        self.pController.prevSong()
        time.sleep(.3)
        self.updateSongInfo()
        pass










if __name__ == '__main__':
    root = tk.Tk()
    # root.overrideredirect(True)
    app = App(root)
    app.mainloop()










