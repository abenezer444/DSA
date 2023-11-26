class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        transactions_map = defaultdict(list)

        for transaction in transactions:
            name, time, cost, country = transaction.split(',')
            if int(cost) > 1000:
                invalid.append(transaction)
            transactions_map[name].append([time,cost,country])
     
        for name in transactions_map:

            for transaction in transactions_map[name]:
                time1, cost1, country1 = transaction
                for transaction2 in transactions_map[name]:
                    time2, cost2, country2 = transaction2
                    if transaction != transaction2:
                        
                        if abs(int(time1) - int(time2)) <= 60 and country1 != country2 and int(cost1)<=1000:
                            invalid.append(name+','+ ','.join(transaction))
                            break
        return invalid




        