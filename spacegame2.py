# # import streamlit as st
# # import random
# # import base64
# # import os
# # import time

# # # ------------------ Dummy User Database ------------------
# # if "users" not in st.session_state:
# #     st.session_state.users = {"Greatness": "1234"}  # default user

# # if "logged_in" not in st.session_state:
# #     st.session_state.logged_in = False
# #     st.session_state.current_user = None


# # # ------------------ Sign Up & Login ------------------
# # st.sidebar.title("🔑 Sign In / Sign Up")

# # if not st.session_state.logged_in:
# #     auth_choice = st.sidebar.radio("Choose an option:", ["Login", "Sign Up"])

# #     if auth_choice == "Login":
# #         username = st.sidebar.text_input("👤 Username")
# #         password = st.sidebar.text_input("🔒 Password", type="password")
# #         if st.sidebar.button("Login"):
# #             if username in st.session_state.users and st.session_state.users[username] == password:
# #                 st.session_state.logged_in = True
# #                 st.session_state.current_user = username
# #                 st.sidebar.success(f"✅ Welcome back, {username}!")
# #                 st.rerun()
# #             else:
# #                 st.sidebar.error("❌ Invalid username or password")

# #     elif auth_choice == "Sign Up":
# #         new_user = st.sidebar.text_input("👤 Choose a username")
# #         new_pass = st.sidebar.text_input("🔒 Choose a password", type="password")
# #         if st.sidebar.button("Sign Up"):
# #             if new_user in st.session_state.users:
# #                 st.sidebar.warning("⚠️ Username already exists")
# #             elif not new_user.strip() or not new_pass.strip():
# #                 st.sidebar.warning("⚠️ Please enter valid credentials")
# #             else:
# #                 st.session_state.users[new_user] = new_pass
# #                 st.sidebar.success("✅ Account created! Please log in.")

# # else:
# #     # ------------------ Main App (only after login) ------------------
# #     st.sidebar.success(f"👋 Hello, {st.session_state.current_user}")
# #     if st.sidebar.button("🚪 Logout"):
# #         st.session_state.logged_in = False
# #         st.session_state.current_user = None
# #         st.rerun()

# #     # 🏷️ Title
# #     st.title("🎯 Subject Quiz & 🧮 Calculator")

# #     # ------------------ Background Settings ------------------
# #     bg_choice = st.radio("Choose background type:", ["Color", "Image"])

# #     if bg_choice == "Color":
# #         bg_color = st.color_picker("Pick a background color:", "#12B0F4")
# #         page_bg = f"""
# #         <style>
# #         [data-testid="stAppViewContainer"] {{
# #             background-color: {bg_color};
# #             background-size: cover;
# #         }}
# #         [data-testid="stHeader"] {{
# #             background-color: rgba(0,0,0,0);
# #         }}
# #         </style>
# #         """
# #     else:
# #         bg_image = st.file_uploader("Upload a background image", type=["png", "jpg", "jpeg"])
# #         if bg_image:
# #             encoded_image = base64.b64encode(bg_image.read()).decode()
# #             page_bg = f"""
# #             <style>
# #             [data-testid="stAppViewContainer"] {{
# #                 background-image: url("data:image/png;base64,{encoded_image}");
# #                 background-size: cover;
# #                 background-position: center;
# #             }}
# #             [data-testid="stHeader"] {{
# #                 background-color: rgba(0,0,0,0);
# #             }}
# #             </style>
# #             """
# #         else:
# #             page_bg = ""

# #     st.markdown(page_bg, unsafe_allow_html=True)

# #     # ------------------ Question Bank ------------------
# #     question_bank = {
# #         "Math": {
# #             "Even & Odd": [
# #                 ("Is 45 even or odd?", "Odd"),
# #                 ("Is 100 even or odd?", "Even"),
# #                 ("Is 73 even or odd?", "Odd"),
# #             ],
# #             "Multiplication": [
# #                 ("What is 6 × 7?", "42"),
# #                 ("What is 9 × 9?", "81"),
# #                 ("What is 12 × 3?", "36"),
# #             ],
# #         },
# #         "Science": {

