from collections import defaultdict

# User input for data
print("Enter the transaction data (separated by a single newline, each transaction consisting of 6 lines):")
input_data = input()

# Split user input data into transactions
transactions = input_data.split('\n')

# Dictionary to store customer-wise total amount
customer_totals = defaultdict(float)

# Process each transaction
for i in range(0, len(transactions), 6):  # Each transaction has 6 lines
    if i + 4 < len(transactions):  # Check if index exists for customer and amount
        customer = transactions[i + 3]  # Customer name is on the fourth line
        amount_str = transactions[i + 5].replace('฿', '').replace(',', '')  # Extract amount and remove currency symbol and commas
        amount = float(amount_str)

        # Update customer's total amount
        customer_totals[customer] += amount

# Print customer-wise total amounts
print("\nTotal amounts spent by each customer:")
for customer, total_amount in customer_totals.items():
    print(f"{customer}: ฿{total_amount:.2f}")
