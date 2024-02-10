n = int(input())
lines = []

transactions = []
for n in range(0, n):
    transaction = input().split(',')
    transactions.append(transaction)
# TODO: Split each line into individual transactions and append them to a transaction list
transactions = [line.split() for line in lines]
# TODO: Define a function to detect fraudulent transactions
def detect_frauds(transactions):
    suspicious_transactions = []

   # TODO: Iterate over each transaction
    for transaction in transactions:
        trans_id, value, threshold = transaction
        value = int(value)
        threshold = int(threshold)
        # TODO: Check if the transaction value exceeds the fraud threshold
        if value > threshold:
            suspicious_transactions.append(trans_id)

    return suspicious_transactions

# TODO: Print the suspicious transactions list
print('\n'.join(detect_frauds(transactions)))