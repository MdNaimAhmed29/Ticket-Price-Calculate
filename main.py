def calculate_ticket_price(age, showtime):

    if age <= 10:
        ticket_price = 300
    elif 11 <= age <= 25:
        ticket_price = 500
    elif 26 <= age <= 60:
        ticket_price = 800
    elif age > 60:
        ticket_price = 400
    else:
        return None


    discount = 0
    if showtime < 1700:
        discount = ticket_price * 0.10

    discounted_price = ticket_price - discount

    return ticket_price, discount, discounted_price



try:
    age = int(input("Age: "))
    if age < 0:
        raise ValueError("Age must be a positive integer.")

    showtime = int(input("Showtime (HHMM): "))
    if showtime < 0 or showtime >= 2400 or showtime % 100 >= 60:
        raise ValueError("Please provide the showtime in the correct format.")


    ticket_price, discount, discounted_price = calculate_ticket_price(age, showtime)


    print(f"Ticket price: {ticket_price} BDT")
    print(f"Discount: {discount:.2f} BDT")
    print(f"Discounted price: {discounted_price:.2f} BDT")

except ValueError as e:
    print(f"Invalid input. {e}")