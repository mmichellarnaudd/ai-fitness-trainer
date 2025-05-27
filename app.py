import streamlit as st

st.set_page_config(page_title="AI Personal Trainer", layout="centered")

st.title("🏋️ AI Personal Trainer")
st.write("Get your personalized weekly workout plan based on your fitness goal, level, and available equipment.")

name = st.text_input("What's your name?")
goal = st.selectbox("What's your fitness goal?", ["Fat Loss", "Muscle Gain", "Endurance", "General Fitness"])
level = st.selectbox("What's your fitness level?", ["Beginner", "Intermediate", "Advanced"])
equipment = st.text_input("What equipment do you have? (e.g., dumbbells, bands, none)")

if st.button("Generate My Plan"):
    plan = {}

    if goal == "Fat Loss":
        plan["workout_type"] = "HIIT + Cardio"
        plan["frequency"] = "5 days/week"
    elif goal == "Muscle Gain":
        plan["workout_type"] = "Strength Training"
        plan["frequency"] = "4 days/week"
    elif goal == "Endurance":
        plan["workout_type"] = "Circuit + Cardio"
        plan["frequency"] = "5 days/week"
    else:
        plan["workout_type"] = "General Fitness"
        plan["frequency"] = "3 days/week"

    if "dumbbell" in equipment.lower():
        plan["equipment_plan"] = "Use dumbbells for squats, rows, and overhead presses."
    elif "band" in equipment.lower():
        plan["equipment_plan"] = "Incorporate resistance band exercises like rows, presses, and squats."
    else:
        plan["equipment_plan"] = "Focus on bodyweight exercises: push-ups, squats, lunges, and planks."

    st.subheader(f"Here's your personalized plan, {name}!")
    st.markdown(f"**Goal-based focus:** {plan['workout_type']}")
    st.markdown(f"**Training frequency:** {plan['frequency']}")
    st.markdown(f"**Fitness level:** {level}")
    st.markdown(f"**Equipment strategy:** {plan['equipment_plan']}")
    st.success("Stay consistent and let's hit those goals! 💪")
