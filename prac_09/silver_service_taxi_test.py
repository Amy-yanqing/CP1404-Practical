"""
SilverServiceTaxi class tests
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

    # my_taxi = SilverServiceTaxi("Hummer", 200, 4)
    # my_taxi.drive(20)
    # print(my_taxi.get_fare())

main()
