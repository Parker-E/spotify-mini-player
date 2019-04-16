import os
import spotipy
import spotipy.util as util
import json
import requests
from PIL import Image
from PIL import ImageTk


SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = 'http://localhost/'


class PlayerController():
    def __init__(self):
        self.token = ''
        self.spController = None
        self.playbackState = None

    def getToken(self, username):
        if not self.token:
            scope = 'user-library-read playlist-read-private playlist-read-collaborative user-read-playback-state user-read-private user-modify-playback-state user-read-currently-playing streaming'
            self.token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)
            self.spController = spotipy.Spotify(auth=self.token)
        return self.token

    def getTokenCache(self):
        cd = os.getcwd()
        for root, dirs, files in os.walk(cd):
            for file in files:
                if '.cache-' in file:
                    with open(file, 'r') as cacheFile:
                        return json.load(cacheFile), file[7:]
        return -1

    def refreshToken(self):
        scope = 'user-library-read playlist-read-private playlist-read-collaborative user-read-playback-state user-read-private user-modify-playback-state user-read-currently-playing streaming'
        cache, username = self.getTokenCache()
        if cache != -1:
            self.token = util.prompt_for_user_token(username, scope)
            self.spController = spotipy.Spotify(auth=self.token)
            return True
        else:
            return False

    def getPlayback(self):
        self.playbackState = self.spController.current_playback()['is_playing']
        return self.playbackState

    def setPlayback(self, playbackState):
        if self.spController:
            if playbackState:
                self.spController.start_playback()
                self.playbackState = playbackState
            else:
                self.spController.pause_playback()
                self.playbackState = playbackState
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
        if self.spController:
            return self.spController.next_track()
        pass

    def prevSong(self):
        if self.spController:
            return self.spController.previous_track()
        pass

    def getSongInfo(self):
        result = self.spController.current_user_playing_track()
        if result:
            info = {
                'artistName': result['item']['artists'][0]['name'],
                'durationms': result['item']['duration_ms'],
                'progressms': result['progress_ms'],
                'songName': result['item']['name'],
                'isPlaying': result['is_playing'],
                'albumArt': result['item']['album']['images'][0]
            }
            self.playbackState = result['is_playing']
            return info
        return False

    def getAlbumImage(self, albumArt):
        coverImage = ImageTk.PhotoImage(Image.open(requests.get(albumArt['url'], stream=True).raw).resize((140, 140), Image.ANTIALIAS))
        return coverImage


class FrameController():

    def __init__(self, appFrame):
        self.appFrame = appFrame

    def swapFrame(self, old, new):
        old.pack_forget()
        new.pack()

    def resizeWindow(self, h, w):
        self.appFrame.master.geometry("{}x{}+{}+{}".format(h, w, self.appFrame.winX, self.appFrame.winY))
        pass
