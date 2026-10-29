import numpy as np


file = open("Loan_prediction_dataset.csv", "r")


loan_amounts = np.genfromtxt(file, delimiter=",", skip_header=1, usecols=8)


file.close()


clean_loan_amounts = loan_amounts[~np.isnan(loan_amounts)]


mean_loan = np.mean(clean_loan_amounts)
median_loan = np.median(clean_loan_amounts)
std_loan = np.std(clean_loan_amounts)


print("--- Loan Amount Statistical Analysis ---")
print(f"Total Records: {len(loan_amounts)}")
print(f"Valid Records (non-missing): {len(clean_loan_amounts)}")
print(f"Missing Values (NaN): {np.isnan(loan_amounts).sum()}")
print("-" * 40)
print(f"Mean Loan Amount: {mean_loan:.2f}")
print(f"Median Loan Amount: {median_loan:.2f}")
print(f"Standard Deviation: {std_loan:.2f}")

