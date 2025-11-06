import os
from app.gui import App
from app.data_manager import DataManager

DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

CRED_PATH = os.path.join(DATA_DIR, 'credentials.json')
STUDENT_DATA_PATH = os.path.join(DATA_DIR, 'student_data.json')
COURSE_PATH = os.path.join(DATA_DIR, 'courses.json')

if __name__ == "__main__":
    data_manager = DataManager(CRED_PATH, STUDENT_DATA_PATH, COURSE_PATH)
    app = App(data_manager)
    app.mainloop() 