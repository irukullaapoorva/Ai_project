import streamlit as st
import joblib, os
import pickle


# Loading Models
def load_prediction_model(model_file):
	return joblib.load(open(os.path.join(model_file),"rb"))


def main():
    st.title("Hotel Booking Demand")


    lead_time = st.number_input("Enter Lead Time", step=1, min_value=0)
    arrival_date_week_number = st.number_input("Arrival Date Week Number", step=1, min_value=0)
    stays_in_weekend_nights = st.number_input("Stays in Weekend Night", step=1, min_value=0)
    stays_in_week_nights = st.number_input("stays in week Nights", step=1, min_value=0)
    adults = st.number_input("Adults", step=1, min_value=0)
    babies = st.number_input("Babies", step=1, min_value=0)
    model = pickle.load(open('model.pkl', 'rb'))

    pred = model.predict([[lead_time, arrival_date_week_number, stays_in_weekend_nights, stays_in_week_nights, adults, babies]])
    if st.button("Predict:"):

        if (babies or stays_in_weekend_nights >=4):
            st.success("Resort Hotel")

        elif pred[0]==1:
            st.success("Resort Hotel")

        elif pred[0]==0 or (babies and stays_in_weekend_nights <3):
            st.success("City Hotel")




if __name__ == '__main__':
    main()