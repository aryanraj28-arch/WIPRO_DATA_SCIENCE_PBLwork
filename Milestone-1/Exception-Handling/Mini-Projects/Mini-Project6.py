**Mini-Project6
1)
import os

def analyze_purchase():
    # 1. Handle runtime file input and check existence
    file_name = input("Enter the file name: ").strip()
    
    # Append extension if not provided by user
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' could not be found. Please check the name and try again.")
        return
    except PermissionError:
        print(f"Error: Permission denied reading '{file_name}'.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while opening the file: {e}")
        return

    # Initialize counters and accumulators
    items_purchased = 0
    free_items = 0
    amount_to_pay = 0
    discount_given = 0

    # 2. Process file content line by line
    for line_num, line in enumerate(lines, start=1):
        cleaned_line = line.strip()
        
        # Skip empty lines
        if not cleaned_line:
            continue
            
        try:
            # Split item name and value/price by the last space
            parts = cleaned_line.rsplit(maxsplit=1)
            if len(parts) != 2:
                raise ValueError("Malformed line structure (expected 'Item Name Value')")
                
            key, value = parts[0], parts[1]

            # Check if it's the discount line
            if key.lower() == 'discount':
                discount_given = float(value)
                continue

            # Process regular or free items
            items_purchased += 1
            if value.lower() == 'free':
                free_items += 1
            else:
                amount_to_pay += float(value)

        except ValueError as ve:
            print(f"Warning: Skipping line {line_num} due to invalid data format ('{cleaned_line}'). Error: {ve}")
        except Exception as e:
            print(f"Warning: Unexpected error processing line {line_num}: {e}")

    # 3. Compute final metrics
    final_amount = amount_to_pay - discount_given
    if final_amount < 0:
        final_amount = 0  # Final payment shouldn't realistically be negative

    # 4. Display Sample Output matching format
    print("\n--- Output Results ---")
    print(f"No of items purchased: {items_purchased}")
    print(f"No of free items: {free_items}")
    print(f"Amount to pay: {amount_to_pay:g}")
    print(f"Discount given: {discount_given:g}")
    print(f"Final amount paid: {final_amount:g}")

if __name__ == "__main__":
    analyze_purchase()