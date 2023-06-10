import pandas as pd
import cv2
import keyboard
import csv
from moviepy.editor import VideoFileClip
from tkinter import Tk, filedialog
from tkinter import messagebox


def draw_text(img, text,
          font = cv2.FONT_HERSHEY_PLAIN,
          pos = (0, 0),
          font_scale = 2,
          font_thickness = 1,
          text_color = (0, 0, 255),
          text_color_bg = (0, 0, 0)
          ):

    x, y = pos
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size
    cv2.rectangle(img, pos, (x + text_w, y + text_h), text_color_bg, -1)
    cv2.putText(img, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)

    return text_size

def process_frame(frame, frame_number, left, right):
        
    left = left
    right = right
    back = False

    # Add frame number to the frame
    draw_text(frame, f"Frame: {frame_number}", pos = (int(frame.shape[0]*0.40), int(frame.shape[1]*0.01)), text_color = (0, 255, 0))
    
    # Add left value to the frame
    draw_text(frame, f"Left: {left}", pos = (int(frame.shape[0]*0.01), int(frame.shape[1]*0.01)))

    # Add right value to the frame
    draw_text(frame, f"Right: {right}", pos = (int(frame.shape[0]*0.90), int(frame.shape[1]*0.01)))

    # Display the frame with the frame number
    cv2.imshow("Frame", frame)
    # Wait for a keystroke
    key = cv2.waitKey(0)
    if key == ord('1'):
        left = 1
        right = 0
    if key == ord('3'):
        left = 0
        right = 1
    if key == ord('0'):
        left = 0
        right = 0
    if key == ord('2'):
        pass
    if key == ord('5'):
        back = True
    return left, right, back

def main():
    # Create a Tkinter window
    root = Tk()
    root.withdraw()

    # Open a file dialog to select the video file
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])

    if not video_path:
        print("No video file selected.")
        return

    # Open the video file
    video = VideoFileClip(video_path)
    
    # Create another Tkinter window
    root = Tk()
    root.withdraw()

    # Open a file dialog to select the video file
    csv_path = filedialog.askopenfilename(filetypes=[("text files", "*.csv")])

    if csv_path:
        # Load the CSV file
        labels = pd.read_csv(csv_path)
    else:
        print("No label file selected")
            
    
    frame_generator = video.iter_frames()
    frame_list = list(frame_generator) # This takes a while
    frame_labels_left = ["-"]*len(frame_list)
    frame_labels_right = ["-"]*len(frame_list)
    current_frame = 0
    
    while current_frame < len(frame_list):
              
        frame = frame_list[current_frame]
        
        if csv_path:
            if frame_labels_left[current_frame] != "-" and frame_labels_right[current_frame] != "-":
                left = frame_labels_left[current_frame]
                right = frame_labels_right[current_frame]
            else:
                left = labels.iloc[current_frame]['Left']  # 'Left' is the column name in the CSV
                right = labels.iloc[current_frame]['Right']  # 'Left' is the column name in the CSV
        
        if not csv_path:
            if frame_labels_left[current_frame] != "-" and frame_labels_right[current_frame] != "-":
                left = frame_labels_left[current_frame]
                right = frame_labels_right[current_frame]
            else:
                left = 0
                right = 0

        # Process the current frames
        left, right, back = process_frame(frame, current_frame, left, right)
        
        if back:
            # Go back one frame
            current_frame = max(0, current_frame - 1)
            continue
        
        # Break the loop if the user presses 'q'
        if keyboard.is_pressed('q'):
            break
        
        frame_labels_left[current_frame] = left
        frame_labels_right[current_frame] = right
        
        current_frame += 1
        
        if current_frame == len(frame_list):
            # Ask the user if they want to exit
            response = messagebox.askquestion("Exit", "Do you want to exit the program?")
            if response == 'yes':
                continue
            else:
                current_frame = len(frame_list) - 1

    # Write the frame labels to a CSV file
    output_csv = video_path.rsplit('.', 1)[0] + '_labels.csv'
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Frame', 'Left', 'Right'])
        for i, (left, right) in enumerate(zip(frame_labels_left, frame_labels_right)):
            writer.writerow([i+1, left, right])

    # Close the OpenCV windows
    cv2.destroyAllWindows()


# Call the main function
main()
