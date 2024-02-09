import sys
import pandas as pd


def clean_data(input1, input2, output):
    # Read the input files
    contact_data = pd.read_csv(input1)
    other_data = pd.read_csv(input2)

    # Merge the data based on ID
    merged_data = pd.merge(contact_data, other_data, left_on='respondent_id', right_on='id')

    # Drop rows with missing values
    merged_data = merged_data.dropna()

    # Drop rows with job values containing 'insurance' or 'Insurance'
    merged_data = merged_data[~merged_data['job'].str.contains('insurance|Insurance')]

    # Remove redundant columns
    merged_data = merged_data.drop(columns=['id'])

    # Save the cleaned data to the output file
    merged_data.to_csv(output, index=False)


if __name__ == '__main__':
    # Get the input and output file paths from command line arguments
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output = sys.argv[3]

    # Call the clean_data function
    clean_data(input1, input2, output)