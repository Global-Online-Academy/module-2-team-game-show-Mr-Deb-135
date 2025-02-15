# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING
import random

# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split,steal"),("split,split"),("steal,split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy: Start with a higher chance to split, then increase chances of steal based on the number of rounds played
# 
choicesmade = 0
y = 20
def hereticalharbingersstrat2(history):
    global choicesmade,y
    for i in history:
        (me,them) = i
        choicesmade += 1
    if choicesmade == 0:
        return "split"
    elif choicesmade >= 1:
        x = random.randint(1,y)
        if y > 4:
            if x <= (y * 0.7):
                return "steal"
            else: 
                return "split"
        else:
            return "steal"
    y -= 1  
print(hereticalharbingersstrat2(hist4))
# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 
