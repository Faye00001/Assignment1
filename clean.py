import pandas as pd

def clean_data(input1, input2, output):

    contact_data = pd.read_csv(input1)
    other_data = pd.read_csv(input2)


    merged_data = pd.merge(contact_data, other_data, left_on='respondent_id', right_on='id')
    merged_data.drop('id', axis=1, inplace=True)  # 删除冗余的id列


    merged_data.dropna(inplace=True)


    merged_data = merged_data[~merged_data['job'].str.contains('insurance|Insurance')]


    merged_data.to_csv(output, index=False)


    print("Output file shape:", merged_data.shape)

if __name__ == '__main__':
    import sys


    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output = sys.argv[3]


    clean_data(input1, input2, output)