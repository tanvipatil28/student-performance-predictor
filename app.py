```python
import streamlit as st

# -----------------------------
# Knowledge Base
# -----------------------------

rules = [
    ({"att": "High", "study": "High"},
     {"engagement": "High"},
     "R1: High Attendance + High Study -> High Engagement"),

    ({"att": "Low", "study": "Low"},
     {"engagement": "Low"},
     "R2: Low Attendance + Low Study -> Low Engagement"),

    ({"att": "Low", "study": "High"},
     {"engagement": "Self_Studier"},
     "R3: Low Attendance + High Study -> Self Studier"),

    ({"att": "Moderate", "study": "Moderate"},
     {"engagement": "Moderate"},
     "R4: Moderate Attendance + Study -> Moderate Engagement"),

    ({"marks": "Poor", "study": "High"},
     {"diagnosis": "Struggling"},
     "R5: Poor Marks + High Study -> Needs Help"),

    ({"marks": "Excellent", "engagement": "High"},
     {"diagnosis": "Mastery"},
     "R6: Top Marks + High Engagement -> Subject Mastery"),

    ({"marks": "Good", "engagement": "High"},
     {"diagnosis": "Strong"},
     "R7: Good Marks + High Engagement -> Strong Performer"),

    ({"marks": "Average", "engagement": "Moderate"},
     {"diagnosis": "Steady"},
     "R8: Average Marks + Moderate Engagement -> Steady Progress"),

    ({"marks": "Poor", "engagement": "Low"},
     {"diagnosis": "Deficit"},
     "R9: Poor Marks + Low Engagement -> Critical Deficit"),

    ({"diagnosis": "Mastery"},
     {"pred": "Distinction (Grade A+)",
      "advice": "Nominate for honors and peer mentoring."},
     "R10: Mastery -> Distinction"),

    ({"diagnosis": "Strong"},
     {"pred": "First Class (Grade A)",
      "advice": "Great performance! Practice past papers for A+."},
     "R11: Strong -> First Class"),

    ({"diagnosis": "Steady"},
     {"pred": "Second Class (Grade B)",
      "advice": "Increase study by 3 hrs/week to achieve Grade A."},
     "R12: Steady -> Second Class"),

    ({"diagnosis": "Struggling"},
     {"pred": "Borderline (Grade C)",
      "advice": "Attend faculty doubt sessions and focus on basics."},
     "R13: Struggling -> Borderline"),

    ({"diagnosis": "Deficit"},
     {"pred": "Critical Failure (Grade F)",
      "advice": "Parent meeting needed and remedial classes."},
     "R14: Deficit -> Critical Failure"),

    ({"engagement": "Self_Studier"},
     {"pred": "Pass (Attendance Warning)",
      "advice": "Must attend classes to meet 75% criteria."},
     "R15: Self Studier -> Warning"),
]


# -----------------------------
# Forward Chaining
# -----------------------------

def forward_chain(att_val, marks_val, study_val):

    att = "High" if att_val >= 85 else (
        "Moderate" if att_val >= 75 else "Low"
    )

    mrk = "Excellent" if marks_val >= 80 else (
        "Good" if marks_val >= 60 else (
            "Average" if marks_val >= 40 else "Poor"
        )
    )

    std = "High" if study_val >= 15 else (
        "Moderate" if study_val >= 7 else "Low"
    )

    memory = {
        "att": att,
        "marks": mrk,
        "study": std
    }

    initial_facts = dict(memory)

    fired_rules = []
    new_facts = []

    while True:

        rule_fired = False

        for conditions, consequences, desc in rules:

            if (
                desc not in fired_rules
                and all(
                    memory.get(k) == v
                    for k, v in conditions.items()
                )
            ):

                fired_rules.append(desc)

                for k, v in consequences.items():

                    if k not in memory:
                        new_facts.append(f"{k} = {v}")

                    memory[k] = v

                rule_fired = True
                break

        if not rule_fired:
            break

    pred = memory.get(
        "pred",
        "Second Class (Grade B)"
    )

    advice = memory.get(
        "advice",
        "Maintain regular study hours."
    )

    return (
        initial_facts,
        fired_rules,
        new_facts,
        pred,
        advice
    )


# -----------------------------
# Preset Functions
# -----------------------------

def set_topper():
    st.session_state.attendance = 92.0
    st.session_state.marks = 88.0
    st.session_state.study = 18.0


def set_hard_worker():
    st.session_state.attendance = 88.0
    st.session_state.marks = 35.0
    st.session_state.study = 20.0


def set_at_risk():
    st.session_state.attendance = 45.0
    st.session_state.marks = 28.0
    st.session_state.study = 3.0


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Student Performance Predictor",
    layout="wide"
)

st.title("🎓 Student Performance Prediction System")

st.subheader("AI-Based Forward Chaining System")

st.write(
    "Enter student information to predict performance "
    "using rule-based forward chaining."
)


# -----------------------------
# Initialize Session State
# -----------------------------

if "attendance" not in st.session_state:
    st.session_state.attendance = 88.0

if "marks" not in st.session_state:
    st.session_state.marks = 35.0
    

if "study" not in st
