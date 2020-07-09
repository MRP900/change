# an algorith to return change in the form of coins and bills

def make_change(balance_due, payment):
    """Takes a bill and customer payment and returns a dictionary of cash denominations 
       to return to the customer
    
    Arguments:
        balance_due {[float]} -- [a bill to be paid]
        payment {[float]} -- [amount of cash used by customer to pay bill]
    
    Returns:
        [dictionary] -- [keys = denominations, values = quantity of denominations]
    """

    # convert to non decimal
    balance_due = 100 * (balance_due)
    payment = 100 * (payment)
    
    
    # find balance_due_customer
    balance_due_cust = payment - balance_due

    print(f"Balance Due Customer: {(balance_due_cust / 100)}")

    # keys = denominations in pennies
    money = {
        10000: 'one Hundred dollar bill',
        5000: 'fifty dollar bill',
        2000: 'twenty dollar bill',
        1000: 'ten dollar bill',
        500: 'five dollar bill',
        100: 'one dollar bill',
        25: 'quarter',
        10: 'dime',
        5: 'nickel',
        1: 'penny',
    }

    change_due = {}

    for k, v in money.items():
        if k <= balance_due_cust:
            quant = balance_due_cust / k
            balance_due_cust = balance_due_cust % k
            print(f"{balance_due_cust}")
            change_due[v] = int(quant)

    return change_due



if __name__ == "__main__":
    print("\n1:")
    change = make_change(24.99, 50)
    print(change)

    print("\n2:")
    change = make_change(27.31, 100)
    print(change)

    print("\n3:")
    change = make_change(321, 500)
    print(change)

    print("\n4:")
    change = make_change(500, 5000)
    print(change)

    print("\n5:")
    change = make_change(.95, 1)
    print(change)

    print("\n6:")
    change = make_change(.01, 1)
    print(change)

    print("\n7:")
    change = make_change(.99, 1)
    print(change)
    
    print("\n8:")
    change = make_change(1.45, 1.50)
    print(change)

    print("\n9:")
    print(make_change(175, 300))


