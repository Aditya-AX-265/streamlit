import streamlit as st
import requests

api_url = "https://dev-api.nextvue.io/api/starter/getAeratorUpByAerator"

def fetch_data(start_date, end_date, location_id):
    params = {
        "startDate": start_date,
        "endDate": end_date,
        "locationId": location_id
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    st.title("Aerator Data Table")

    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    location_id = st.text_input("Location ID")

    start_datetime = str(start_date) + "T00:00:00.000"
    end_datetime = str(end_date) + "T23:59:00.000"

    if st.button("Fetch Data"):
        if start_date and end_date and location_id:
            data = fetch_data(start_datetime, end_datetime, location_id)
            if data:
                st.write("### Fetched Data:")
                # st.write(data)
                st.table(data)
            else:
                st.write("Failed to fetch data. Please check your input.")
        else:
            st.write("Please provide all required inputs.")

if __name__ == "__main__":
    main()
# import requests

# def get_farmer_farms_by_phone_number(phone_number, token):
#     base_url = 'http://app.aquaexchange.com/api/farmer/farmsbymobilenumber/'
#     url = f'{base_url}{phone_number}/'
#     headers = {'Authorization': f'Token {token}'}

#     try:
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             raise Exception('Failed to fetch farmer farms by phone number')
#     except Exception as e:
#         print("Error:", e)
#         return {}

# # Example usage:
# phone_number = '8617756280'  
# token = 'e50f000f342fe8453e714454abac13be07f18ac3'  
# result = get_farmer_farms_by_phone_number(phone_number, token)
# print(result)
