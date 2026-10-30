import streamlit as st

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# FORWARD CHAINING ENGINE
# ============================================================

def forward_chain(attendance, marks, study):

    # --------------------------------------------------------
    # Convert input values into categories
    # --------------------------------------------------------

    if attendance >= 85:
        att = "High"
    elif attendance >= 75:
        att = "Moderate"
    else:
        att = "Low"

    if marks >= 80:
        mark_level = "Excellent"
    elif marks >= 60:
        mark_level = "Good"
    elif marks >= 40:
        mark_level = "Average"
    else:
        mark_level = "Poor"

    if study >= 15:
        study_level = "High"
    elif study >= 7:
        study_level = "Moderate"
    else:
        study_level = "Low"

    # --------------------------------------------------------
    # Initial Working Memory
    # --------------------------------------------------------

    facts = {
        "att": att,
        "marks": mark_level,
        "study": study_level
    }

    fired_rules = []
    new_facts = []

    changed = True

    # ========================================================
    # FORWARD CHAINING
    # ========================================================

    while changed:

        changed = False

        # ----------------------------------------------------
        # R1: High Attendance + High Study
        # ----------------------------------------------------

        if (
            facts.get("att") == "High"
            and facts.get("study") == "High"
            and "engagement" not in facts
        ):
            facts["engagement"] = "High"

            fired_rules.append(
                "R1: High Attendance + High Study → High Engagement"
            )

            new_facts.append(
                "Engagement = High"
            )

            changed = True

        # ----------------------------------------------------
        # R2: Low Attendance + Low Study
        # ----------------------------------------------------

        if (
            facts.get("att") == "Low"
            and facts.get("study") == "Low"
            and "engagement" not in facts
        ):
            facts["engagement"] = "Low"

            fired_rules.append(
                "R2: Low Attendance + Low Study → Low Engagement"
            )

            new_facts.append(
                "Engagement = Low"
            )

            changed = True

        # ----------------------------------------------------
        # R3: Low Attendance + High Study
        # ----------------------------------------------------

        if (
            facts.get("att") == "Low"
            and facts.get("study") == "High"
            and "diagnosis" not in facts
        ):
            facts["diagnosis"] = "Self Studier"

            fired_rules.append(
                "R3: Low Attendance + High Study → Self Studier"
            )

            new_facts.append(
                "Diagnosis = Self Studier"
            )

            changed = True

        # ----------------------------------------------------
        # R4: Moderate Attendance + Moderate Study
        # ----------------------------------------------------

        if (
            facts.get("att") == "Moderate"
            and facts.get("study") == "Moderate"
            and "engagement" not in facts
        ):
            facts["engagement"] = "Moderate"

            fired_rules.append(
                "R4: Moderate Attendance + Moderate Study → Moderate Engagement"
            )

            new_facts.append(
                "Engagement = Moderate"
            )

            changed = True

        # ----------------------------------------------------
        # R5: Poor Marks + High Study
        # ----------------------------------------------------

        if (
            facts.get("marks") == "Poor"
            and facts.get("study") == "High"
            and "diagnosis" not in facts
        ):
            facts["diagnosis"] = "Struggling"

            fired_rules.append(
                "R5: Poor Marks + High Study → Struggling"
            )

            new_facts.append(
                "Diagnosis = Struggling"
            )

            changed = True

        # ----------------------------------------------------
        # R6: Excellent Marks + High Engagement
        # ----------------------------------------------------

        if (
            facts.get("marks") == "Excellent"
            and facts.get("engagement") == "High"
            and "diagnosis" not in facts
        ):
            facts["diagnosis"] = "Mastery"

            fired_rules.append(
                "R6: Excellent Marks + High Engagement → Mastery"
            )

            new_facts.append(
                "Diagnosis = Mastery"
            )

            changed = True

        # ----------------------------------------------------
        # R7: Good Marks + High Engagement
        # ----------------------------------------------------

        if (
            facts.get("marks") == "Good"
            and facts.get("engagement") == "High"
            and "diagnosis" not in facts
        ):
            facts["diagnosis"] = "Strong"

            fired_rules.append(
                "R7: Good Marks + High Engagement → Strong"
            )

            new_facts.append(
                "Diagnosis = Strong"
            )

            changed = True

        # ----------------------------------------------------
        # R8: Average Marks + Moderate Engagement
        # ----------------------------------------------------

        if (
            facts.get("marks") == "Average"
            and facts.get("engagement") == "Moderate"
            and "diagnosis" not in facts
        ):
            facts["diagnosis"] = "Steady"

            fired_rules.append(
                "R8: Average Marks + Moderate Engagement → Steady"
            )

            new_facts.append(
                "Diagnosis = Steady"
            )

            changed = True

        # ----------------------------------------------------
        # R9: Poor Marks + Low Engagement
        # ----------------------------------------------------

        if (
            facts.get("marks") == "Poor"
            and facts.get("engagement") == "Low"
            and "diagnosis" not in facts
        ):
            facts["diagnosis"] = "Deficit"

            fired_rules.append(
                "R9: Poor Marks + Low Engagement → Deficit"
            )

            new_facts.append(
                "Diagnosis = Deficit"
            )

            changed = True

        # ----------------------------------------------------
        # R10: Mastery → Distinction
        # ----------------------------------------------------

        if (
            facts.get("diagnosis") == "Mastery"
            and "prediction" not in facts
        ):
            facts["prediction"] = "Distinction (Grade A+)"
            facts["advice"] = "Nominate for honors and peer mentoring"

            fired_rules.append(
                "R10: Mastery → Distinction (Grade A+)"
            )

            new_facts.append(
                "Prediction = Distinction (Grade A+)"
            )

            new_facts.append(
                "Advice = Nominate for honors and peer mentoring"
            )

            changed = True

        # ----------------------------------------------------
        # R11: Strong → First Class
        # ----------------------------------------------------

        if (
            facts.get("diagnosis") == "Strong"
            and "prediction" not in facts
        ):
            facts["prediction"] = "First Class (Grade A)"
            facts["advice"] = "Practice past papers to improve towards A+"

            fired_rules.append(
                "R11: Strong → First Class (Grade A)"
            )

            new_facts.append(
                "Prediction = First Class (Grade A)"
            )

            new_facts.append(
                "Advice = Practice past papers to improve towards A+"
            )

            changed = True

        # ----------------------------------------------------
        # R12: Steady → Second Class
        # ----------------------------------------------------

        if (
            facts.get("diagnosis") == "Steady"
            and "prediction" not in facts
        ):
            facts["prediction"] = "Second Class (Grade B)"
            facts["advice"] = "Increase study time by about 3 hours per week"

            fired_rules.append(
                "R12: Steady → Second Class (Grade B)"
            )

            new_facts.append(
                "Prediction = Second Class (Grade B)"
            )

            new_facts.append(
                "Advice = Increase study time by about 3 hours per week"
            )

            changed = True

        # ----------------------------------------------------
        # R13: Struggling → Borderline
        # ----------------------------------------------------

        if (
            facts.get("diagnosis") == "Struggling"
            and "prediction" not in facts
        ):
            facts["prediction"] = "Borderline (Grade C)"
            facts["advice"] = "Attend faculty doubt sessions and strengthen basics"

            fired_rules.append(
                "R13: Struggling → Borderline (Grade C)"
            )

            new_facts.append(
                "Prediction = Borderline (Grade C)"
            )

            new_facts.append(
                "Advice = Attend faculty doubt sessions and strengthen basics"
            )

            changed = True

        # ----------------------------------------------------
        # R14: Deficit → Critical Failure
        # ----------------------------------------------------

        if (
            facts.get("diagnosis") == "Deficit"
            and "prediction" not in facts
        ):
            facts["prediction"] = "Critical Failure (Grade F)"
            facts["advice"] = "Remedial classes and parent/mentor guidance required"

            fired_rules.append(
                "R14: Deficit → Critical Failure (Grade F)"
            )

            new_facts.append(
                "Prediction = Critical Failure (Grade F)"
            )

            new_facts.append(
                "Advice = Remedial classes and parent/mentor guidance required"
            )

            changed = True

        # ----------------------------------------------------
        # R15: Self Studier → Pass
        # ----------------------------------------------------

        if (
            facts.get("diagnosis") == "Self Studier"
            and "prediction" not in facts
        ):
            facts["prediction"] = "Pass (Attendance Warning)"
            facts["advice"] = "Continue self-study but improve attendance to at least 75%"

            fired_rules.append(
                "R15: Self Studier → Pass (Attendance Warning)"
            )

            new_facts.append(
                "Prediction = Pass (Attendance Warning)"
            )

            new_facts.append(
                "Advice = Continue self-study but improve attendance to at least 75%"
            )

            changed = True

        # ----------------------------------------------------
        # R16: Low Attendance + Moderate Study +
        #      Average/Poor Marks → At Risk
        # ----------------------------------------------------

        if (
            facts.get("att") == "Low"
            and facts.get("study") == "Moderate"
            and facts.get("marks") in ["Average", "Poor"]
            and "diagnosis" not in facts
        ):
            facts["diagnosis"] = "At Risk"

            fired_rules.append(
                "R16: Low Attendance + Moderate Study + Average/Poor Marks → At Risk"
            )

            new_facts.append(
                "Diagnosis = At Risk"
            )

            changed = True

        # ----------------------------------------------------
        # R17: At Risk → Borderline
        # ----------------------------------------------------

        if (
            facts.get("diagnosis") == "At Risk"
            and "prediction" not in facts
        ):
            facts["prediction"] = "Borderline (Grade C)"
            facts["advice"] = "Improve attendance and maintain regular study"

            fired_rules.append(
                "R17: At Risk → Borderline (Grade C)"
            )

            new_facts.append(
                "Prediction = Borderline (Grade C)"
            )

            new_facts.append(
                "Advice = Improve attendance and maintain regular study"
            )

            changed = True

        # ----------------------------------------------------
        # R18: Low Attendance + Good Marks +
        #      Moderate Study → Attendance Warning
        # ----------------------------------------------------

        if (
            facts.get("att") == "Low"
            and facts.get("marks") == "Good"
            and facts.get("study") == "Moderate"
            and "diagnosis" not in facts
        ):
            facts["diagnosis"] = "Attendance Warning"

            fired_rules.append(
                "R18: Low Attendance + Good Marks + Moderate Study → Attendance Warning"
            )

            new_facts.append(
                "Diagnosis = Attendance Warning"
            )

            changed = True

        # ----------------------------------------------------
        # R19: Attendance Warning → Good Standing
        # ----------------------------------------------------

        if (
            facts.get("diagnosis") == "Attendance Warning"
            and "prediction" not in facts
        ):
            facts["prediction"] = "Good Standing (Grade B)"
            facts["advice"] = "Maintain good marks and improve attendance to at least 75%"

            fired_rules.append(
                "R19: Attendance Warning → Good Standing (Grade B)"
            )

            new_facts.append(
                "Prediction = Good Standing (Grade B)"
            )

            new_facts.append(
                "Advice = Maintain good marks and improve attendance to at least 75%"
            )

            changed = True

    # --------------------------------------------------------
    # Default Prediction
    # --------------------------------------------------------

    if "prediction" not in facts:

        facts["prediction"] = "Second Class (Grade B)"
        facts["advice"] = "Maintain regular study hours"

    return facts, fired_rules, new_facts


