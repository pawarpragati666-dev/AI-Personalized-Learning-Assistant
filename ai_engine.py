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
            recommendation = "Advance to next level topics"

        elif marks >= 50:
            level = "Average"
            recommendation = "Practice more exercises"

        else:
            level = "Weak"
            recommendation = "Revise basics and watch tutorials"

        results[subject] = {
            "marks": marks,
            "level": level,
            "recommendation": recommendation
        }

    return results
