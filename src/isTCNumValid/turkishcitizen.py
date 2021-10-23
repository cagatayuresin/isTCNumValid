#!/usr/bin python3
"""
A module can say a TCNum is valid or not according to offical TCNum algorithm.
This statue cannot say someone has this TCNum or anything about a TCNum's owners info.
Just valid or not.

Cagatay URESIN
cagatayuresin@gmail.com
"""
class trcitizennum:
    """
    It takes a TCNum as an object and checks if it is valid or not.
    tcnum = turkishcitezn.trcitizennum(num)
    tcnum.isvalid -> bool
    """
    def __init__(self, tcnum):
        self.tcnum = str(tcnum)

    def isvalid(self):
        """
        Returns True or False if the Turkish Citizen Number is valid or not.
        """
        # A tcnum cannot start with - or 0
        if self.tcnum.startswith("-") or self.tcnum.startswith("0"):
            return False

        # tcnum has to be 11-digits and numeric 
        if len(self.tcnum) != 11 or not self.tcnum.isnumeric():
            return False

        # The Algorithm
        oddsum = 0
        evensum = 0
        for i in range(0,9):
            if i%2 == 1:
                evensum += int(self.tcnum[i])
            else:
                oddsum += int(self.tcnum[i])
                
        if not (7*oddsum+9*evensum)%10 == int(self.tcnum[9]):
            return False
        else:
            digitsum = 0
            for digit in self.tcnum[:10]:
                digitsum += int(digit)
            if not digitsum%10 == int(self.tcnum[10]):
                return False
            elif not (oddsum*8)%10 == int(self.tcnum[10]):
                return False
            else:
                return True

        