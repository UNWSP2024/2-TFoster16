# Timothy Foster, 1/29/25, Total Purchase Program

def calculate_total_purchase():

    # Get User Input.
    item1 = float(input('Enter the cost of the first item in dollars.'))
    item2 = float(input('Enter the cost of the second item in dollars.'))
    item3 = float(input('Enter the cost of the third item in dollars.'))
    item4 = float(input('Enter the cost of the fourth item in dollars.'))
    item5 = float(input('Enter the cost of the fifth item in dollars.'))

    # Calculate The Sale Subtotal By Addition, Round The Answer, and Print The Results.
    saleSubtotal = round(item1 + item2 + item3 + item4 + item5, 2)
    print('The sale subtotal is $', saleSubtotal, '.')

    # Calculate The Sale Tax By Percentage, Round The Answer, and Print The Results.
    salesTax = round(0.07 * saleSubtotal, 2)
    print('The sales tax is $', salesTax, '.')

    # Calculate The Sale Total By Addition and Print The Results. There Is No Reason To Round Because The Other Variables Are Already Rounded To Two Places.
    salesTotal = saleSubtotal + salesTax
    print('The sale total is $', salesTotal, '.')

calculate_total_purchase()