# #     "Physics": [
# #         ("What force pulls objects towards Earth?", "Gravity"),
# #         ("What is the speed of light in vacuum (approx)?", "300000 km/s"),
# #         ("Who is known as the father of modern physics?", "Albert Einstein"),
# #         ("What is the unit of force?", "Newton"),
# #         ("Which planet has the strongest gravity in our solar system?", "Jupiter"),
# #         ("What is the SI unit of energy?", "Joule"),
# #         ("Which law states that 'For every action, there is an equal and opposite reaction'?", "Newton's Third Law"),
# #         ("What type of energy is possessed by a moving object?", "Kinetic energy"),
# #         ("What happens to the volume of most materials when heated?", "It increases"),
# #         ("What is the center of mass of the Earth called?", "Core"),
# #     ],"Biology": [
# #     ("What organ pumps blood through the body?", "Heart"),
# #     ("What gas do humans breathe in to survive?", "Oxygen"),
# #     ("What gas do humans exhale?", "Carbon dioxide"),
# #     ("Which part of the plant carries out photosynthesis?", "Leaf"),
# #     ("What is the basic unit of life?", "Cell"),
# #     ("Which organ is responsible for filtering blood in humans?", "Kidney"),
# #     ("Which organ controls the body using electrical signals?", "Brain"),
# #     ("What pigment makes plants green?", "Chlorophyll"),
# #     ("How many chambers are there in the human heart?", "4"),
# #     ("Which system in the body is responsible for transporting blood?", "Circulatory system"),
# #     ("What type of blood cells help fight infections?", "White blood cells"),
# #     ("What is the largest organ in the human body?", "Skin"),
# #     ("What is the process by which plants make food?", "Photosynthesis"),
# #     ("Which part of the human body contains the smallest bones?", "Ear"),
# #     ("Which organ helps in digestion by producing bile?", "Liver"),
# # ]

# #         },
# #         "English": {
# #     "Grammar": [
# #         ("Which is correct: 'She go' or 'She goes'?", "She goes"),
# #         ("What is the plural of 'child'?", "Children"),
# #         ("Which is correct: 'They is happy' or 'They are happy'?", "They are happy"),
# #         ("What is the past tense of 'run'?", "Ran"),
# #         ("What is the comparative form of 'big'?", "Bigger"),
# #         ("Which article fits: 'I saw ___ apple on the table'?", "An"),
# #         ("Which is correct: 'He don’t like apples' or 'He doesn’t like apples'?", "He doesn’t like apples"),
# #         ("What is the plural of 'mouse'?", "Mice"),
# #         ("Fill in the blank: 'She ___ playing football yesterday.' (was / were)", "was"),
# #         ("Which is correct: 'I have went' or 'I have gone'?", "I have gone"),
# #         ("What is the superlative form of 'good'?", "Best"),
# #         ("Which is correct: 'There is many people' or 'There are many people'?", "There are many people"),
# #         ("What is the past tense of 'eat'?", "Ate"),
# #         ("Choose the correct pronoun: 'This is ___ book.' (my / mine)", "My"),
# #         ("Which is correct: 'He speak English' or 'He speaks English'?", "He speaks English"),
# #     ]
# # }
# #     }

# #     # ------------------ Session State ------------------
# #     if "score" not in st.session_state:
# #         st.session_state.score = 0
# #         st.session_state.total = 0
# #         st.session_state.current_q = None

# #     # ------------------ Quiz Section ------------------
# #     st.header("📝 Quiz Section")

# #     subject_choice = st.selectbox("Choose a subject:", list(question_bank.keys()))
# #     topic_choice = st.selectbox("Choose a topic:", list(question_bank[subject_choice].keys()))

# #     if st.button("Load Question"):
# #         st.session_state.current_q = random.choice(question_bank[subject_choice][topic_choice])

# #     if st.session_state.current_q:
# #         question, correct_answer = st.session_state.current_q
# #         st.write(f"❓ {question}")
# #         user_answer = st.text_input("Your Answer:")

