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

    
    # find balance_due_customer
    balance_due_cust = payment - balance_due

    print(f"Balance Due Customer: {format(balance_due_cust, '.2f')}")

    money = {
        100: 'one Hundred dollar bill',
        50: 'fifty dollar bill',
        20: 'twenty dollar bill',
        10: 'ten dollar bill',
        5: 'five dollar bill',
        1: 'one dollar bill',
        .25: 'quarter',
        .1: 'dime',
        .05: 'nickel',
        .01: 'penny',
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


