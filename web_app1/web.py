import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("To do app")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

st.checkbox("Way to go")
st.checkbox("Congratulations")

todos = functions.get_todos()
for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        st.experimental_rerun()

st.text_input(label='Enter to-do',
              placeholder='please enter todo',
              label_visibility='hidden',
              on_change=add_todo, key='new_todo',)