# #         if st.button("Submit Answer"):
# #             st.session_state.total += 1
# #             if user_answer.strip().lower() == correct_answer.lower():
# #                 st.session_state.score += 1
# #                 st.success(f"✅ Correct! (+1)")
# #             else:
# #                 st.error(f"❌ Wrong! Correct: {correct_answer}")

# #         if st.button("Next Question"):
# #             st.session_state.current_q = random.choice(question_bank[subject_choice][topic_choice])
# #             st.rerun()

# #     # ------------------ Score Board ------------------
# #     st.subheader("📊 Your Performance")
# #     if st.session_state.total > 0:
# #         accuracy = (st.session_state.score / st.session_state.total) * 100
# #         st.write(f"✅ Score: {st.session_state.score}/{st.session_state.total} ({accuracy:.1f}%)")
# #     else:
# #         st.write("No questions answered yet.")

# #     # ------------------ Calculator ------------------
# #     st.header("🧮 Python Calculator")

# #     num1 = st.number_input("Enter the first number:", format="%.2f")
# #     num2 = st.number_input("Enter the second number:", format="%.2f")
# #     operation = st.selectbox("Select an operation:", ["+", "-", "*", "/"])

# #     if st.button("Calculate"):
# #         if operation == "+":
# #             st.success(f"Result: {num1} + {num2} = {num1+num2}")
# #         elif operation == "-":
# #             st.success(f"Result: {num1} - {num2} = {num1-num2}")
# #         elif operation == "*":
# #             st.success(f"Result: {num1} × {num2} = {num1*num2}")
# #         elif operation == "/":
# #             if num2 == 0:
# #                 st.error("Error: Cannot divide by zero")
# #             else:
# #                 st.success(f"Result: {num1} ÷ {num2} = {num1/num2:.2f}")
# #second code
# import streamlit as st
# import random
# import base64
# import os
# import time

# # ------------------ Button Glow Effect (Red) ------------------
# button_glow = """
# <style>
# div.stButton > button {
#     background-color: #12B0F4; /* Crimson Red */
#     color: white;
#     border: none;
#     padding: 0.6em 1.2em;
#     border-radius: 12px;
#     font-size: 16px;
#     font-weight: bold;
#     transition: all 0.3s ease-in-out;
#     box-shadow: 0px 0px 8px rgba(220, 20, 60, 0.4);
# }
# div.stButton > button:hover {
#     background-color: #FF4500; /* blue-Red hover */
#     box-shadow: 0px 0px 18px rgba(255, 69, 0, 0.9);
#     transform: scale(1.05);
# }
# </style>
# """
# st.markdown(button_glow, unsafe_allow_html=True)

# # ------------------ Dummy User Database ------------------
# if "users" not in st.session_state:
#     st.session_state.users = {"Greatness": "1234"}  # default user (no longer used)

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
#     st.session_state.current_user = None

# # ------------------ Sign Up & Login ------------------
# st.sidebar.title("🔑 Sign In")
# if not st.session_state.logged_in:
#     username = st.sidebar.text_input("👤 Username")
#     password = st.sidebar.text_input("🔒 Password", type="password")
#     if st.sidebar.button("Login"):
#         # ✅ Accept any username & password
#         st.session_state.logged_in = True
#         st.session_state.current_user = username if username.strip() else "Guest"
#         st.sidebar.success(f"✅ Welcome, {st.session_state.current_user}!")
#         st.rerun()
# else:
#     # ------------------ Main App (only after login) ------------------
#     st.sidebar.success(f"👋 Hello, {st.session_state.current_user}")
#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         st.session_state.current_user = None
#         st.rerun()

#     # 🏷️ Title
#     st.title("🎯 Subject Quiz & 🧮 Calculator")

