# Array List implementation of Contacts
from Contact import Contact

class ContactList:
    """Contact List class that creates an array list of the phonebook.
    """

    def __init__(self, size: int = 50):
        """
            Create an array list of contacts with default storage size of 50.
        """
        self.phonebook = [None] * size
        self.size = 0

    def getSize(self):
        """
            Get the size of this contact list.
        """
        return self.size
    
    def first(self) -> Contact:
        """
            Get the first contact in this contact list.
            Returns none if the list is empty.
        """
        # Complete this Method
        if self.isEmpty():
            return None
        return self.phonebook[0]
    
    def getLast(self) -> Contact:
        """
            Get the last contact in this contact list.
            Returns none if the list is empty.
        """
        # Complete this Method
        
        if self.isEmpty():
            return None
        return self.phonebook[self.getSize() - 1]

    def getContactAtIndex(self, index: int) -> Contact:
        """Gets the contact at given index in the contact linked list.
        Returns None if index is not found in the list.

        Args:
            index (int): Index to get in the contact linked list.

        Returns:
            Contact: Contact at index.
        """
        # Complete this Method
        return 
    
    def getContact(self, student_num: str) -> Contact:
        """Gets the contact based on given student number. Will return None
        if contact is not found.

        Args:
            student_num (str): Student number to base search from.

        Returns:
            Contact: Contact information.
        """
        # Complete this Method
        
        for contact in self.phonebook:
            if contact == None:
                continue
            
            if contact.getStudentNumber() == student_num:
                return contact
            
        return None
    
    def getContactBySurname(self, surname: str) -> Contact:
        """Gets the contact based on surname. Will return None if contact is not found.
        """
        # Complete this Method
        
        matching_contacts = [contact for contact in self.phonebook if contact and contact.getLName() == surname]
        return matching_contacts
    
    def isEmpty(self) -> bool:
        """
            Checks if contact list has no contacts.
        """
        return self.getSize() == 0
    
    def incrSize(self) -> None:
        """
            Increase the size of this contact list.
        """
        # Complete this Method
        self.size += 1

    def decrSize(self) -> None:
        """
            Decrease the size of this contact list
        """
        self.size -= 1

    def __increasePhonebookSize(self) -> None:
        """
            Increases the size of this phonebook by two times.
        """
        # Complete this Method
        return 
    
    def insert(self, c : Contact):
        """Inserts new contact at index point.

        Args:
            c (Contact): Contact to be inserted.
        """
        # Complete this Method
        return 

    def __findIndexInsertion(self, c: Contact) -> int:
        """Finds the index to insert from based on contact's
        last name, and first name if both have the same first names.

        Args:
            c (Contact): Contact to compare and to be inserted.

        Returns:
            int: Node insertion point for new contact.
        """
        # Complete this Method
        return 
    
    def __adjustPhonebook(self, start: int, end = int, dir: str = "f") -> None:
        """
        Adjusts the arrangement of this phonebook from start to end.

        Args:
            index (int): Index for adjustment.
            dir (str): Direction of adjustment:
                "f" -> Forward indexing adjustment. For example, element at index 0 takes the value of the element at index 1.
                "b" -> Backward indexing adjustment. For example, elemet at index 1 takes the value of the element at index 0.
        """
        # Complete this Method
        return 
    
    def deleteContact(self, stdn: str) -> Contact:
        """Finds the contact based on their student number.
        Returns the deleted contact. Otherwise, returns -1 if not found.

        Args:
            stdn (str): Student number of contact to be deleted.

        Returns:
            Contact: Deleted contact, if found.
        """
        # Complete this Method
        for i in range(self.size):
            if self.phonebook[i] and self.phonebook[i].getStudentNumber() == stdn:
                deleted_contact = self.phonebook[i]
                self.__adjustPhonebook(i, self.size - 1, dir="f")
                self.phonebook[self.size - 1] = None
                self.decrSize()
                return deleted_contact
        return None
        
    def __sort(self, by: str) -> list:
        """
            Sorts the phonebook based on the contact's attribute value.
        
            Args:
                by (str): Attribute value to sort the phonebook from.
            
            Returns:
                list: A copy of this phonebook list sorted based on the attribute value given.
        """
        # Complete this method optionally
        # Correctly completing this method will reward up to 4 bonus points in your MTE.
        return -1
        
    def __str__(self, f = None, by: str = 'lname') -> str:
        """
        Prints every contact in this contact list.

        Args:
            f (list, optional): A list that filters which contact should
                be outputted in the list of country codes. Defaults to None.
            by (str): Condition whether to print contact on a particular order based from some attribute.
            Note, completing the bonus functionality from this argument is optional.

        Returns:
            str: Every contact in this contact list in a particular order.
        """
        # Complete this method
        s = "<----Phonebook---->"
        if not self.isEmpty():
            # Complete this method.
            # Optionally include viewing contacts in a particular order for up to 1 bonus point in your MTE.
            print("Not Empty")
        else:
            s += "\nThis phonebook is currently empty..."
        s += "\n<----End---->"
        return s