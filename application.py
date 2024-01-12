# Importing the Necessary Libraires
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
import gc
import time

# Reading csv file
df = pd.read_csv("Singapore Flat Resale Price.csv")


# Function to predict flat resale price
def predict(year, month, flat_type, flat_model, floor_area, town, lease_commence_date, storey_range):
   
   global df
   
   tn = dict(zip(df["town"],df["town_encode"]))
   ft = dict(zip(df["flat_type"],df["flat_type_encode"]))
   fm = dict(zip(df["flat_model"],df["flat_model_encode"]))

   with open("best_model.pkl", "rb") as file:
      model = pickle.load(file)

   town_en = tn[town]
   flat_type_en = ft[flat_type]
   flat_model_en = fm[flat_model]
   min_storey, max_storey = storey_range.lower().split("to")

   prediction = model.predict([[year, 
                                 month, 
                                 int(flat_type_en), 
                                 int(flat_model_en), 
                                 floor_area, 
                                 int(town_en), 
                                 lease_commence_date, 
                                 int(min_storey), 
                                 int(max_storey)]])
   del model
   del df
   gc.collect()
   return prediction
   
   
      
# Streamlit Setup
st.set_page_config("Singapore Resale Flat Price Prediction", layout = "wide") 


selected = option_menu(None,
                       options = ["Menu", "Price Prediction"],
                       icons = ["house"],
                       orientation = "horizontal",
                       styles = {"nav-link": {"font-size": "18px", "text-align": "center", "margin": "1px"},
                                 "icon": {"color": "yellow", "font-size": "20px"},
                                 "nav-link-selected": {"background-color": "#9457eb"}})


if selected == "Menu":
   st.title(":blue[**Singapore Resale Flat Price Prediction**]")

   st.markdown("")

   st.markdown('''* The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application 
                    that predicts the resale prices of flats in Singapore.''')
   st.markdown('''* This predictive model will be based on historical data of resale flat transactions, and it aims to assist both 
                    potential buyers and sellers in estimating the resale value of a flat.''')


if selected == "Price Prediction":

   with st.form("predict"):

      col1, col2, col3= st.columns(3)
      with col1:
         st.number_input(":blue[Year]", value = 2024, step = 1, key = "yr")

         st.markdown("") 

         st.number_input(":blue[Floor Area]", value = 80.0, step = 0.01, key = "fa")
          
         st.number_input(":blue[Lease Commence Date]", value = 1980, step = 1, key = "lcd")
         

      with col2:
         st.slider(":blue[Month]", min_value = 1, max_value = 12, key = "mn")

         st.selectbox(":blue[Town]", options = df["town"].unique(), key = "tn")
          
         st.text_input(":blue[Storey Range]", value = "1 to 4" , placeholder = "Eg: 1 To 4", key = "sr")
         

      with col3:
         st.selectbox(":blue[Flat Type]", options = df["flat_type"].unique(), key = "ft")
         
         st.markdown("")

         st.selectbox(":blue[Flat Model]", options = df["flat_model"].unique(), key = "fm")


      if st.form_submit_button("Predict"):

         if st.session_state["sr"] != "":
            
            try:
               price_pred = predict(st.session_state["yr"], st.session_state["mn"], st.session_state["ft"], st.session_state["fm"],
                                    st.session_state["fa"], st.session_state["tn"], st.session_state["lcd"], st.session_state["sr"])        
               with st.success(f"The Predicted Price is  :green[$ {price_pred[0]:,.0f}]"):
                  time.sleep(10)
                  st.empty()          
            except:
               st.error(":red[ERROR:] Please Enter Valid Details")

         else:
            st.error(":red[ERROR:] Please fill in :red['storey range']")



# -----------------------x-------------------------x--------------------------x------------------------x----------------------x--------------------x----------------------------------------------
     

   





