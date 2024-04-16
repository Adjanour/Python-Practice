# import tkinter as tk

# def add_activity():
#     # Get input from entry fields and update schedule dictionary
#     pass 

# def generate_schedule():
#     # Write to schedule.txt file (similar to before)
#     pass

# # Build GUI 
# root = tk.Tk()
# root.title("Schedule Builder")

# day_label = tk.Label(root, text="Enter Day:")
# day_label.pack()
# day_entry = tk.Entry(root)
# day_entry.pack()

# # ... Similar elements for time slot and activity

# add_button = tk.Button(root, text="Add Activity", command=add_activity)
# add_button.pack()

# generate_button = tk.Button(root, text="Generate Schedule", command=generate_schedule) 
# generate_button.pack()

# root.mainloop() 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

class ScheduleBuilder(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Schedule Builder")

        # Create widgets
        self.day_label = QLabel("Enter Day:")
        self.day_entry = QLineEdit()
        # ... (Similar widgets for time slot and activity)
        self.add_button = QPushButton("Add Activity")
        self.generate_button = QPushButton("Generate Schedule") 

        # Layout
        layout = QGridLayout()
        layout.addWidget(self.day_label, 0, 0)
        layout.addWidget(self.day_entry, 0, 1)
        # ... (Add other widgets to layout)
        layout.addWidget(self.add_button, 2, 0)  # Example row/column placement
        layout.addWidget(self.generate_button, 2, 1) 
        self.setLayout(layout)

        # Connect button actions
        self.add_button.clicked.connect(self.add_activity)
        self.generate_button.clicked.connect(self.generate_schedule)

    def add_activity(self):
        # ... Logic to get data and update schedule dictionary
        pass

    def generate_schedule(self):
        # ... Logic to generate the schedule.txt file
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScheduleBuilder()
    window.show()
    sys.exit(app.exec_()) 
