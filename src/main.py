from database_connection import initialize_database
from inventory_analysis import generate_inventory_report
from work_hours_analysis import generate_work_hours_report
from sales_analysis import generate_sales_report


def print_header():
    print("=" * 60)
    print("      Bacchus Winery Operations Analysis System")
    print("=" * 60)


def print_footer():
    print("=" * 60)
    print("Analysis Complete")
    print("=" * 60)


def main():
    print_header()

    print("\nInitializing database...\n")
    initialize_database()

    print("\nGenerating Inventory Report...\n")
    generate_inventory_report()

    print("\nGenerating Employee Work Hours Report...\n")
    generate_work_hours_report()

    print("\nGenerating Sales Performance Report...\n")
    generate_sales_report()

    print_footer()


if __name__ == "__main__":
    main()