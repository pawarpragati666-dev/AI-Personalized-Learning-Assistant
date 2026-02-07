def analyze_performance(python_marks, dbms_marks, ai_marks):

    results = {}

    subjects = {
        "Python": python_marks,
        "DBMS": dbms_marks,
        "AI": ai_marks
    }

    for subject, marks in subjects.items():

        if marks >= 75:
            level = "Strong"
            roadmap = "Learn advanced concepts and build projects"

        elif marks >= 50:
            level = "Average"
            roadmap = "Practice exercises and revise intermediate topics"

        else:
            level = "Weak"
            roadmap = "Revise basics, watch tutorials, and practice beginner problems"

        results[subject] = {
            "marks": marks,
            "level": level,
            "roadmap": roadmap
        }

    return results


def predict_performance(python_marks, dbms_marks, ai_marks):

    avg = (python_marks + dbms_marks + ai_marks) / 3

    if avg >= 75:
        prediction = "Excellent performance expected"
    elif avg >= 50:
        prediction = "Good performance expected"
    else:
        prediction = "Needs improvement"

    return prediction