#     # ------------------ Background Settings ------------------
#     bg_choice = st.radio("Choose background type:", ["Color", "Image"])
#     if bg_choice == "Color":
#         bg_color = st.color_picker("Pick a background color:", "#12B0F4")
#         page_bg = f"""
#         <style>
#         [data-testid="stAppViewContainer"] {{
#             background-color: {bg_color};
#             background-size: cover;
#         }}
#         [data-testid="stHeader"] {{
#             background-color: rgba(0,0,0,0);
#         }}
#         </style>
#         """
#     else:
#         bg_image = st.file_uploader("Upload a background image", type=["png", "jpg", "jpeg"])
#         if bg_image:
#             encoded_image = base64.b64encode(bg_image.read()).decode()
#             page_bg = f"""
#             <style>
#             [data-testid="stAppViewContainer"] {{
#                 background-image: url("data:image/png;base64,{encoded_image}");
#                 background-size: cover;
#                 background-position: center;
#             }}
#             [data-testid="stHeader"] {{
#                 background-color: rgba(0,0,0,0);
#             }}
#             </style>
#             """
#         else:
#             page_bg = ""
#     st.markdown(page_bg, unsafe_allow_html=True)

#     # ------------------ Question Bank ------------------
#     question_bank = {
#         "Math": {
#             "Even & Odd": [
#                 ("Is 45 even or odd?", "Odd"),
#                 ("Is 100 even or odd?", "Even"),
#                 ("Is 73 even or odd?", "Odd"),
#             ],
#             "Multiplication": [
#                 ("What is 6 × 7?", "42"),
#                 ("What is 9 × 9?", "81"),
#                 ("What is 12 × 3?", "36"),
#             ],
#         },
#         "Science": {
#             "Physics": [
#                 ("What force pulls objects towards Earth?", "Gravity"),
#                 ("What is the speed of light in vacuum (approx)?", "300000 km/s"),
#                 ("Who is known as the father of modern physics?", "Albert Einstein"),
#                 ("What is the unit of force?", "Newton"),
#                 ("Which planet has the strongest gravity in our solar system?", "Jupiter"),
#                 ("What is the SI unit of energy?", "Joule"),
#                 ("Which law states that 'For every action, there is an equal and opposite reaction'?", "Newton's Third Law"),
#                 ("What type of energy is possessed by a moving object?", "Kinetic energy"),
#                 ("What happens to the volume of most materials when heated?", "It increases"),
#                 ("What is the center of mass of the Earth called?", "Core"),
#             ],
#             "Biology": [
#                 ("What organ pumps blood through the body?", "Heart"),
#                 ("What gas do humans breathe in to survive?", "Oxygen"),
#             ]
#         },
#         "English": {
#             "Grammar": [
#                 ("Which is correct: 'She go' or 'She goes'?", "She goes"),
#                 ("What is the plural of 'child'?", "Children"),
#                 ("Which is correct: 'They is happy' or 'They are happy'?", "They are happy"),
#                 ("What is the past tense of 'run'?", "Ran"),
#                 ("What is the comparative form of 'big'?", "Bigger"),
#                 ("Which article fits: 'I saw ___ apple on the table'?", "An"),
#                 ("Which is correct: 'He don’t like apples' or 'He doesn’t like apples'?", "He doesn’t like apples"),
#                 ("What is the plural of 'mouse'?", "Mice"),
#                 ("Fill in the blank: 'She ___ playing football yesterday.' (was / were)", "was"),
#                 ("Which is correct: 'I have went' or 'I have gone'?", "I have gone"),
#                 ("What is the superlative form of 'good'?", "Best"),
#                 ("Which is correct: 'There is many people' or 'There are many people'?", "There are many people"),
#                 ("What is the past tense of 'eat'?", "Ate"),
#                 ("Choose the correct pronoun: 'This is ___ book.' (my / mine)", "My"),
#                 ("Which is correct: 'He speak English' or 'He speaks English'?", "He speaks English"),
#             ]
#         }
#     }

#     # ------------------ Session State ------------------
#     if "score" not in st.session_state:
#         st.session_state.score = 0
#         st.session_state.total = 0
#         st.session_state.current_q = None

#     # ------------------ Quiz Section ------------------
#     st.header("📝 Quiz Section")

#     subject_choice = st.selectbox("Choose a subject:", list(question_bank.keys()))
#     topic_choice = st.selectbox("Choose a topic:", list(question_bank[subject_choice].keys()))

