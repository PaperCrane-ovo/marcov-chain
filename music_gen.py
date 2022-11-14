import pysynth
import random
import numpy as np
import tools
class MusicGen:
    '''
    使用pysynth生成音乐
    '''
    def __init__(self,name,matrix=None,time = 100,dimension = 1) -> None:
        '''
        name: 音乐名
        matrix: 概率转移矩阵
        time: 音乐时长
        dimension: 矩阵维度,对应dimension-1阶马尔可夫链
        '''
        self.name = name
        self.matrix = matrix
        self.time = time
        self.dimension = dimension
    def gen(self):
        '''
        生成音乐,保存在name.wav中
        '''
        if self.matrix is None:
            return 
        init_note = random.choice(tools.notes)
        init_octave = random.choice(tools.octaves)
        init_duration = random.choice(tools.durations)
        init = (init_note+init_octave,init_duration)
        musics = [init]
        for i in range(self.time):  
            note = musics[i][0]
            octave = note[-1]
            duration = musics[i][1]
            note = note[:-1]
            note_index = tools.relations[note]
            prob = self.matrix[note_index]
            next_note = np.random.choice(tools.notes,p=prob)
            next_octave = octave
            next_duration = duration
            if next_note == 'c':
                next_octave = str(int(octave)+1)
            elif next_note == 'b':
                next_octave = str(int(octave)-1)
            next = (next_note+next_octave,next_duration)
            musics.append(next)
        pysynth.make_wav(musics,fn = self.name+'.wav')

