# Source file for Contact class that is holding the user's information

class Contact:
    """
        A contact object used by Phonebook. Each contact has their own
        name, student number, contact number, and occupation. 
        
        The full contact number of a contact is a combination of its country code, area code,
        and contact number, IN ORDER.
    """
    COUNTRY_CODES = {
        60: "Federation of Malaysia", # Malaysia
        62: "Republic of Indonesia", # Indonesia
        63: "Republic of the Philippines", # Philippines
        65: "Republic of Singapore", # Singapore
        66: "Kingdom of Thailand", # Thailand
        84: "Socialist Republic of Vietnam", # Vietnam
        673: "Brunei Darussalam", # Brunei
        855: "Kingdom of Cambodia", # Cambodia
        856: "Lao People's Democratic Republic", # Burma
        95: "Republic of the Union of Myanmar", # Myanmar
        670: "Democratic Republic of Timor Leste" # Timor Leste
    }
    
    def __init__(self, stdn: str, fname: str, sname: str, occupation: str,
                    gender: str, cc: int, area: int, number: int):
        """
        Args:
            stdn (str): Student number
            fname (str): First name of the contact
            sname (str): Last name of the contact
            occupation (str): Contact's work title
            gender (str): Contact's gender
            cc (int): Contact's country code
            area (int): Contact's area code
            number (int): Contact's contact number
        """
        self.student_num = stdn
        self.fname = fname
        self.lname = sname 
        self.occupation = occupation
        self.gender = gender 
        self.cc = cc 
        self.area = area
        self.number = number 

    def getStudentNumber(self) -> str:
        """Get the contact's student number.

        Returns:
            str: String student number.
        """
        return self.student_num

    def getFName(self) -> str:
        """Get the contact's first name.

        Returns:
            str: First name.
        """
        return self.fname
    
    def getLName(self) -> str:
        """Get the contact's last name

        Returns:
            str: Last name.
        """
        return self.lname
    
    def getFullName(self) -> str:
        """Gets the full name of the contact, which is a concatenation 
        of its first name and last name.

        Returns:
            str: Full name of the contact.
        """
        return self.fname + " " + self.lname
    
    def getOccupation(self) -> str:
        """Get the contact's occupation or work.

        Returns:
            str: Occupation.
        """
        return self.occupation
    
    def getGender(self) -> str:
        """Get the contact's gender.

        Returns:
            str: Male or Female.
        """
        return self.gender
    
    def getPronoun(self) -> str:
        return "His" if self.getGender() == "M" else "Her"
    
    def getCountryCode(self) -> str:
        """Gets the string value of the contact's country code.
        This refers to the different countries and their respective 
        country codes

        Returns:
            str: The name of the country associated to that country code value.
        """
        return Contact.COUNTRY_CODES[self.getNumericCountryCode()]
    
    def getNumericCountryCode(self) -> int:
        """Get the numeric country code of this contact.

        Returns:
            int: Numeric country code.
        """
        return self.cc
    
    def getAreaCode(self) -> int:
        """Get numeric area code of this contact

        Returns:
            int: Numeric area code.
        """
        return self.area
    
    def getContactNumber(self) -> int:
        """Get the contact number of this contact.

        Returns:
            int: Contact number only.
        """
        return self.number

    def getFullContactNumber(self) -> str:
        """Get the full contact number of this contact.

        Returns:
            str: Full contact number, including numeric country code, 
            area code, and contact number.
        """
        return "{}-{}-{}".format(self.getNumericCountryCode(),
                                self.getAreaCode(),
                                self.getContactNumber())
    
    def get(self, attr: str) -> any:
        """
            Get the value of selected attribute for this object.

            Args:
                self (Contact): This object.
                attr (str): Attribute of this object to retrieve from.
        """
        # Optionally complete this method for up to 2 additional points in your MTE.
        return -1
        
    def setStudentNumber(self, new_stdn: str) -> None:
        """Sets a new student number of this contact.
        Args:
            new_stdn (str): New student number.
        """
        self.student_num = new_stdn
    
    def setFName(self, new_fname : str) -> None:
        """Sets a new new first name of this contact.

        Args:
            new_fname (str): New first name.
        """
        self.fname = new_fname
    
    def setLName(self, new_sname: str) -> None:
        """Sets a new last name of this contact.

        Args:
            new_sname (str): New last name.
        """
        self.lname = new_sname
        
    def setGender(self, new_gender: str) -> None:
        """Sets a new gender of this contact. Must be either M or F.
        Will return -1 if new gender value is invalid.
        Args:
            new_gender (str): _description_
        """
        if new_gender.capitalize() != "M" or new_gender.capitalize != "F":
            print("Sorry, that is an invalid value for gender.")
            return -1
        else: 
            self.gender = new_gender

    def setOccupation(self, new_occupation: str) -> None:
        """Sets a new occupation of this contact.

        Args:
            new_occupation (str): New occupation.
        """
        self.occupation = new_occupation

    def setCountryCode(self, new_country_code: int) -> None:
        """Sets a new country code for this contact. 
        New country code must exist in the current.
        Returns -1 if new country code is not successfully set.

        Args:
            new_country_code (int): New country code.
        """
        if not new_country_code in Contact.COUNTRY_CODES:
            print("Sorry, this country code does not exist. Try again.")
            return -1
        else: 
            self.cc = new_country_code
            
    def setAreaCode(self, new_area: int) -> None:
        """Sets a new area code for this contact.

        Args:
            new_area (int): New area code.
        """
        self.area = new_area
        
    def setContactNumber(self, new_number: int) -> None:
        """Sets new contact number for this contact.

        Args:
            new_number (int): New contact number.
        """
        self.number = new_number
        
    @staticmethod
    def compareNames(c1: 'Contact', c2: 'Contact', comparison_type: int = 0) -> int:
        """Compares the names of two different contacts. 
        
        Args:
            c1 (Contact): Contact 1
            c2 (Contact): Contact 2
            comparison_type (int): 0 to compare last names. 1 to compare first names. Defaults to 0.
 
        Returns:
            int: 1 if name value of c1 > c2.
            0 if both contacts have same name value.
            -1 if name value of c1 < c2.
        """
        # Complete this method
        return -1
    
    @staticmethod
    def compare(c1: 'Contact', c2: 'Contact', modifier: str) -> int:
        """
            Compares two contacts based on a comparison method.

        Args:
            c1 (Contact): Contact 1
            c2 (Contact): Contact 2
            modifier: Attribute to compare with one another with.

        Returns:
            int: 1 if c1 wins comparison over c2. 0 if both contact are equal in comparison. -1 if c1 loses comparison to c2.
        """
        # Optionally complete (and only utilize this method instead of the compareNames() method)
        # in comparing attribute values (used in completing another bonus part of the project)
        
        # Bonus points may receive up to 3 points in your MTE.
        return -1
        
    def __str__(self) -> str:
        """Returns a string representation of this contact."""
        return "{}, {}, with student number {}, is a/an {}. {} phone number is {}.".format(
            self.getLName(), self.getFName(), self.getStudentNumber(), self.getOccupation(),
            self.getPronoun(), self.getFullContactNumber()) 
