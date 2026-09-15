import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    """Load the e-commerce customer dataset from the CSV file."""
    file_path = "data/ecommerce_customers.csv"
    data = pd.read_csv(file_path)
    return data


def analyze_average_spending(data):
    """Calculate the average total spending for each customer segment."""
    spending = (
        data.groupby("customer_segment")
        ["total_spent_usd"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\nQuestion 1:")
    print("Which customer segment has the highest average total spending?")
    print("-" * 60)
    print(spending)

    highest_segment = spending.index[0]
    highest_average = spending.iloc[0]

    print(
        f"\nAnswer: {highest_segment} has the highest "
        f"average total spending of ${highest_average:,.2f}."
    )

    return spending

def analyze_customer_count(data):
    """Count the number of customers in each customer segment."""
    customer_counts = (
        data.groupby("customer_segment")["customer_id"]
        .count()
        .sort_values(ascending=False)
    )

    print("\nQuestion 2:")
    print("Which customer segment has the highest number of customers?")
    print("-" * 60)
    print(customer_counts)

    largest_segment = customer_counts.index[0]
    largest_count = customer_counts.iloc[0]

    print(
        f"\nAnswer: {largest_segment} has the highest number "
        f"of customers with {largest_count:,} customers."
    )

    return customer_counts

def show_customer_segments(data):
    """Display the number of customers in each customer segment."""
    segments = (
        data["customer_segment"]
        .value_counts()
        .sort_values(ascending=False)
    )

    print("\nCustomer Segments Summary")
    print("-" * 60)

    for segment, count in segments.items():
        print(f"{segment}: {count:,} customers")

    print(f"\nTotal customers analyzed: {len(data):,}")

def create_spending_chart(spending):
    """Create and save a bar chart of average spending by customer segment."""
    plt.figure(figsize=(10, 6))

    spending.plot(kind="bar")

    plt.title("Average Total Spending by Customer Segment")
    plt.xlabel("Customer Segment")
    plt.ylabel("Average Total Spending (USD)")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig("output/average_spending_by_segment.png")
    plt.show()

    print("\nGraph saved to:")
    print("output/average_spending_by_segment.png")

def main():
    """Run the e-commerce customer data analysis program."""
    data = load_data()

    print("E-Commerce Customer Data Analyzer")
    print("=" * 40)

    print(f"Number of customers: {len(data)}")
    print(f"Number of columns: {len(data.columns)}")

    spending = analyze_average_spending(data)
    analyze_customer_count(data)
    show_customer_segments(data)
    create_spending_chart(spending)
    


if __name__ == "__main__":
    main()