# ============================================================
# RISK LEVEL
# ============================================================

def get_risk_level(diagnosis):

    if diagnosis == "Mastery":
        return "🟢 Low Risk"

    elif diagnosis == "Strong":
        return "🟢 Low Risk"

    elif diagnosis == "Steady":
        return "🟡 Moderate Risk"

    elif diagnosis == "Attendance Warning":
        return "🟠 High Risk"

    elif diagnosis == "Self Studier":
        return "🟠 High Risk"

    elif diagnosis == "At Risk":
        return "🟠 High Risk"

    elif diagnosis == "Struggling":
        return "🟠 High Risk"

    elif diagnosis == "Deficit":
        return "🔴 Very High Risk"

    else:
        return "🟡 Moderate Risk"


# ============================================================
# PERSONALIZED RECOMMENDATIONS
# ============================================================

def get_recommendations(attendance, marks, study, diagnosis):

    recommendations = []

    # Attendance
    if attendance < 75:

        recommendations.append(
            "Increase attendance to at least 75% to avoid attendance-related academic problems."
        )

    elif attendance < 85:

        recommendations.append(
            "Try to improve attendance above 85% for more consistent academic engagement."
        )

    else:

        recommendations.append(
            "Maintain your good attendance and continue attending classes regularly."
        )

    # Marks
    if marks < 40:

        recommendations.append(
            "Focus on basic concepts, revision, and solving practice questions."
        )

    elif marks < 60:

        recommendations.append(
            "Improve internal marks through regular revision and more practice."
        )

    elif marks < 80:

        recommendations.append(
            "Continue practicing and revise regularly to move towards excellent marks."
        )

    else:

        recommendations.append(
            "Maintain your strong academic performance with regular revision."
        )

    # Study
    if study < 7:

        recommendations.append(
            "Gradually increase weekly study time and follow a regular study schedule."
        )

    elif study < 15:

        recommendations.append(
            "Try to increase focused study time to 15 hours per week."
        )

    else:

        recommendations.append(
            "Your study time is strong; focus on study quality and effective revision."
        )

    # Diagnosis-specific advice
    if diagnosis == "Struggling":

        recommendations.append(
            "Since study time is high but marks are low, focus on study methods, concepts, and doubt clearing."
        )

    elif diagnosis == "Self Studier":

        recommendations.append(
            "You study well independently, but improving classroom attendance is important."
        )

    elif diagnosis == "At Risk":

        recommendations.append(
            "Your attendance and academic performance need attention. Prioritize classes and regular revision."
        )

    elif diagnosis == "Attendance Warning":

        recommendations.append(
            "Your marks are good, but attendance is low. Focus mainly on improving attendance."
        )

    elif diagnosis == "Mastery":

        recommendations.append(
            "You are performing at a mastery level. Continue consistently and consider peer mentoring."
        )

    elif diagnosis == "Strong":

        recommendations.append(
            "You are performing strongly. Practice previous question papers to move towards A+."
        )

    elif diagnosis == "Deficit":

        recommendations.append(
            "Seek faculty support, remedial classes, and regular academic guidance."
        )

    return recommendations