#     if st.button("Load Question"):
#         st.session_state.current_q = random.choice(question_bank[subject_choice][topic_choice])

#     if st.session_state.current_q:
#         question, correct_answer = st.session_state.current_q
#         st.write(f"❓ {question}")
#         user_answer = st.text_input("Your Answer:")

#         if st.button("Submit Answer"):
#             st.session_state.total += 1
#             if user_answer.strip().lower() == correct_answer.lower():
#                 st.session_state.score += 1
#                 st.success(f"✅ Correct! (+1)")
#             else:
#                 st.error(f"❌ Wrong! Correct: {correct_answer}")

#         if st.button("Next Question"):
#             st.session_state.current_q = random.choice(question_bank[subject_choice][topic_choice])
#             st.rerun()

#     # ------------------ Score Board ------------------
#     st.subheader("📊 Your Performance")
#     if st.session_state.total > 0:
#         accuracy = (st.session_state.score / st.session_state.total) * 100
#         st.write(f"✅ Score: {st.session_state.score}/{st.session_state.total} ({accuracy:.1f}%)")
#     else:
#         st.write("No questions answered yet.")

#     # ------------------ Calculator ------------------
#     st.header("🧮 Python Calculator")
#     num1 = st.number_input("Enter the first number:", format="%.2f")
#     num2 = st.number_input("Enter the second number:", format="%.2f")
#     operation = st.selectbox("Select an operation:", ["+", "-", "*", "/"])

#     if st.button("Calculate"):
#         if operation == "+":
#             st.success(f"Result: {num1} + {num2} = {num1+num2}")
#         elif operation == "-":
#             st.success(f"Result: {num1} - {num2} = {num1-num2}")
#         elif operation == "*":
#             st.success(f"Result: {num1} × {num2} = {num1*num2}")
#         elif operation == "/":
#             if num2 == 0:
#                 st.error("Error: Cannot divide by zero")
#             else:
#                 st.success(f"Result: {num1} ÷ {num2} = {num1/num2:.2f}")
# import streamlit as st
# import random
# import base64
# import os

# # ------------------ Button Glow Effect (Red) ------------------
# button_glow = """
# <style>
# div.stButton > button {
#     background-color: #12B0F4; /* Crimson Red */
#     color: white;
#     border: none;
#     padding: 0.6em 1.2em;
#     border-radius: 12px;
#     font-size: 16px;
#     font-weight: bold;
#     transition: all 0.3s ease-in-out;
#     box-shadow: 0px 0px 8px rgba(220, 20, 60, 0.4);
# }
# div.stButton > button:hover {
#     background-color: #FF4500; /* blue-Red hover */
#     box-shadow: 0px 0px 18px rgba(255, 69, 0, 0.9);
#     transform: scale(1.05);
# }
# </style>
# """
# st.markdown(button_glow, unsafe_allow_html=True)

# # ------------------ Dummy User Database ------------------
# if "users" not in st.session_state:
#     st.session_state.users = {"Greatness": "1234"}

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
#     st.session_state.current_user = None

# # ------------------ Track Scores ------------------
# if "score" not in st.session_state:
#     st.session_state.score = 0
#     st.session_state.total = 0
#     st.session_state.highest_score = 0

# # ------------------ Track Menu ------------------
# if "menu" not in st.session_state:
#     st.session_state.menu = "Main Menu"

# # ------------------ Question Bank ------------------
# question_bank = {
#     "Easy": [
#         ("Is 45 even or odd?", "Odd"),
#         ("What organ pumps blood?", "Heart"),
#         ("Which is correct: 'She go' or 'She goes'?", "She goes"),
#     ],
#     "Hard": [
#         ("What is the speed of light (approx)?", "300000 km/s"),
#         ("Which law says 'For every action, there is an equal and opposite reaction'?", "Newton's Third Law"),
#         ("What is the superlative form of 'good'?", "Best"),
#     ]
# }

