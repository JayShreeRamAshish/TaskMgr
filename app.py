import streamlit as st
import pandas as pd
import streamlit.components.v1 as stc
from db_fxns import *


# Set page configuration
st.set_page_config(
    page_title="Task Management System",
    page_icon="🔢",
    layout="wide",  # You can also use "centered"
    initial_sidebar_state="expanded"  # You can also use "collapsed"
)
# Your Streamlit code

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:2px;border-radius:5px">
    <h1 style="color:white;text-align:center;">Task Management System</h1>
    <p style="color:white;text-align:center;">Jay Shree Ram</p>
    </div>
    """
def main():
	
    stc.html(HTML_BANNER)

    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()
    if choice == "Create":
        st.subheader("Create your Task")
        ticket_number=st.text_input("Enter Ticket Number")
        ticket_creation_date=st.date_input("Ticekt Creation Date")
        client_name=st.text_input("Client Name")
        ticket_assigned=st.text_input("Ticekt Assigned")
        ticket_discription =st.text_area("Ticket Discription")
        ticket_deadline=st.date_input("Ticekt Deadline")
        ticket_satatus=st.selectbox("Status",["Open","Pendin","Completed","Closed","Pending for Approval","Hold"])
        
        if st.button("Add Task"):
            add_data(ticket_number,ticket_creation_date,client_name,ticket_assigned,ticket_discription,ticket_deadline,ticket_satatus)
            st.success("Added ::{} ::To Task".format(ticket_number))

        # Add your create functionality here

    elif choice == "Read":
		# st.subheader("View Items")
        result = view_all_data()
        st.dataframe(result)

    elif choice == "Update":
        st.subheader("Update")
        # Add your update functionality here

    elif choice == "Delete":
        st.subheader("Delete")
        # Add your delete functionality here

    elif choice == "About":
        st.subheader("About")
        # Add your about information here
   

if __name__ == '__main__':
    main()
