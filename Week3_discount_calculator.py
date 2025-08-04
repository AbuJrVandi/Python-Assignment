def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.
    
    Args:
        price (float): Original price of the item
        discount_percent (float): Discount percentage to apply (0-100)
        
    Returns:
        float: Final price after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
original_price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage (0-100): "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"\nOriginal Price: ${original_price:.2f}")
    print(f"Discount Applied: {discount_percent}%")
    print(f"Final Price after {discount_percent}% discount: ${final_price:.2f}")
else:
    print(f"\nNo discount applied. The price remains: ${original_price:.2f}")