# ============================================================
# STREAMLIT UI
# ============================================================

st.title("🎓 Student Performance Prediction System")

st.subheader("AI-Based Forward Chaining System")

st.write(
    "This system predicts student performance using attendance, "
    "internal marks, and weekly study hours."
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("📋 Student Information")

attendance = st.sidebar.number_input(
    "Attendance Percentage (%)",
    min_value=0.0,
    max_value=100.0,
    value=85.0,
    step=1.0
)

marks = st.sidebar.number_input(
    "Internal Assessment Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=1.0
)

study = st.sidebar.number_input(
    "Weekly Study Hours",
    min_value=0.0,
    max_value=100.0,
    value=10.0,
    step=1.0
)

run_prediction = st.sidebar.button(
    "🔍 Run Prediction",
    use_container_width=True
)


# ============================================================
# RUN PREDICTION
# ============================================================

if run_prediction:

    facts, fired_rules, new_facts = forward_chain(
        attendance,
        marks,
        study
    )

    diagnosis = facts.get(
        "diagnosis",
        "No specific diagnosis"
    )

    prediction = facts.get(
        "prediction",
        "Second Class (Grade B)"
    )

    advice = facts.get(
        "advice",
        "Maintain regular study hours"
    )

    risk = get_risk_level(diagnosis)

    recommendations = get_recommendations(
        attendance,
        marks,
        study,
        diagnosis
    )

    # ========================================================
    # PERFORMANCE DASHBOARD
    # ========================================================

    st.header("📊 Performance Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Attendance",
            f"{attendance:.0f}%"
        )

        if attendance >= 85:

            st.success("High Attendance")

        elif attendance >= 75:

            st.warning("Moderate Attendance")

        else:

            st.error("Low Attendance")

    with col2:

        st.metric(
            "Internal Marks",
            f"{marks:.0f}/100"
        )

        if marks >= 80:

            st.success("Excellent")

        elif marks >= 60:

            st.success("Good")

        elif marks >= 40:

            st.warning("Average")

        else:

            st.error("Poor")

    with col3:

        st.metric(
            "Weekly Study",
            f"{study:.0f} hrs"
        )

        if study >= 15:

            st.success("High Study")

        elif study >= 7:

            st.warning("Moderate Study")

        else:

            st.error("Low Study")

    st.divider()

    # ========================================================
    # INITIAL FACTS
    # ========================================================

    st.header("1️⃣ Initial Facts - Working Memory")

    fact_col1, fact_col2, fact_col3 = st.columns(3)

    with fact_col1:

        st.info(
            f"Attendance = {facts['att']}\n\n"
            f"Actual Value = {attendance:.0f}%"
        )

    with fact_col2:

        st.info(
            f"Marks = {facts['marks']}\n\n"
            f"Actual Value = {marks:.0f}/100"
        )

    with fact_col3:

        st.info(
            f"Study = {facts['study']}\n\n"
            f"Actual Value = {study:.0f} hrs/week"
        )

    # ========================================================
    # RULES FIRED
    # ========================================================

    st.header("2️⃣ Rules Fired")

    if fired_rules:

        for rule in fired_rules:

            st.write(
                "✅",
                rule
            )

    else:

        st.write(
            "No rules were fired."
        )

    # ========================================================
    # NEW FACTS
    # ========================================================

    st.header("3️⃣ New Facts Deduced")

    if new_facts:

        for fact in new_facts:

            st.success(
                fact
            )

    else:

        st.write(
            "No new facts were deduced."
        )

    # ========================================================
    # FINAL PREDICTION
    # ========================================================

    st.header("4️⃣ Final Prediction & Recommendation")

    result_col1, result_col2 = st.columns(2)

    with result_col1:

        st.subheader("🎯 Final Prediction")

        st.success(
            prediction
        )

        st.write(
            f"**Diagnosis:** {diagnosis}"
        )

    with result_col2:

        st.subheader("🚦 Risk Level")

        if "Low Risk" in risk:

            st.success(risk)

        elif "Very High Risk" in risk:

            st.error(risk)

        else:

            st.warning(risk)

        st.write(
            f"**System Advice:** {advice}"
        )

    st.divider()

    # ========================================================
    # PERSONALIZED RECOMMENDATIONS
    # ========================================================

    st.header("💡 Personalized Recommendations")

    for recommendation in recommendations:

        st.write(
            "•",
            recommendation
        )

    st.divider()

    # ========================================================
    # OVERALL SUMMARY
    # ========================================================

    st.header("📌 Overall Performance Summary")

    st.write(
        f"The system analyzed the student's attendance of "
        f"**{attendance:.0f}%**, internal marks of "
        f"**{marks:.0f}/100**, and weekly study time of "
        f"**{study:.0f} hours**."
    )

    st.write(
        f"Using forward chaining, the system identified the student "
        f"as **{diagnosis}** and predicted **{prediction}**."
    )

else:

    st.info(
        "👈 Enter the student's details in the sidebar and click "
        "**Run Prediction** to analyze performance."
    )
