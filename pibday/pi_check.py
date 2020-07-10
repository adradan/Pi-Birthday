class Pi:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year
        self.bday = None
        self.str_bday = None

    def set_bday(self):
        self.bday = f'{self.month}{self.day}{self.year}'

    def set_string(self):
        self.str_bday = f'{self.month}/{self.day}/{self.year}'

    def check_pi(self):
        check = False
        with open('pi_million.txt', 'r') as pi:
            line = (line.strip() for line in pi)
            for nums in line:
                if self.bday in nums:
                    check = True
                    break
        return check
