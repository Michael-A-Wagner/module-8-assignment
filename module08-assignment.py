# Module 6 Assignment: Functions and Modular Programming
# TechRetail Sales Analysis System

# Welcome message
print("=" * 60)
print("TECHRETAIL SALES ANALYSIS SYSTEM")
print("=" * 60)

# Sample quarterly sales data 
# Format: [product_name, category, price, quantity_sold, employee_id]
sales_data = [
    ["Smartphone Pro", "Phones", 899.99, 15, "E101"],
    ["Laptop Ultra", "Computers", 1299.99, 10, "E105"],
    ["Wireless Earbuds", "Audio", 149.99, 30, "E101"],
    ["Smart Watch", "Wearables", 249.99, 12, "E102"],
    ["Gaming Console", "Gaming", 499.99, 8, "E103"],
    ["Bluetooth Speaker", "Audio", 79.99, 25, "E102"],
    ["Tablet Lite", "Computers", 399.99, 18, "E104"],
    ["Digital Camera", "Cameras", 599.99, 5, "E105"],
    ["VR Headset", "Gaming", 299.99, 7, "E103"],
    ["Fitness Tracker", "Wearables", 129.99, 22, "E104"],
    ["Smartphone Plus", "Phones", 699.99, 20, "E101"],
    ["Laptop Basic", "Computers", 899.99, 14, "E105"]
]

# Employee information
# Format: {employee_id: [name, commission_rate]}
employees = {
    "E101": ["Alex Johnson", 0.05],
    "E102": ["Sarah Williams", 0.045],
    "E103": ["James Brown", 0.04],
    "E104": ["Lisa Davis", 0.05],
    "E105": ["Michael Wilson", 0.055]
}

# TODO 1: Sales Analysis Functions
# 1.1 Create a function to calculate total sales revenue
# REQUIRED FUNCTION NAME: calculate_total_sales
def calculate_total_sales():
    """
    Calculates the total revenue from all sales.
    
    Returns:
        float: The total sales revenue.
    """
    # Your code here
    total_sales_revenue = 0 
    for data in sales_data:
        p, q = data[2],data[3]
        total_sales_revenue += p*q
    return total_sales_revenue
    pass

# 1.2 Create a function to calculate the total sales for a specific category
# REQUIRED FUNCTION NAME: calculate_category_sales
def calculate_category_sales(category):
    """
    Calculates the total revenue from sales in a specific product category.
    
    Args:
        category (str): The product category to calculate sales for.
        
    Returns:
        float: The total sales revenue for the specified category.
    """
    # Your code here
    total_category_sales = 0 
    for data in sales_data:
        p,q = data[2],data[3]
        c = data[1]
        if c == category:
            total_category_sales += p*q
    return total_category_sales    
    pass

# 1.3 Create a function to find the best-selling product
# REQUIRED FUNCTION NAME: find_best_selling_product
# Should return tuple: (product_name, total_revenue)
# Your function here
def find_best_selling_product():
    best = ("",0)
    for data in sales_data:
         p,q = data[2],data[3]
         product = data[0]
         revenue = p * q
         if revenue > best[1]:
             best = (product, revenue)
    return best
best = find_best_selling_product()

# TODO 2: Commission Calculation Functions
# 2.1 Create a function to calculate commission for a specific employee
# REQUIRED FUNCTION NAME: calculate_employee_commission
def calculate_employee_commission(employee_id):
    """
    Calculates the commission earned by a specific employee.
    
    Args:
        employee_id (str): The unique identifier of the employee.
        
    Returns:
        float: The commission amount earned.
    """
    # Your code here
    total_employee_revenue = 0
    for data in sales_data:
        if data[4] == employee_id:
            p,q = data[2],data[3]
            total_employee_revenue += p*q
    commission_rate = employees[employee_id][1]
    return round(total_employee_revenue * commission_rate,2)
    pass

# 2.2 Create a function to calculate total commission for all employees
# REQUIRED FUNCTION NAME: calculate_total_commission
# Should return float: total commission for all employees
# Your function here
def calculate_total_commission():
    total_commission = 0
    for emp in employees:
        total_commission += calculate_employee_commission(emp)
    return total_commission


