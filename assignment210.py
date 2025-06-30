
print("NAME: VAJRESH SHENOY ")
print("USN:1AY24AI034")
print("SECTION:M")
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.seconds = hour * 3600 + minute * 60 + second

    def __str__(self):
        minutes, seconds = divmod(self.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

    def increment(self, seconds):
        self.seconds += seconds
        return self  
    
    def is__after(self, other):
        return self.seconds > other.seconds

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(0, 0, self.seconds + other.seconds)
        else:
            return Time(0, 0, self.seconds + other)

def int__to__time(seconds):
    return Time(0, 0, seconds)

def main():
    start__time = Time(9, 45, 0)
    print(f"Start time: {start__time}")

    end__time = Time(start__time.seconds)  
    end__time.increment(1337)
    print(f"End time: {end__time}")
    print(f"Is end time after start time? {end__time.is__after(start__time)}")
    print(f"Start time + 1000 seconds: {start__time + 1000}")
    print(f"Start time + 1 hour: {start__time + 3600}")
    
main()
