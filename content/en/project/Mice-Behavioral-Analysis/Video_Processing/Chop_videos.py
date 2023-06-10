import os
from moviepy.editor import VideoFileClip
from PyQt5 import QtWidgets, QtCore

class Chopper(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set up the GUI
        self.setWindowTitle('Video Chopper')
        self.resize(400, 100)

        self.folder_label = QtWidgets.QLabel('Select a folder to chop:')
        self.folder_button = QtWidgets.QPushButton('Browse')
        self.folder_button.clicked.connect(self.browse_folder)

        self.run_button = QtWidgets.QPushButton('Run')
        self.run_button.clicked.connect(self.run)
        
        self.start_label = QtWidgets.QLabel('Enter start time:')
        self.start_edit = QtWidgets.QTimeEdit()
        self.start_edit.setDisplayFormat("mm:ss")
        default_start = QtCore.QTime(0, 0, 2) # Set the default start time at 2 s
        self.start_edit.setTime(default_start)
        self.start = self.start_edit.time()
        self.start_edit.timeChanged.connect(lambda time: setattr(self, "start", time))
        
        self.end_label = QtWidgets.QLabel('Enter end time:')
        self.end_edit = QtWidgets.QTimeEdit()
        self.end_edit.setDisplayFormat("mm:ss")
        default_end = QtCore.QTime(0, 5, 2) # Set the default end time to 5 minutes after the start
        self.end_edit.setTime(default_end)
        self.end = self.end_edit.time()
        self.end_edit.timeChanged.connect(lambda time: setattr(self, "end", time))
        
        self.shift_label = QtWidgets.QLabel('Enter phase shift:')
        self.shift_edit = QtWidgets.QTimeEdit()
        self.shift_edit.setDisplayFormat("mm:ss")
        default_shift = QtCore.QTime(0, 0, 10)
        self.shift_edit.setTime(default_shift)
        self.shift = self.shift_edit.time()
        self.shift_edit.timeChanged.connect(lambda time: setattr(self, "shift", time))
        
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.folder_label)
        layout.addWidget(self.folder_button)
        layout.addWidget(self.run_button)
        layout.addWidget(self.start_label)
        layout.addWidget(self.start_edit)
        layout.addWidget(self.end_label)
        layout.addWidget(self.end_edit)
        layout.addWidget(self.shift_label)
        layout.addWidget(self.shift_edit)

        self.setLayout(layout)
        self.show()


    def browse_folder(self):
        """Open a file dialog to select a folder."""
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder')
        self.folder_button.setText(folder_path)
        self.folder_path = folder_path

    def run(self):
        """Process all videos in the selected folder."""
        if not hasattr(self, 'folder_path'):
            return

        # Create the "videos cortados" folder if it does not exist
        cortados_path = os.path.join(self.folder_path, 'videos cortados moviepy')
        if not os.path.exists(cortados_path):
            os.makedirs(cortados_path)

        # Get the list of video files in the folder
        filenames = os.listdir(self.folder_path)
        video_filenames = [filename for filename in filenames if os.path.splitext(filename)[1].lower() in ('.mp4', '.avi')]
        
        # Defino inicio y fin de los videos del lado izquierdo
        start = - (self.start.secsTo(QtCore.QTime(0, 0)))
        end = - (self.end.secsTo(QtCore.QTime(0, 0)))
        shift = - (self.shift.secsTo(QtCore.QTime(0, 0)))
        
        # Process each video file left side
        for video_filename in video_filenames:
            video_path = os.path.join(self.folder_path, video_filename)
            video = VideoFileClip(video_path).subclip(start, end)

            # Obtenemos la duración y las dimensiones del video
            self.duration = video.duration
            self.frame_width, self.frame_height = video.size
            
            # Create the output video writers
            video_name = os.path.splitext(video_filename)[0]
            video_izq_path = os.path.join(cortados_path, video_name + '_L.mp4')
            
            # Cortamos el video por la mitad
            video_izq = video.crop(x1 = 0, y1 = 0, x2 = self.frame_width//2, y2 = self.frame_height)
            video_der = video.crop(x1 = self.frame_width//2, y1 = 0, x2 = self.frame_width, y2 = self.frame_height)
            
            # Giramos los videos 90 grados en sentido antihorario
            video_izq_rotado = video_izq.rotate(90)
            
            # Guardamos los videos rotados
            video_izq_rotado.write_videofile(video_izq_path, fps = video.fps)
        
        # Defino inicio y fin de los videos del lado derecho
        start = start + shift
        end = end + shift
        
        # Process each video file right side
        for video_filename in video_filenames:
            video_path = os.path.join(self.folder_path, video_filename)
            video = VideoFileClip(video_path).subclip(start, end)

            # Obtenemos la duración y las dimensiones del video
            self.duration = video.duration
            self.frame_width, self.frame_height = video.size
            
            # Create the output video writers
            video_name = os.path.splitext(video_filename)[0]
            video_der_path = os.path.join(cortados_path, video_name + '_R.mp4')
            
            # Cortamos el video por la mitad
            video_der = video.crop(x1 = self.frame_width//2, y1 = 0, x2 = self.frame_width, y2 = self.frame_height)
            
            # Giramos los videos 90 grados en sentido horario
            video_der_rotado = video_der.rotate(-90)
            
            # Guardamos los videos rotados
            video_der_rotado.write_videofile(video_der_path, fps = video.fps)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    splitter = Chopper()
    app.exec_()