import streamlit as st
import streamlit_authenticator as stauth

names = ["John Smith","Rebecca Briggs"]
usernames = ["jsmith","rbriggs"]
passwords = ["123","456"]

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
	names, usernames, hashed_passwords, "some_cookie_name", "some_signature_key", cookie_expiry_days=30
)


name, authentication_status, username = authenticator.login("Login", "sidebar")

if authentication_status:
	authenticator.logout("Logout", "sidebar")
	st.write(f"Welcome *{name}*")
	st.title("Some content")

elif authentication_status == False:
	st.error("Username/password is incorrect")

elif authentication_status == None:
	st.warning("Please enter your username and password")