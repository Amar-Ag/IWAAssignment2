"""
15. Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?
"""


class Bank:
    @staticmethod
    def get_account_no():
        return 'Account number : XXXXXX'

    @staticmethod
    def get_Pin_no():
        return 'Pin number for card : XXXXXX'


class Customer:
    def __init__(
            self,
            fullName,
            fatherName,
            motherName,
            grandFatherName,
            currentAddress,
            permanentAddress,
            contactNo,
            addressProof,
            supportingDocumentOne,
            supportingDocumentTwo,
            jobStatus,
            jobType,
            maritalStatus,
            accountType,
            balance
    ):
        self.fullName = fullName
        self.fatherName = fatherName
        self.motherName = motherName
        self.grandFatherName = grandFatherName
        self.currentAddress = currentAddress
        self.permanentAddress = permanentAddress
        self.contactNo = contactNo
        self.addressProof = addressProof
        self.supportingDocumentOne = supportingDocumentOne
        self.supportingDocumentTwo = supportingDocumentTwo
        self.jobStatus = jobStatus
        self.jobType = jobType
        self.maritalStatus = maritalStatus
        self.accountType = accountType
        self.balance = balance
        self.account_no = Bank.get_account_no()
        self.is_active = True
        self.pin = Bank.get_Pin_no()

    def balance_enquiry(self):
        return self.balance

    def deposit_money(self, depositAmount):
        self.balance += depositAmount
        return f'New balance: {self.balance}'

    def get_card_pin(self):
        return self.card_pin

    def set_card_pin(self, pin):
        self.pin = pin

    def withdraw_money(self, withdrawAmount):
        if withdrawAmount > self.balance:
            return 'Insufficient balance.'
        else:
            return f'Rs.{withdrawAmount} has been withdrawn from your account no. {Bank.get_account_no()}. New Balance: {self.balance}'



