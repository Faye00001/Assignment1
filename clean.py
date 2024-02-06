import pandas as pd
import sys


def clean_data(input1, input2, output):
    # Step 1: Merge the two input data files based on the ID value
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')

    # Drop redundant column after merging
    merged_df.drop('id', axis=1, inplace=True)

    # Step 2: Drop rows with missing values
    merged_df.dropna(inplace=True)

    # Step 3: Drop rows if their job value contains 'insurance' or 'Insurance'
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

    # Step 4: Save the cleaned data
    merged_df.to_csv(output, index=False)


if __name__ == '__main__':
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Please provide 3 required arguments: input1, input2, and output.")
        sys.exit(1)

    # Get the arguments from the command line
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output = sys.argv[3]

    # Call the clean_data function
    clean_data(input1, input2, output)