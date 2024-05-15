import streamlit as st

from streamlit_option_menu import option_menu


import home, upload, dashboard, Assesment,Information
st.set_page_config(
        page_title="ASD",
        page_icon=":smiley:"
)


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": function
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='ASD ',
                options=['Home','Upload','dashboard','assesment','Information'],
                icons=['house-fill','upload','list-task','bar-chart-fill','info-circle-fill'],
                menu_icon='menu-button-fill',
                default_index=1
                
                )

        
        if app == "Home":
            home.app()
        if app == "Upload":
            upload.app()    
        if app == "dashboard":
            dashboard.app()        
        if app == 'assesment':
            Assesment.app()
        if app == "Information":
            Information.app()    
            
             
          
             
    run()            
         