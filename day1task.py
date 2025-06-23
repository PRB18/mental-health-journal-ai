
import streamlit as st

st.set_page_config(page_title="Mental Health Journal" ,layout="centered")
st.title("Mental Health Dashboard")


def summary(mood,entry,date):
	st.success("Thanks for the details nigga!")
	st.write("Date: ", date)
	st.markdown(f"""
	 **Your mood is: ** {mood}  
	 **You day was like this : ** {entry}
	 """)



mood= st.selectbox("Select your mood: ", ["Happy","Sad","Okay","Depressed","Freaky"])


entry=st.text_area("How was your day? ")

date=st.date_input("enter the date: ")

if st.button("Submit"):
	summary(mood,entry,date)


	
	
