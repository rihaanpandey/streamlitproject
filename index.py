import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a CSV file
def load_data():
    return pd.read_csv('blood.csv')

def main():
    st.markdown("<h1 style='text-align: center; color: #9B59B6;'>Select Name from Dataset</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<h2 style='color: #008080;'>Dataset</h2>", unsafe_allow_html=True)
    show_dataset = st.sidebar.checkbox("Show Dataset")
    df = None

    if show_dataset:
        # Load the dataset
        df = load_data()
        # Display the dataset in the sidebar
        st.sidebar.subheader("Loaded Data:")
        st.sidebar.write(df)

    selected_data = pd.DataFrame()
    selected_name = st.selectbox("Select your name:", df['Name'] if df is not None else [])
    submitted = st.button("Submit") 

    if submitted and df is not None:
        selected_data = df[(df['Name'] == selected_name)]
        st.write("Selected Data:")
        st.write(selected_data)

        # Visualizations
        st.subheader("Visualization")
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))  # Separate axes for each subplot

        # Plot histogram of Age
        ax1.hist(selected_data['Age'])
        ax1.set_xlabel('Age')
        ax1.set_ylabel('Frequency')
        ax1.set_title('Age Distribution')

        # Calculate percentage of people with and without Blood Group
        BloodGroup_counts = selected_data['Blood Group'].value_counts(normalize=True) * 100
        labels = BloodGroup_counts.index.tolist()
        sizes = BloodGroup_counts.values.tolist()

        # Plot pie chart for sugar status
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax2.set_title('Blood Group Status')

        st.pyplot(fig)

if __name__ == "__main__": 
    main()
