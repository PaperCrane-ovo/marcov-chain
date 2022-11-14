from readmatrix import ReadMatrix
from music_gen import MusicGen
import numpy as np
songs = ['平凡之路','晴天','mopemope']

def merge_matrix(prob_matrix_list):
    near_matrix = np.divide(np.add(prob_matrix_list[0], prob_matrix_list[1]),2)
    far_matrix = np.divide(np.add(prob_matrix_list[0], prob_matrix_list[2]),2)
    return (near_matrix, far_matrix)

def main():
    prob_matrix_list = []

    for song in songs:
        filename = song + '.txt'
        readmatrix = ReadMatrix(filename,dimension=1)
        prob_matrix = readmatrix.read()
        prob_matrix_list.append(prob_matrix)
    
    near_matrix, far_matrix = merge_matrix(prob_matrix_list)

    near_music = MusicGen(name = 'near',matrix = near_matrix)
    far_music = MusicGen(name = 'far',matrix = far_matrix)
    
    near_music.gen()
    far_music.gen()
if __name__ == "__main__":
    main()
    
