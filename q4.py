def print_statistics(func):
    def wrapper(*args):
        fList=func(args[0])
       
       
        num_list = [int(num) for num in fList]
        count = len(num_list)
        total = sum(num_list)
        average = total / count
        maximum = max(num_list)
        print("Numbers read:", num_list)
        print("Count of numbers read:", count)
        print("Average of the numbers:", average)
        print("Maximum of the numbers:", maximum)
        
        return num_list
    
    return wrapper


def printStats(t):
    allLines=[]
    with open(t, 'r') as file:
        for line in file:
            lineReturn(line.split())

@print_statistics
def lineReturn(numList):
    return numList

line_of_numbers = printStats("test2.txt") 
print(line_of_numbers)

# Here in this answer i have used three functions. IN this printStats functions, we open and iterate 
# through the lines of the file and call the lineReturn function. This lineReturn function just returns
# the line again and calls the decorator for the line that is passed to it.
# This is done to achieve the functionality separately for each line. To avoid using a list of lines of the file
# i have used this approach
