import pandas as pd
import numpy as np

class Point:
    def __init__(self, df, table):
        data = df[table]
        
        x = data['x']
        y = data['y']
        
        self.positions = np.dstack((x, y))[0]
    
    @staticmethod
    def dist(p1, p2):
        return np.linalg.norm(p1.positions - p2.positions, axis=1)
        
class Obj(Point):
    def __init__(self, df, table):
        super(Obj, self).__init__(df, table)
        
        self.median_array = np.repeat(
            np.expand_dims(np.median(self.positions, axis=0), axis=0),
            len(self.positions),
            axis=0
        )
        
        self.median_coordinates = self.median_array[0]

class Vector():
    def __init__(self, p1, p2, normalize=True):
        self.positions = p2.positions - p1.positions
        
        self.norm = np.linalg.norm(self.positions, axis=1)
        
        if normalize:
            self.positions = self.positions / np.repeat(
                np.expand_dims(
                    self.norm,
                    axis=1
                ),
                2,
                axis=1
            )
    
    @staticmethod
    def angle(v1, v2):
        length = len(v1.positions)
        
        angle = np.zeros(length)
        
        for i in range(length):
            angle[i] = np.rad2deg(
                np.arccos(
                    np.dot(
                        v1.positions[i], v2.positions[i]
                    )
                )
            )
            
        return angle
