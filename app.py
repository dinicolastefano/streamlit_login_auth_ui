import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

__login__obj = __login__(auth_token = "pk_prod_RKE7Q0BBDKMTDTKJVG15EKPXFXT4",
                    company_name = "Shims",
                    width = 200, height = 250,
                    logout_button_name = 'Logout', hide_menu_bool = False,
                    hide_footer_bool = False,
                    lottie_url = 'https://budgyai-ksk3w7wlp2yic2cuobbpsr.streamlit.app/')

LOGGED_IN= __login__obj.build_login_ui()
username= __login__obj.get_username()

if LOGGED_IN == True:

   st.markdown("Your Streamlit Application Begins here!")
   st.markdown(st.session_state)
   st.write(username)
                                      
