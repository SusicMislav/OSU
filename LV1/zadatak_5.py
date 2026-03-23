fhand = open("zadaci/SMSSpamCollection.txt")

HamWordCounter = 0
HamSMSCounter = 0
SpamWordCounter = 0
SpamSMSCounter = 0
SpamSMSwithEclamation = 0
for line in fhand :
    words = line.split()
    if words[0] == "ham":
        HamSMSCounter += 1
        for word in words[1::1]:
            HamWordCounter += 1
    if words[0] == "spam":
        SpamSMSCounter +=1
        for word in words[1::1]:
            SpamWordCounter += 1
        if words.pop() == "!":
            SpamSMSwithEclamation += 1

print("Average number of words in ham messages: ", HamWordCounter / HamSMSCounter)
print("Average number of words in spam messages: ", SpamWordCounter / SpamSMSCounter)

print("Number of messages that finish with an exclamation mark: ", SpamSMSwithEclamation)
