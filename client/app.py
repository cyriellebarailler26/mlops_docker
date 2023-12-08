import streamlit as st
import requests

def main():
    st.title("Fruit Adder App")

    # Input for the fruit name
    fruit_name = st.text_input("Enter a fruit name:")

    # Button to add the fruit
    if st.button("Add Fruit"):
        if fruit_name:
            # Make a request to the server
            server_url = "http://server:8000/add/{}".format(fruit_name)
            response = requests.get(server_url)

            # Display the result
            if response.status_code == 200:
                st.success("Fruit added successfully!")
            else:
                st.error(f"Failed to add fruit. Server returned status code {response.status_code}")

    if st.button("List All Fruits"):
            # Make a request to the server to get the list of all fruits
            list_url = "http://server:8000/list"
            list_response = requests.get(list_url)

            # Display the list of fruits
            if list_response.status_code == 200:
                fruits = list_response.json()
                st.info("List of all fruits:")
                st.write(fruits)
            else:
                st.error(f"Failed to retrieve the list of fruits. Server returned status code {list_response.status_code}")

if __name__ == "__main__":
    main()

