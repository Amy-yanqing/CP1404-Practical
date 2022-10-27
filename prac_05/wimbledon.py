"""
Wimbledon data-reading, processing and displaying
"""
FILENAME = "wimbledon.csv"
champion_to_count = {}
country_to_count = {}
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    get_champion_country_records()
    display_records()


def get_champion_country_records():
    """Create dictionary of champions and countries"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.split(",")[INDEX_CHAMPION]
            if parts in champion_to_count:
                champion_to_count[parts] += 1
                # champion_to_count[parts] = champion_to_count.get(parts, 0) + 1
            else:
                champion_to_count[parts] = 1
            country = line.split(",")[INDEX_COUNTRY]
            country_to_count[country] = country_to_count.get(country, 0) + 1


def display_records():
    """Display champions and countries"""
    print("Wimbledon Champions")
    for champion, count in champion_to_count.items():
        print(champion, count)
    print(f"These {len(country_to_count.keys())} countries have won Wimbledon")
    print(",".join(sorted(country_to_count.keys())))


main()
