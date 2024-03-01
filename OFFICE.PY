import pymongo

#database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mnc_db"]
office = db['country']

# Office class
class Office:
    # Class variable
    office_counter = 0

    # Initialize class with default values
    def __init__(self, name, address, city, state, zip_code):
        self.office_id = Office.generate_office_id()
        self.office_name = name
        self.office_address = address
        self.office_city = city
        self.office_state = state
        self.office_zip_code = zip_code
        self.data = {"_id":self.office_id,
                     "name":self.office_name,
                     "address":self.office_address,
                     "city":self.office_city,
                     "state":self.office_state,
                     "zip_code":self.office_zip_code}
        office.insert_one(self.data)

    # Generate unique office ID
    @classmethod
    def generate_office_id(cls):
        Office.office_counter += 1
        return Office.office_counter

    # Getter for office_id
    def get_office_id(self):
        return self.office_id

    # Getter for office_name
    def get_office_name(self):
        return self.office_name

    # Getter for office_address
    def get_office_address(self):
        return self.office_address

    # Getter for office_city
    def get_office_city(self):
        return self.office_city

    # Getter for office_state
    def get_office_state(self):
        return self.office_state

    # Getter for office_zip_code
    def get_office_zip_code(self):
        return self.office_zip_code


# Main function
def main():
    # Create an office
    office = Office("Head Office", "1234 Main St.", "Chicago", "IL", "60601")

    # Print the office details
    print(f"Office ID: {office.get_office_id()}")
    print(f"Name: {office.get_office_name()}")
    print(f"Address: {office.get_office_address()}")
    print(f"City: {office.get_office_city()}")
    print(f"State: {office.get_office_state()}")
    print(f"Zip Code: {office.get_office_zip_code()}")


if __name__ == "__main__":
    main()
