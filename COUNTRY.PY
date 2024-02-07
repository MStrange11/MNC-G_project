from OFFICE import Office 

# Country class
class Country:
    # Class variable
    country_counter = 0

    # Initialize class with default values
    def __init__(self, name, iso_code, currency_code):
        self.country_id = Country.generate_country_id()
        self.country_name = name
        self.country_iso_code = iso_code
        self.country_currency_code = currency_code
        self.office_list = []

    # Generate unique country ID
    @classmethod
    def generate_country_id(cls):
        Country.country_counter += 1
        return Country.country_counter

    # Getter for country_id
    def get_country_id(self):
        return self.country_id

    # Getter for country_name
    def get_country_name(self):
        return self.country_name

    # Getter for country_iso_code
    def get_country_iso_code(self):
        return self.country_iso_code

    # Getter for country_currency_code
    def get_country_currency_code(self):
        return self.country_currency_code
    
    # Setter for country_currency_code
    def add_office(self, off):
        self.office_list.append(off)
        print(off.office_name,'office added at',self.country_name)

    def show_office(self):
        if not self.office_list:
            print('no Office')
            return
        for off in self.office_list:
            print(off.office_name)

    def get_offices(self):
        return None if not self.office_list  else self.office_list


# Main function
def main():
    # Create a country
    country = Country("United States", "US", "USD")

    # Print the country details
    print(f"Country ID: {country.get_country_id()}")
    print(f"Name: {country.get_country_name()}")
    print(f"ISO Code: {country.get_country_iso_code()}")
    print(f"Currency Code: {country.get_country_currency_code()}")

    office = Office("Head Office", "1234 Main St.", "Chicago", "IL", "60601")
    country.add_office(office)
    country.show_office()


if __name__ == "__main__":
    main()