# # ------------------ Sign Up & Login ------------------
# st.sidebar.title("🔑 Sign In")
# if not st.session_state.logged_in:
#     username = st.sidebar.text_input("👤 Username")
#     password = st.sidebar.text_input("🔒 Password", type="password")
#     if st.sidebar.button("Login"):
#         st.session_state.logged_in = True
#         st.session_state.current_user = username if username.strip() else "Guest"
#         st.sidebar.success(f"✅ Welcome, {st.session_state.current_user}!")
#         st.rerun()
# else:
#     st.sidebar.success(f"👋 Hello, {st.session_state.current_user}")
#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         st.session_state.current_user = None
#         st.session_state.menu = "Main Menu"
#         st.rerun()

#     # ------------------ MAIN MENU ------------------
#     if st.session_state.menu == "Main Menu":
#         st.title("🏠 Main Menu")
#         st.write("Choose what you want to do:")

#         if st.button("🎮 Play Game"):
#             st.session_state.menu = "Game"
#             st.rerun()

#         if st.button("📝 Take a Quiz (Easy)"):
#             st.session_state.menu = "Quiz Easy"
#             st.rerun()

#         if st.button("📝 Take a Quiz (Hard)"):
#             st.session_state.menu = "Quiz Hard"
#             st.rerun()

#         if st.button("📊 Highest Score"):
#             st.session_state.menu = "Highest Score"
#             st.rerun()

#     # ------------------ GAME SECTION ------------------
#     elif st.session_state.menu == "Game":
#         st.title("🎮 Simple Game")
#         st.write("👉 Game coming soon...")
#         if st.button("⬅️ Back to Menu"):
#             st.session_state.menu = "Main Menu"
#             st.rerun()

#     # ------------------ QUIZ SECTION ------------------
#     elif st.session_state.menu in ["Quiz Easy", "Quiz Hard"]:
#         difficulty = "Easy" if "Easy" in st.session_state.menu else "Hard"
#         st.title(f"📝 {difficulty} Quiz")

#         if "current_q" not in st.session_state:
#             st.session_state.current_q = None

#         if st.button("Load Question"):
#             st.session_state.current_q = random.choice(question_bank[difficulty])

#         if st.session_state.current_q:
#             question, correct_answer = st.session_state.current_q
#             st.write(f"❓ {question}")
#             user_answer = st.text_input("Your Answer:")

#             if st.button("Submit Answer"):
#                 st.session_state.total += 1
#                 if user_answer.strip().lower() == correct_answer.lower():
#                     st.session_state.score += 1
#                     st.success("✅ Correct!")
#                 else:
#                     st.error(f"❌ Wrong! Correct: {correct_answer}")

#                 # Update highest score
#                 if st.session_state.score > st.session_state.highest_score:
#                     st.session_state.highest_score = st.session_state.score

#             if st.button("Next Question"):
#                 st.session_state.current_q = random.choice(question_bank[difficulty])
#                 st.rerun()

#         st.subheader("📊 Your Performance")
#         if st.session_state.total > 0:
#             accuracy = (st.session_state.score / st.session_state.total) * 100
#             st.write(f"✅ Score: {st.session_state.score}/{st.session_state.total} ({accuracy:.1f}%)")
#             st.write(f"🏆 Highest Score: {st.session_state.highest_score}")
#         else:
#             st.write("No questions answered yet.")

#         if st.button("⬅️ Back to Menu"):
#             st.session_state.menu = "Main Menu"
#             st.rerun()

#     # ------------------ HIGHEST SCORE SECTION ------------------
#     elif st.session_state.menu == "Highest Score":
#         st.title("🏆 Highest Score")
#         st.write(f"👤 {st.session_state.current_user}: **{st.session_state.highest_score} points**")
#         if st.button("⬅️ Back to Menu"):
#             st.session_state.menu = "Main Menu"
#             st.rerun()
import streamlit as st
import random
import base64

