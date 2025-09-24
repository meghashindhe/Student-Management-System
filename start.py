import streamlit as st
from datetime import date
from crud import add_student, get_students, delete_student, update_student
from validators import is_valid_email

st.title('Student Management System')

actions = ['Add Student','Update Student', 'Delete Student', 'View Students']
st.sidebar.write('Manage students easily')
choice = st.sidebar.selectbox('Actions', actions)


#adding student
if choice == 'Add Student':
    st.subheader('Add Student')
    student_id = st.text_input('Student ID',placeholder='Enter unique student ID')
    name = st.text_input('Name')
    email = st.text_input('Email')
    dob_str = st.date_input(
        "Date of Birth",
        min_value=date(1990,1,1),
        max_value=date.today()
    )
    phone = st.text_input('Phone')

    if st.button('Add'):
        if not student_id or not name or not email:
            st.error("Student ID, Name, and Email are required fields")

        elif not student_id.isdigit():
            st.error("Please enter a numeric Student ID")

        elif not is_valid_email(email):
            st.error('Please enter a valid email address')
        
        elif len(phone) != 10 or not phone.isdigit():
            st.error("Phone number must be exactly 10 digits")

        else:
            student_id = int(student_id)
            success = add_student(student_id, name, email, dob_str, phone)
            if success:
                st.success('Student added successfully')
            else:
                st.warning('Student ID already exists')

#updating student
elif choice == 'Update Student':
    st.subheader('Update Students')
    df = get_students()
    st.dataframe(df)

    student_id = st.text_input('enter Student ID to update')
    name = st.text_input('New Name')
    email = st.text_input('New Email')
    dob_str = st.date_input('New Date Of Birth')
    phone = st.text_input('New Phone')

    if st.button('update'):
        if not student_id or not name or not email:
            st.error("Student ID, Name, and Email are required fields")
        elif not student_id.isdigit():
            st.error("Please enter a numeric Student ID")
        elif not is_valid_email(email):
            st.error('Please enter a valid email address')

        elif len(phone) != 10 or not phone.isdigit():
            st.error("Phone number must be exactly 10 digits")

        else:
            student_id = int(student_id)
            rows = update_student(student_id, name, email, dob_str, phone)
            if rows > 0:
                st.success('Student updated successfully')
                df = get_students()
                st.dataframe(df)

            else:
                st.warning("No student found with that ID.")


#delete student
elif choice == 'Delete Student':
    st.subheader('Delete Student')
    df = get_students()
    st.dataframe(df)

    student_id = st.text_input('Enter Student ID to delete')
    if st.button("Delete"):
        if not student_id.isdigit():
            st.error("Please enter a numeric Student ID")
        else:
            student_id = int(student_id)
            rows = delete_student(student_id)
            if rows > 0:
                st.success('Student deleted successfully')
                df = get_students()
                st.dataframe(df)
            else:
                st.warning("No student found with that ID.")



#view students
elif choice == 'View Students':
    st.subheader('All Students')
    df = get_students()
    st.dataframe(df)
