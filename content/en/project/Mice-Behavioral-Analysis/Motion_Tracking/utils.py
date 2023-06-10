import pandas as pd
import numpy as np

def suavizar(vec, n):
    kernel = [1 / n] * n
    return np.convolve(vec, kernel, "same")

class Punto:
    def __init__(self, df, tabla):
        data = df[tabla]
        
        x = suavizar(data['x'], 5)
        y = suavizar(data['y'], 5)
        
        self.posiciones = np.dstack((x, y))[0]
        
        
    
    @staticmethod
    def dist(p1, p2):
        return np.linalg.norm(p1.posiciones - p2.posiciones, axis=1)
        
class Obj(Punto):
    def __init__(self, df, tabla):
        super(Obj, self).__init__(df, tabla)
        
        self.posiciones = np.repeat(
            np.expand_dims(np.mean(self.posiciones, axis=0), axis=0),
            len(self.posiciones),
            axis=0
        )
        
class PuntoCuerpo(Punto):
    pass

class Vector():
    def __init__(self, p1, p2, normalizar=True):
        self.posiciones = p2.posiciones - p1.posiciones
        
        self.norm = np.linalg.norm(self.posiciones, axis=1)
        
        if normalizar:
            self.posiciones = self.posiciones / np.repeat(
                np.expand_dims(
                    self.norm,
                    axis=1
                ),
                2,
                axis=1
            )
            
    @staticmethod
    def cosine(v1, v2):
        length = len(v1.posiciones)
        cos = np.zeros(length)

        for i in range(length):
            cos[i] = np.dot(v1.posiciones[i], v2.posiciones[i])
            
        return cos
