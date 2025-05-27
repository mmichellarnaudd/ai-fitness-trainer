import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title="AI Personal Trainer", layout="centered")

# --- Header Section ---
st.markdown("""
    <style>
        .main-title {
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            margin-bottom: 10px;
        }
        .description {
            text-align: center;
            font-size: 1.1em;
            margin-bottom: 30px;
            color: #555;
        }
        .input-section {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        .result-box {
            background-color: #e6f7ff;
            padding: 20px;
            border-left: 6px solid #1890ff;
            border-radius: 8px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🏋️ AI Personal Trainer</div>", unsafe_allow_html=True)
st.markdown("<div class='description'>Get your personalized weekly workout plan based on your fitness goal, level, and available equipment.</div>", unsafe_allow_html=True)

# --- Input Section ---
st.markdown("<div class='input-section'>", unsafe_allow_html=True)
name = st.text_input("What's your name?")
goal = st.selectbox("What's your fitness goal?", ["Fat Loss", "Muscle Gain", "Endurance", "General Fitness"])
level = st.selectbox("What's your fitness level?", ["Beginner", "Intermediate", "Advanced"])
equipment = st.text_input("What equipment do you have? (e.g., dumbbells, bands, none)")
st.markdown("</div>", unsafe_allow_html=True)

add_vertical_space(1)

# --- Plan Generation ---
if st.button("🎯 Generate My Plan"):
    plan = {}

    if goal == "Fat Loss":
        plan["workout_type"] = "HIIT + Cardio"
        plan["frequency"] = "5 days/week"
        plan["nutrition"] = "High protein, low carb. Focus on lean meats, veggies, and water."
    elif goal == "Muscle Gain":
        plan["workout_type"] = "Strength Training"
        plan["frequency"] = "4 days/week"
        plan["nutrition"] = "Caloric surplus with high protein. Add rice, pasta, healthy fats."
    elif goal == "Endurance":
        plan["workout_type"] = "Circuit + Cardio"
        plan["frequency"] = "5 days/week"
        plan["nutrition"] = "Balanced diet with slow carbs (e.g., oats, whole grains), protein, hydration."
    else:
        plan["workout_type"] = "General Fitness"
        plan["frequency"] = "3 days/week"
        plan["nutrition"] = "Moderate carbs, high protein. Prioritize variety and hydration."

    if "dumbbell" in equipment.lower():
        plan["equipment_plan"] = "Use dumbbells for squats, rows, and overhead presses."
    elif "band" in equipment.lower():
        plan["equipment_plan"] = "Incorporate resistance band exercises like rows, presses, and squats."
    else:
        plan["equipment_plan"] = "Focus on bodyweight exercises: push-ups, squats, lunges, and planks."

    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.subheader(f"Here's your personalized plan, {name}!")
    st.markdown(f"**🏆 Goal-based focus:** {plan['workout_type']}")
    st.markdown(f"**📅 Training frequency:** {plan['frequency']}")
    st.markdown(f"**⚙️ Fitness level:** {level}")
    st.markdown(f"**🧰 Equipment strategy:** {plan['equipment_plan']}")
    st.markdown(f"**🥗 Nutrition tip:** {plan['nutrition']}")
    st.success("Stay consistent and let's hit those goals! 💪")
    st.markdown("</div>", unsafe_allow_html=True)
