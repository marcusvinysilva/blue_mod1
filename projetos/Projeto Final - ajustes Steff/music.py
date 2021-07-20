def musica(a=False):
    from pygame import mixer
    
    if a:
        mixer.init()
        mixer.music.load('./Projeto/Projeto Final - Game IF/musicproj.mp3')
        mixer.music.play(loops=2)
    else:
        mixer.music.stop()