# ------------------ Button Glow Effect ------------------
button_glow = """
<style>
div.stButton > button {
    background-color: #12B0F4; /* Crimson white */
    color: white;
    border: none;
    padding: 0.6em 1.2em;
    border-radius: 12px;
    font-size: 16px;
    font-weight: bold;
    transition: all 0.3s ease-in-out;
    box-shadow: 0px 0px 8px rgba(220, 20, 60, 0.4);
}
div.stButton > button:hover {
    background-color: #FF4500; /* black-white hover */
    box-shadow: 0px 0px 18px rgba(255, 69, 0, 0.9);
    transform: scale(1.05);
}
</style>
"""
st.markdown(button_glow, unsafe_allow_html=True)

# ------------------ Session State ------------------
if "users" not in st.session_state:
    st.session_state.users = {"Greatness": "1234"}  # default

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.current_user = None

if "menu" not in st.session_state:
    st.session_state.menu = "Main Menu"

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.highest_score = 0
    st.session_state.current_q = None

# ------------------ Sign In ------------------
st.sidebar.title("🔑 Sign In")
if not st.session_state.logged_in:
    username = st.sidebar.text_input("👤 Username")
    password = st.sidebar.text_input("🔒 Password", type="password")
    if st.sidebar.button("Login"):
        st.session_state.logged_in = True
        st.session_state.current_user = username if username.strip() else "Guest"
        st.sidebar.success(f"✅ Welcome, {st.session_state.current_user}!")
        st.rerun()
