import pandas as pd

FILE_PATH = "data/students.csv"

def load_data():
    return pd.read_csv(FILE_PATH)

def save_data(name, python_marks, dbms_marks, ai_marks):

    df = load_data()

    new_data = {
        "name": name,
        "python_marks": python_marks,
        "dbms_marks": dbms_marks,
        "ai_marks": ai_marks
    }

    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    df.to_csv(FILE_PATH, index=False)
