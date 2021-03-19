import pynput
import music21
import pygame

freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 1024    # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)

class PianoKey:
    def __init__(self, tone, key):
        self.isKeyPress = False;
        self.key = key;
        self.stream = music21.stream.Stream();
        note = music21.note.Note(tone);
        note.duration.quarterLength = 16;
        self.stream.append(note);
        self.stream.write('midi', fp=key + ".mid");
        #self.player = pygame.mixer.music.load(key + ".mid");
    def KeyPress(self):
        print('{0} pressed'.format(self.key));
        self.player = pygame.mixer.music.load(self.key + ".mid");
        self.player = pygame.mixer.music.play();
        #self.player.play();
        return;
    def KeyRelease(self):
        print('{0} release'.format(self.key));
        #self.player = pygame.mixer.music.stop();
        #self.player = pygame.mixer.music.unload();
        #self.player.stop();
        return;

PianoKey_Setting = [['C', "'1'"], 
                    ['D', "'2'"],
                    ['E', "'3'"],
                    ['F', "'4'"],
                    ['G', "'5'"],
                    ['A', "'6'"],
                    ['B', "'7'"]];

Obj_PianoKeys = {};                    
                    
def initPiano():                    
    for setting in PianoKey_Setting:                
        Obj_PianoKeys[setting[1]] = (PianoKey(setting[0], setting[1]));

def on_press_fun(key):
    #print('{0} pressed'.format(key));
    print("key" + str(key));
    if(str(key) in Obj_PianoKeys):
        Obj_PianoKeys[str(key)].KeyPress();
    
def on_release_fun(key):
    #print('{0} release'.format(key));
    if(str(key) in Obj_PianoKeys):
        Obj_PianoKeys[str(key)].KeyRelease();
    if(key == pynput.keyboard.Key.esc):
        #Stop Listener
        return False;




if __name__ == "__main__":
    print("Hello World");
    initPiano();
    with pynput.keyboard.Listener(on_press = on_press_fun, on_release = on_release_fun) as listener:
        listener.join();
        
    