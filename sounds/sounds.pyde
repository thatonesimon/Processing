# Ex7.pyde
# Based on Java File in Examples: PlayAFile.pde

'''
This sketch demonstrates how to play a file with Minim
using an AudioPlayer. It's also a good example of how
to draw the waveform of the audio. Full documentation
for AudioPlayer can be found at http://
code.compartmental.net/minim/
audioplayer_class_audioplayer.html
For more information about Minim and additional features,
visit http://code.compartmental.net/minim/
'''

add_library('minim')

player = None

def setup():
    size(1024, 200)
    global player
    minim = Minim(this)
    player = minim.loadFile("song.mp3")
    
def draw():
    background(0)
    stroke(255)
    # draw the waveforms
    # the values returned by left.get() and right.get()
    # will be between -1 and 1, so we need to scale them
    # up to see the waveform. Note that if the file is
    # MONO, left.get() and right.get() will return the
    # same value
    for i in range(player.bufferSize()-1):
        x1 = map(i, 0, player.bufferSize(), 0, width)
        x2 = map(i+1, 0, player.bufferSize(), 0, width)
        line( x1, 50 + player.left.get(i)*50, 
             x2, 50 + player.left.get(i+1)*50 )
        line( x1, 150 + player.right.get(i)*50,
             x2, 150 + player.right.get(i+1)*50)
    posx = map(player.position(), 0, player.length(),
               0, width)
    stroke(0,200,0)
    line(posx, 0, posx, height)
    if player.isPlaying():
        text("Press any key to pause playback.", 10, 20)
    else:
        text("Press any key to start playback.", 10, 20)
        
def keyPressed():
    if player.isPlaying():
        player.pause()
    # if the player is at the end of the file,
    # we have to rewind it before telling it to
    # play again
    elif player.position() == player.length():
        player.rewind()
        player.play()
    else:
        player.play() 
