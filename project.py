import numpy as np
import joblib
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load the trained model
model = joblib.load("Placement Project.joblib")

# Create LabelEncoders for categorical variables
le_gender = LabelEncoder()
le_stream = LabelEncoder()

# Fit the encoders with the categories used in your notebook
le_gender.fit(['Male', 'Female'])
le_stream.fit(['Electronics And Communication', 'Computer Science', 'Information Technology', 'Civil'])

def predict():
    try:
        # Retrieve input data from the entry fields
        age = float(e1.get())
        gender = e2.get()
        stream = e3.get()
        internships_completed = int(e4.get())
        cgpa = float(e5.get())
        history_of_backlogs = int(e6.get())
        
        # Encode categorical variables
        if gender not in le_gender.classes_ or stream not in le_stream.classes_:
            result_label.config(text="Invalid category values. Please check your inputs.")
            return
        
        gender_encoded = le_gender.transform([gender])[0]
        stream_encoded = le_stream.transform([stream])[0]
        
        # Prepare the input data for prediction
        input_data = np.array([[age, gender_encoded, stream_encoded, internships_completed, cgpa, history_of_backlogs]])
        
        # Make the prediction
        prediction = model.predict(input_data)
        
        # Display the result
        result_label.config(text=f"Predicted Result: {'Placed' if prediction[0] == 1 else 'Not Placed'}")
    except ValueError as e:
        result_label.config(text=f"Error: {e}")

# Create the main window
win = tk.Tk()
win.geometry("800x500")
win.title("Placement Prediction")
win.config(bg="white")

# Create a title label
title_label = tk.Label(win, text="Placement Prediction", font=("Helvetica", 18, "bold"), bg="lightgreen", borderwidth=5)
title_label.pack(padx=10, pady=10, side="top")

# Create two frames
frame1 = tk.Frame(win, bg="white", relief="groove")
frame2 = tk.Frame(win, bg="lightgreen", relief="groove", borderwidth=5 , border= 10)

# Pack the frames
frame1.pack(side="left", fill="both", expand=True, padx=20, pady=20)
frame2.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Load and display image in frame2
image_path = r"C:\Users\Dell\Desktop\Placement Prediction\placement-prediction-using-machine-learning.jpg"
image = Image.open(image_path)
image = image.resize((210, 200))  # Resize the image if necessary
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(frame2, image=photo, border=5 , relief="raised")
image_label.pack(pady=20)

# Create input labels and entry fields in frame1
labels_text = ["Age", "Gender", "Stream", "Internships Completed", "CGPA", "History of Backlogs"]
entries = []

for text in labels_text:
    label = tk.Label(frame1, text=text, background="lightgreen")
    entry = tk.Entry(frame1)
    label.pack(pady=5)
    entry.pack(pady=5)
    entries.append(entry)

e1, e2, e3, e4, e5, e6 = entries

# Create a predict button and result label in frame2
predict_button = ttk.Button(frame2, text="Predict", command=predict, width=15)
predict_button.pack(pady=10)

result_label = tk.Label(frame2, text="", bg="lightgreen", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the Tkinter event loop
win.mainloop()
