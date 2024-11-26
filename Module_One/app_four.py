import streamlit as st
import pandas as pd
from datetime import datetime

# --- Initialize Session State ---
if "timeline" not in st.session_state:
    st.session_state["timeline"] = []
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []
if "uploaded_notes" not in st.session_state:
    st.session_state["uploaded_notes"] = []

# --- Helper Functions ---
def add_task(task_name, description, due_date):
    st.session_state["tasks"].append({
        "Task Name": task_name,
        "Description": description,
        "Due Date": due_date,
        "Completed": False
    })

def mark_task_complete(index):
    st.session_state["tasks"][index]["Completed"] = True

# --- App Title ---
st.title("📚 LearnTrack: Your Learning Timeline Manager")

# --- Sidebar Navigation ---
st.sidebar.header("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Timeline", "Tasks", "Notes"])

# --- Home Page ---
if page == "Home":
    st.header("Welcome to LearnTrack!")
    st.write("""
        Track your learning progress, manage tasks, upload notes, and stay on top of your goals.
    """)
    st.image("https://via.placeholder.com/800x400?text=Learning+Made+Easy", use_column_width=True)

    st.markdown("### Features:")
    st.markdown("""
    - 📅 **Timeline Creation**: Visualize your learning journey.
    - ✅ **Task Management**: Stay organized with task tracking.
    - 📝 **Notes Upload**: Keep all your notes in one place.
    - 📊 **Progress Tracking**: Stay motivated and complete your goals!
    """)

# --- Timeline Page ---
# --- Timeline Page ---
elif page == "Timeline":
    st.header("📅 Your Learning Timeline")
    
    # Form to Add Timeline Events
    with st.form("Add Timeline Event"):
        title = st.text_input("Milestone Title")
        date = st.date_input("Target Date", min_value=datetime.today())
        submit = st.form_submit_button("Add Milestone")
        
        if submit and title:
            st.session_state["timeline"].append({
                "Milestone": title,
                "Date": date
            })
            st.success("Milestone added!")
    
    # Display Timeline and Progress Bars
    if st.session_state["timeline"]:
        st.write("### Your Milestones:")
        today = datetime.today()
        for milestone in st.session_state["timeline"]:
            milestone_title = milestone["Milestone"]
            due_date = milestone["Date"]
            days_left = (due_date - today.date()).days

            if days_left > 0:
                st.write(f"**{milestone_title}** - 🗓️ {due_date} ({days_left} days to go!)")
                progress = 100 - ((days_left / max(days_left, 30)) * 100)  # Assuming 30 days as max
                st.progress(progress / 100)
            elif days_left == 0:
                st.write(f"**{milestone_title}** - 🗓️ {due_date} (Today is the day! 🚀)")
                st.progress(1.0)
            else:
                st.write(f"**{milestone_title}** - 🗓️ {due_date} (Overdue by {-days_left} days 😔)")
                st.progress(0.0)
    else:
        st.write("No milestones added yet. Start by adding one above!")


# --- Tasks Page ---
elif page == "Tasks":
    st.header("✅ Task Management")
    
    # Tabs for Pending and Completed Tasks
    tab1, tab2 = st.tabs(["📋 Pending Tasks", "✅ Completed Tasks"])
    
    # --- Pending Tasks ---
    with tab1:
        # Add Task Form
        with st.form("Add Task"):
            task_name = st.text_input("Task Name")
            description = st.text_area("Description")
            due_date = st.date_input("Due Date", min_value=datetime.today())
            submit_task = st.form_submit_button("Add Task")
            
            if submit_task and task_name:
                add_task(task_name, description, due_date)
                st.success("Task added successfully!")
        
        # Display Pending Tasks
        pending_tasks = [task for task in st.session_state["tasks"] if not task["Completed"]]
        if pending_tasks:
            st.write("### Your Pending Tasks:")
            for idx, task in enumerate(pending_tasks):
                col1, col2, col3 = st.columns([3, 2, 1])
                col1.write(f"**{task['Task Name']}** - {task['Description']}")
                col2.write(f"Due: {task['Due Date']}")
                if col3.button("Mark Complete", key=f"complete_{idx}"):
                    task_index = st.session_state["tasks"].index(task)
                    mark_task_complete(task_index)
        else:
            st.write("No pending tasks! 🎉")
    
    # --- Completed Tasks ---
    with tab2:
        completed_tasks = [task for task in st.session_state["tasks"] if task["Completed"]]
        if completed_tasks:
            st.write("### Your Completed Tasks:")
            for task in completed_tasks:
                st.write(f"✔️ **{task['Task Name']}** - {task['Description']}")
        else:
            st.write("No completed tasks yet. Keep going! 🚀")
    
    # Progress Tracking
    total_tasks = len(st.session_state["tasks"])
    completed_tasks_count = len([task for task in st.session_state["tasks"] if task["Completed"]])
    if total_tasks > 0:
        progress = (completed_tasks_count / total_tasks) * 100
        st.sidebar.write(f"### Progress: {completed_tasks_count}/{total_tasks} tasks completed")
        st.sidebar.progress(progress / 100)
    else:
        st.sidebar.write("### No tasks yet. Add some to get started!")

# --- Notes Page ---
elif page == "Notes":
    st.header("📝 Notes Upload")
    
    # File Uploader
    uploaded_file = st.file_uploader("Upload your learning material (PDF, DOCX, TXT):", type=["pdf", "docx", "txt"])
    if uploaded_file:
        st.session_state["uploaded_notes"].append(uploaded_file.name)
        with open(f"uploaded_{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    
    st.write("### Uploaded Notes:")
    if st.session_state["uploaded_notes"]:
        for note in st.session_state["uploaded_notes"]:
            st.write(f"- {note}")
    else:
        st.write("No notes uploaded yet.")

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.write("💡 Stay consistent and finish your goals!")
