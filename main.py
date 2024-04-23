import os
from repeater_book_api import RepeaterBookAPI
from csv_exporter import CSVExporter
from sort_repeaters import SortRepeaters

def main():
    location = input("Enter Maidenhead locator (e.g., IO83vn): ").upper()
    api_key = os.environ.get('REPEATERBOOK_API_KEY')

    if not api_key:
        print("REPEATERBOOK_API_KEY environment variable not found.")
        exit(1)

    api = RepeaterBookAPI(api_key)
    repeaters = api.get_repeaters_by_location(location)

    if repeaters:
        sorter = SortRepeaters()
        sorted_repeaters = sorter.sort_repeaters_by_mode_and_distance(repeaters)
        for mode, repeaters in sorted_repeaters.items():
            print(f"Repeater mode: {mode}")
            for repeater, distance in repeaters:
                print(f"  {repeater['callsign']} - Distance: {distance} km")

        export_choice = input("Do you want to export to CHIRP (C), Icom (I), or Yaesu (Y)? ").strip().lower()
        if export_choice in ['c', 'i', 'y']:
            filename = input("Enter the filename to save the CSV (e.g., repeaters.csv): ").strip()
            CSVExporter.export(sorted_repeaters, filename, export_choice)
            print(f"Repeater data saved to {filename}")
        else:
            print("Invalid choice.")
            exit(1)

    else:
        print("Failed to retrieve repeaters.")

if __name__ == "__main__":
    main()
