import pandas as pd

# Read train.csv and test.csv
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')



# Write to submission.csv (example: create an empty DataFrame and save)
#submission_df = pd.DataFrame()  # Replace with your submission data

# Do this only when submitting the data.
#submission_df.to_csv('submission.csv', index=False)

# Read from submission.csv
#submission_read = pd.read_csv('submission.csv')