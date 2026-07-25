from src.database.database_connection import initialize_database
from src.reports.inventory_analysis import generate_inventory_report
from src.reports.sales_analysis import generate_sales_report
from src.reports.work_hours_analysis import generate_work_hours_report


def print_header():
    """Display the application heading."""

    print("=" * 60)
    print("      Operations Data Analysis System")
    print("=" * 60)


def print_footer():
    """Display the application completion message."""

    print("\n" + "=" * 60)
    print("Analysis Complete")
    print("=" * 60)


def main():
    """Initialize the database and generate all reports."""

    print_header()

    print("\nInitializing database...")
    initialize_database()

    print("\nGenerating inventory report...")
    generate_inventory_report()

    print("\nGenerating employee work-hours report...")
    generate_work_hours_report()

    print("\nGenerating sales performance report...")
    generate_sales_report()

    print_footer()


if __name__ == "__main__":
    main()