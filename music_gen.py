import pysynth
import random
import numpy as np
import tools
class MusicGen:
    '''
    使用pysynth生成音乐
    或者只生成一段序列
    '''
    
    def __init__(self,name,matrix=None,time = 100,dimension = 1,type = 'text') -> None:
        '''
        name: 音乐名
        matrix: 概率转移矩阵
        time: 音乐时长
        dimension: 矩阵维度,对应dimension-1阶马尔可夫链
        type: 生成的音乐类型,默认为文本,可选为music
        '''
        self.name = name
        self.matrix = matrix
        self.time = time
        self.dimension = dimension
        self.type = type

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
        if self.dimension ==1:
            result = self.gen_with_2d_matrix(musics)
        elif self.dimension == 2:
            result = self.gen_with_3d_matrix(musics)
        with open(self.name+'.txt','w') as f:
            for music in result:
                f.write(music[0]+','+music[1]+';')
        if self.type == 'music':
            pysynth.make_wav(result,fn = self.name+'.wav')
        
        '''

        pysynth.make_wav(musics,fn = self.name+'.wav')
        '''
    
    def gen_with_2d_matrix(self,musics):
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
        return musics
    def gen_with_3d_matrix(self,musics):
        second_note = random.choice(tools.notes)
        second_octave = random.choice(tools.octaves)
        second_duration = random.choice(tools.durations)
        second = (second_note+second_octave,second_duration)
        musics.append(second)
        for i in range(self.time-1):
            first_note = musics[i][0]
            '''
            first_octave = first_note[-1]
            first_duration = musics[i][1]
            '''
            first_note = first_note[:-1]
            second_note = musics[i+1][0]
            second_octave = second_note[-1]
            second_duration = musics[i+1][1]
            second_note = second_note[:-1]
            first_index = tools.relations[first_note]
            second_index = tools.relations[second_note]

            prob = self.matrix[first_index][second_index]
            next_note = np.random.choice(tools.notes,p=prob)
            next_octave = second_octave
            next_duration = second_duration
            if next_note == 'c':
                next_octave = str(int(second_octave)+1)
            elif next_note == 'b':
                next_octave = str(int(second_octave)-1)
            next = (next_note+next_octave,next_duration)
            musics.append(next)
        return musics


