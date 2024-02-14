data ={
    'Kotak Mahindra Bank':3.5,
    'State Bank Of India':2.5,
    'HDFC Bank':4.5,
    'IDFC Bank':2.0,
    'Canara Bank':4.5
}


def calculate_interest_bank(principal, time, bankName):
    """
    Calculate the compound interest.

    :param principal: The initial loan amount (P)
    :param rate: The annual interest rate as a percentage (r)
    :param time: The time in years the money is invested or borrowed for (t)
    :param compound_frequency: The number of times interest is compounded per year (n)
    :return: The compound interest earned or paid over the time period
    """
    # Convert annual rate from percentage to decimal
    compound_frequency=1
    rate = data[bankName]
    rate /= 100

    # Calculate the amount after the specified time
    amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)

    # Calculate the compound interest
    compound_interest = amount - principal

    return round(compound_interest,3)
    