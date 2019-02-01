#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# This is a class that can be used by companies to create, update, and maintain a company rosterself.
# Work in progress.
# By Nicholas Coletta, in the year 2019.
# www.github.com/statusquonjc46 for plenty of other python things that may or may not be useful to you. Also my IT490 full stack project lol.

# Company object, that instantiates with company name, company address, company type, company website, and telephone number.


class Company(object):

    def __init__(self, compName, compAddress, compType, compWebsite, compTele):
        self.compName = compName
        self.compAddress = compAddress
        self.compType = compType                # initialization of Company object variables.
        self.compWebsite = compWebsite
        self.compTele = compTele

    def __repr__(self):     # Visual representation of how to instantiate this object.
        return 'Company(%s, %s, %s, %s, %s)' % (self.compName, self.compAddress, self.compType, self.compWebsite, self.compTele)

    def __str__(self):  # Output of what this object contains. Human readable.
        return 'Company: %s\nAddress: %s\nField: %s\nWebsite: %s\nTelephone: %s\n' % (self.compName, self.compAddress, self.compType, self.compWebsite, self.compTele)

# Subclass of Company, used to enter the amount of employees in each position.


class PersonnelCount(Company):
    totalEmployee = 0

    def __init__(self, ceo, executive, manager, staff):
        self.ceo = ceo
        self.executive = executive
        self.manager = manager      # initialization of PersonnelCount object variables.
        self.staff = staff

    # Visual representation of how to instantiate this object, positions are in [].
    def __repr__(self):
        return 'PersonnelCount([ceo]:%d, [exec]:%d, [manager]:%d, [staff]:%d)' % (self.ceo, self.executive, self.manager, self.staff)

    def __str__(self):      # Output of what this object contains, human readable.
        return '\nCompany Personnel:\n-CEO: %d\n-Executive: %d\n-Staff Members: %d\n' % (self.ceo, self.executive, self.staff)

    def numOfCEO(self):     # returns the value given to the instantiated class variable for CEO.
        return (self.ceo)

    # returns the value given to the instantiated class variable for Executive.
    def numOfExecutive(self):
        return (self.executive)

    # returns the total number of employees for the given instantiated company.
    def numOfEmployee(self):
        PersonnelCount.totalEmployee = self.numOfCEO() + self.numOfManger() + \
            self.numOfExecutive() + self.numOfStaff()
        return (PersonnelCount.totalEmployee)

    # returns the value given to the instantiated class variable for Manager.
    def numOfManger(self):
        return (self.manager)

    # returns the value given to the instantiated class variable for Staff.
    def numOfStaff(self):
        return (self.staff)

# Subclass of PersonnelCount, which subclasses Company. Used for company finances on salaried employees(all).


class PersonnelSalary(PersonnelCount):
    totalSalary = 0

    def __init__(self, ceoSal, execSal, mgrSal, staffSal):
        self.ceoSal = ceoSal
        self.execSal = execSal      # initialization of Personnel Salary object variables.
        self.mgrSal = mgrSal
        self.staffSal = staffSal

    def __repr__(self):     # Visual representation of how to instantiate this object.
        return 'PersonnelSalary(%d, %d, %d, %d)' % (self.ceoSal, self.execSal, self. mgrSal, self. staffSal)

    def __str__(self):      # Output of what this object contains. Human readable.
        return 'Salaries by position are as follows:\n-CEO: %d\n-Executives: %d\n-Mangers: %d\n-Staff Members: %d\n' % (self.ceoSal, self.execSal, self.mgrSal, self.staffSal)

    # returns the value given to the instantiated class variable for CEO Salary.
    def getCeoSalary(self):
        return (self.ceoSal)

    # returns the value given to the instantiated class variable for Executive Salary.
    def getExecSalary(self):
        return (self.execSal)

    # returns the value given to the instantiated class variable for Manager Salary.
    def getManagerSalary(self):
        return (self.mgrSal)

    # returns the value given to the instantiated class variable for Staff Salary.
    def getStaffSalary(self):
        return (self.staffSal)

    def getTotalSal(self):      # returns the total value of all salaries added together.
        PersonnelSalary.totalSalary = self.getCeoSalary() + self.getExecSalary() + \
            self.getManagerSalary() + self.getStaffSalary()
        return (PersonnelSalary.totalSalary)

# Employee class, subclass of everything above. Used to add, remove, update, and manipulate all things employees.


class Employee(PersonnelCount):
    pass

# Sub to all above, CEO Object, containts CEO specific methods. May be redundant, not sure yet.


class CEO(PersonnelSalary):
    ceoList = []        # Store all CEOs in here.

    def __init__(self, founderOne, founderTwo=None, founderThree=None):
        self.founderOne = founderOne
        CEO.ceoList.append(self.founderOne)
        if founderTwo is None:      # Checks if there are more than 1 CEO.
            self.founderTwo = 'NULL'
        else:
            self.founderTwo = founderTwo
            CEO.ceoList.append(self.foundTwo)
        if founderThree is None:        # Checks to see if there is more than 2 CEOs.
            self.founderThree = 'NULL'
        else:
            self.founderThree = founderThree
            CEO.ceoList.append(self.founderThree)

    def __repr__(self):     # Visual representation of how to instantiate this objecct.
        if self.founderTwo == 'NULL':
            return 'CEO(%s)' % (self.founderOne)
        elif self.founderThree == 'NULL':
            return 'CEO(%s, %s)' % (self.founderOne, self.founderTwo)
        else:
            return 'CEO(%s, %s, %s)' % (self.founderOne, self.founderTwo, self.founderThree)

    def __str__(self):      # Output of what is contained in this object. Human readable.
        if self.founderTwo == 'NULL':
            return 'Our CEO and Founder is: %s' % (self.founderOne)
        elif self.founderThree == 'NULL':
            return 'Our two CEO\'s and Founders are: %s and %s' % (self.founderOne, self.founderTwo)
        else:
            return 'Our three CEO\'s and Founders are: %s, %s, and %s' % (self.founderOne, self. founderTwo, self.founderThree)

    def payType():      # returns the pay type.
        return 'Salary'

    def POC():      # returns the point of contact, 1 level below self.
        return 'Executives'

    def roles():    # returns the roles that the CEO has.
        return 'Business Administration. Business Future. Direction.'

    def salary(self, other):        # gets the salary from PersonnelSalary, and returns it.
        return (other.getCeoSalary())

    def getCEOList(self):       # gets the list of CEOs and returns it.
        return (CEO.ceoList)


channel = Company('CMP', 'Manasquan', 'Business Development',
                  'www.ChannelMethodsPartners.com', '000-000-000')
channelPersonnel = PersonnelCount(1, 2, 3, 4)
channelSal = PersonnelSalary(200000, 120000, 90000, 50000)
channelCEO = CEO('brian')

# print(repr(channelPersonnel))
# print(str(channelPersonnel))
print(channelCEO.salary(channelSal))
print(channelSal.getTotalSal())
