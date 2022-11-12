import pysynth
import random
import numpy as np
class MusicGen:
    def __init__(self,name,matrix=None,time = 100) -> None:
        self.name = name
        self.matrix = matrix
        self.notes = ['c','d','e','f','g','a','b']
        self.relation = {'c':0,'d':1,'e':2,'f':3,'g':4,'a':5,'b':6}
        self.octaves = [3,4,5,6]
        self.durations = ['4','8','16','32']
        self.time = time
    def gen(self):
        if self.matrix is None:
            return 
        init_note = random.choice(self.notes)
        init_octave = random.choice(self.octaves)
        init_duration = random.choice(self.durations)
        init = (init_note,init_octave,init_duration)
        music = [init]
        for i in range(self.time):
            note = music[i][0]
            octave = music[i][1]
            duration = music[i][2]
            note_index = self.relation[note]
            prob = self.matrix[note_index]
            next_note=np.random.choice(self.notes,p=prob)
            next_octave = octave
            next_duration = duration
            music.append((next_note,next_octave,next_duration))
        pysynth.make_wav(music,fn = self.name+'.wav')

