import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
min_number = pyip.inputInt('What is the min number?: ')
max_number = pyip.inputInt('What is the max number?: ')
for questionNumber in range(numberOfQuestions):
    # We will pick two random numbers
    num1 = random.randint(min_number, max_number)
    num2 = random.randint(min_number, max_number)

    prompt = '#%s: %s x %s = ' % (questionNumber+1, num1, num2)
    try:
        # Right answers are managed by allowRegexes
        # Wrong answers are managed by blockRegexes
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], 
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout = 8,
                      limit = 1)
    except pyip.TimeoutException:
        print('Out Of Time!')
        continue
    except pyip.RetryLimitException:
        continue
    else:
        print('Correct!')
        correctAnswers += 1
        time.sleep(1)
print('Score: %s / %s ' % (correctAnswers, numberOfQuestions), end='-> ')
accuracy = int((correctAnswers*100)/numberOfQuestions)
print(f'Estimated Accuracy: {accuracy}%')