else:
    st.sidebar.success(f"👋 Hello, {st.session_state.current_user}")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.session_state.menu = "Main Menu"
        st.rerun()

    # ------------------ Background Settings ------------------
    bg_choice = st.radio("🎨 Choose background type:", ["Color", "Image"])
    if bg_choice == "Color":
        bg_color = st.color_picker("Pick a background color:", "#0A0B0B")
        page_bg = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-color: {bg_color};
            background-size: cover;
        }}
        [data-testid="stHeader"] {{ background-color: rgba(0,0,0,0); }}
        </style>
        """
    else:
        bg_image = st.file_uploader("Upload a background image", type=["png", "jpg", "jpeg"])
        if bg_image:
            encoded_image = base64.b64encode(bg_image.read()).decode()
            page_bg = f"""
            <style>
            [data-testid="stAppViewContainer"] {{
                background-image: url("data:image/png;base64,{encoded_image}");
                background-size: cover;
                background-position: center;
            }}
            [data-testid="stHeader"] {{ background-color: rgba(0,0,0,0); }}
            </style>
            """
        else:
            page_bg = ""
    st.markdown(page_bg, unsafe_allow_html=True)

    # ------------------ Question Bank ------------------
    question_bank = {
        "Math": {
            "Even & Odd": [
                ("Is 45 even or odd?", "Odd"),
                ("Is 100 even or odd?", "Even"),
                ("Is 73 even or odd?", "Odd"),
            ],
            "Multiplication": [
                ("What is 6 × 7?", "42"),
                ("What is 9 × 9?", "81"),
                ("What is 12 × 3?", "36"),
            ],
            "Division": [
                ("What is 100 ÷ 25?", "4"),
                ("What is 49 ÷ 7?", "7"),
                ("What is 81 ÷ 9?", "9"),
            ]
        },
        "Science": {
            "Physics": [
                ("What force pulls objects towards Earth?", "Gravity"),
                ("What is the speed of light in vacuum (approx)?", "300000 km/s"),
                ("Who is known as the father of modern physics?", "Albert Einstein"),
            ],
            "Biology": [
                ("What organ pumps blood through the body?", "Heart"),
                ("What gas do humans breathe in to survive?", "Oxygen"),
            ],
            "Chemistry": [
                ("What is H2O commonly known as?", "Water"),
                ("What gas do plants release during photosynthesis?", "Oxygen"),
            ]
        },
        "English": {
            "Grammar": [
                ("Which is correct: 'She go' or 'She goes'?", "She goes"),
                ("What is the plural of 'child'?", "Children"),
                ("What is the past tense of 'run'?", "Ran"),
                ("What is the superlative form of 'good'?", "Best"),
            ],
            "Vocabulary": [
                ("What is a synonym for 'happy'?", "Joyful"),
                ("What is the opposite of 'hot'?", "Cold"),
             ],
             "Reading": [
                 ("Who wrote 'Romeo and Juliet'?", "Shakespeare"),
                 ("In 'The Three Little Pigs', what blew the houses down?", "Wolf"),
            ]
            
        }
    }

    # ------------------ MAIN MENU ------------------
    if st.session_state.menu == "Main Menu":
        st.title("🏠 Main Menu")
        st.write("Choose what you want to do:")

        if st.button("🎮 Play Game"):
            st.session_state.menu = "Game"
            st.rerun()
        if st.button("📝 Take a Quiz"):
            st.session_state.menu = "Quiz"
            st.rerun()
        if st.button("🧮 Calculator"):
            st.session_state.menu = "Calculator"
            st.rerun()
        if st.button("🏆 Highest Score"):
            st.session_state.menu = "Highest Score"
            st.rerun()

    # ------------------ GAME SECTION ------------------
    elif st.session_state.menu == "Game":
        st.title("🎮 Simple Game")
        st.write("👉 Game coming soon...")
        if st.button("⬅️ Back to Menu"):
            st.session_state.menu = "Main Menu"
            st.rerun()

    # ------------------ QUIZ SECTION ------------------
    elif st.session_state.menu == "Quiz":
        st.title("📝 Subject Quiz")

        subject_choice = st.selectbox("Choose a subject:", list(question_bank.keys()))
        topic_choice = st.selectbox("Choose a topic:", list(question_bank[subject_choice].keys()))

        if st.button("Load Question"):
            st.session_state.current_q = random.choice(question_bank[subject_choice][topic_choice])

        if st.session_state.current_q:
            question, correct_answer = st.session_state.current_q
            st.write(f"❓ {question}")
            user_answer = st.text_input("Your Answer:")

            if st.button("Submit Answer"):
                st.session_state.total += 1
                if user_answer.strip().lower() == correct_answer.lower():
                    st.session_state.score += 1
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Wrong! Correct: {correct_answer}")

                if st.session_state.score > st.session_state.highest_score:
                    st.session_state.highest_score = st.session_state.score

            if st.button("Next Question"):
                st.session_state.current_q = random.choice(question_bank[subject_choice][topic_choice])
                st.rerun()

        st.subheader("📊 Your Performance")
        if st.session_state.total > 0:
            accuracy = (st.session_state.score / st.session_state.total) * 100
            st.write(f"✅ Score: {st.session_state.score}/{st.session_state.total} ({accuracy:.1f}%)")
            st.write(f"🏆 Highest Score: {st.session_state.highest_score}")
        else:
            st.write("No questions answered yet.")

        if st.button("⬅️ Back to Menu"):
            st.session_state.menu = "Main Menu"
            st.rerun()

    # ------------------ CALCULATOR ------------------
    elif st.session_state.menu == "Calculator":
        st.title("🧮 Python Calculator")
        num1 = st.number_input("Enter the first number:", format="%.2f")
        num2 = st.number_input("Enter the second number:", format="%.2f")
        operation = st.selectbox("Select an operation:", ["+", "-", "*", "/"])

        if st.button("Calculate"):
            if operation == "+":
                st.success(f"Result: {num1} + {num2} = {num1+num2}")
            elif operation == "-":
                st.success(f"Result: {num1} - {num2} = {num1-num2}")
            elif operation == "*":
                st.success(f"Result: {num1} × {num2} = {num1*num2}")
            elif operation == "/":
                if num2 == 0:
                    st.error("Error: Cannot divide by zero")
                else:
                    st.success(f"Result: {num1} ÷ {num2} = {num1/num2:.2f}")

        if st.button("⬅️ Back to Menu"):
            st.session_state.menu = "Main Menu"
            st.rerun()

    # ------------------ HIGHEST SCORE ------------------
    elif st.session_state.menu == "Highest Score":
        st.title("🏆 Highest Score")
        st.write(f"👤 {st.session_state.current_user}: **{st.session_state.highest_score} points**")
        if st.button("⬅️ Back to Menu"):
            st.session_state.menu = "Main Menu"
            st.rerun()