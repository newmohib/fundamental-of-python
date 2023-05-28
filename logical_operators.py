
# Logical Operators

# if applicant has high income AND good credit Eligible for loan

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

# if applicant has high income OR good credit Eligible for loan

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

# if applicant has good credit AND doesn't have a criminal record Eligible for loan

has_criminal_record = True
has_good_credit = True

if has_good_credit and not  has_criminal_record:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")