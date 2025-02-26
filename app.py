import streamlit as st

# Set page configuration for a better title and layout
st.set_page_config(page_title="Stylish To-Do List", page_icon="📝", layout="wide")

# Title for the app
st.title("🎯 Stylish To-Do List 🎯")

# Initialize session state if it doesn't exist yet
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Function to add tasks
def add_task(task_name, category, priority):
    st.session_state.tasks.append({"task": task_name, "category": category, "priority": priority, "completed": False})

# Function to remove tasks
def remove_task(task):
    st.session_state.tasks.remove(task)

# Function to mark task as completed
def mark_completed(task):
    task["completed"] = not task["completed"]

# Custom styling for the To-Do List
st.markdown("""
    <style>
        .stButton > button {
            background-color: #FF6347;
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 15px;
            padding: 10px 30px;
            width: 100%;
        }
        .stButton > button:hover {
            background-color: #E74C3C;
        }
        .task-card {
            background-color: #f0f4f8;
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .task-header {
            font-size: 20px;
            font-weight: bold;
            color: #34495E;
        }
        .task-category {
            font-size: 14px;
            color: #7f8c8d;
        }
        .task-priority {
            font-size: 14px;
            color: #FF6347;
        }
        .completed {
            text-decoration: line-through;
            color: grey;
        }
        .stTextInput input {
            font-size: 18px;
            padding: 12px;
        }
    </style>
    """, unsafe_allow_html=True)

# Input fields to add a new task
new_task_name = st.text_input("Task Name", placeholder="Enter your task here...")
task_category = st.selectbox("Category", ["Work", "Personal", "Study", "Other"])
task_priority = st.selectbox("Priority", ["High", "Medium", "Low"])

# Add task button
if st.button("Add Task"):
    if new_task_name:
        add_task(new_task_name, task_category, task_priority)
        st.success(f"Task '{new_task_name}' added successfully!")
    else:
        st.warning("Please enter a task name!")

# Display the list of tasks
st.subheader("📋 Your Tasks:")

# Display tasks in a styled format
for task in st.session_state.tasks:
    task_card = st.container()
    with task_card:
        # Display task name with strikethrough if completed
        task_class = "completed" if task["completed"] else ""
        
        # Task card header
        st.markdown(f"<div class='task-card'><div class='task-header {task_class}'> {task['task']} </div>", unsafe_allow_html=True)
        st.markdown(f"<div class='task-category'>Category: {task['category']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='task-priority'>Priority: {task['priority']}</div>", unsafe_allow_html=True)

        # Buttons to mark task completed or delete
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            if st.button("✅ Mark as Done" if not task["completed"] else "❌ Mark as Not Done", key=task["task"]):
                mark_completed(task)
        with col2:
            if st.button("❌ Delete", key=f"delete_{task['task']}"):
                remove_task(task)
                st.success(f"Task '{task['task']}' removed!")

        st.markdown("</div>", unsafe_allow_html=True)

# Clear all tasks button
if st.button("Clear All Tasks"):
    st.session_state.tasks.clear()
    st.success("All tasks have been cleared!")