# TODO 3: Report Generation Functions
# 3.1 Create a function to generate a sales summary report
# REQUIRED FUNCTION NAME: generate_sales_summary
def generate_sales_summary(include_categories=True):
    """
    Generates a formatted sales summary report.
    
    Args:
        include_categories (bool, optional): Whether to include category breakdown.
            Defaults to True.
        
    Returns:
        str: Formatted report string.
    """
    # Your code here
    report = ""
    report += "=== SALES SUMMARY REPORT ===\n"
    report +=f"Total Sales: ${calculate_total_sales():,.2f}\n\n"
    
    if include_categories:
        report += "=== Sales by Category ===\n"
        for category in ["Phones","Computers","Audio", "Wearables", "Gaming", "Cameras"]:
            revenue = calculate_category_sales(category)
            report += f"{category}: ${revenue:,.2f}\n"
        report += "\n"
    best = find_best_selling_product()
    report += f"Best-Selling Product: {best}\n"
    
    return report
    pass

# 3.2 Create a function to generate an employee performance report
# REQUIRED FUNCTION NAME: generate_employee_report
# Should return string with employee sales and commissions
# Your function here
def generate_employee_report():
    report = "=== EMPLOYEE PERFROMANCE REPORT ===\n"
    
    for emp_id, info in employees.items():
        name = info[0]
        commission = calculate_employee_commission(emp_id)
        
        revenue = 0
        for data in sales_data:
            if data[4] == emp_id:
                revenue += data[2]*data[3]
        report += f"\n{name} ({emp_id})\n"
        report += f"Total Sales: ${revenue:,.2f}\n"
        report += f"Commission Earned: ${commission:,.2f}\n"
    return report
# TODO 4: Utility Functions
# 4.1 Create a function to get all products in a specific category
# REQUIRED FUNCTION NAME: get_products_by_category
def get_products_by_category(category):
    """
    Returns all products belonging to a specific category.
    
    Args:
        category (str): The product category to filter by.
        
    Returns:
        list: List of products in the specified category.
    """
    # Your code here
    products = []
    for data in sales_data:
        if data[1] == category:
            products.append(data[0])
    return products
    pass
# 4.2 Create a function to calculate the average sale price
# REQUIRED FUNCTION NAME: calculate_average_sale_price
# Should return float: average sale price across all transactions
# Your function here
def calculate_average_sale_price():
    total_price = 0
    total_quantity = 0
    for data in sales_data:
        total_price += data[2] * data[3]
        total_quantity += data[3]
    return (total_price/total_quantity)


# Main program flow - function calls to demonstrate your system
# REQUIRED FUNCTION NAME: main
def main():
    print("\nTECHRETAIL QUARTERLY SALES ANALYSIS")
    print("-" * 40)
    
    # Calculate and display total sales
    print("\nTOTAL QUARTERLY SALES:")
    # Your function call here
    print(f"${calculate_total_sales():,.2f}")
    # Display category sales
    print("\nSALES BY CATEGORY:")
    categories = ["Phones", "Computers", "Audio", "Wearables", "Gaming", "Cameras"]
    # Your code to display sales for each category
    for cat in categories:
        print(f"{cat}: ${calculate_category_sales(cat):,.2f}")
    # Display best-selling product
    print("\nBEST-SELLING PRODUCT:")
    # Your function call here
    best = find_best_selling_product()
    print(best)
    # Display employee commissions
    print("\nEMPLOYEE COMMISSIONS:")
    # Your code to display commission for each employee
    for emp_id in employees:
        commission = calculate_employee_commission(emp_id)
        print(f"{employees[emp_id][0]}: ${commission:,.2f}")
    # Generate and display sales summary report
    print("\nQUARTERLY SALES SUMMARY REPORT:")
    # Your function call here
    print(generate_sales_summary())
    # Generate and display employee performance report
    print("\nEMPLOYEE PERFORMANCE REPORT:")
    # Your function call here
    print(generate_employee_report())
# Run the main program
if __name__ == "__main__":
    main()