#commission_rate_p = 0.0
#commission_rate_s


commission_rate_p = float(input("Enter commission rate percentage (ex 0.03) on stock purchase: "))
commission_rate_s = float(input("Enter commission rate percentage (ex 0.03) on stock sale: "))
num_shares_p = float(input('Enter number of shares purchased: '))
num_shares_s = float(input('Enter number of shares sold: '))
purchase_price = float(input('Enter purchase price per share: '))
sell_price = float(input('Enter sell price per share: '))


amountPaidForStock = 0
purchaseCommission = 0
totalPaid = 0
stockSoldFor = 0
sellingCommission = 0
totalReceived = 0
profitOrLoss = 0

amountPaidForStock = num_shares_p * purchase_price
purchaseCommission = commission_rate_p * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = num_shares_s * sell_price
sellingCommission = commission_rate_s *stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid



print('Amount paid for stock: $', amountPaidForStock)
print('Commission paid on the purchase: $', purchaseCommission)
print('Amount the stock sold for: $', stockSoldFor)
print('Commission paid on the sale: $', sellingCommission)
print(' Profit (or loss if negative): $', profitOrLoss)


#print(commission_rate_p)
