
print("List of menu functions")
print("Press")
print("1 -> Phone book")
print("2 -> Message")
print("3 -> Chat")
print("4 -> Call register")
print("5 -> Tones")
print("6 -> Settings")
print("7 -> Call divert")
print("8 -> Games")
print("9 -> Calculator")
print("10 -> Reminders")
print("11 -> Clock")
print("12 -> Profiles")
print("13 -> SIM services")

nokia = int(input())

if nokia == 1:
    print("Phone book")
    print("For phone book")
    print("1 -> Search")
    print("2 -> Services Nos.")
    print("3 -> Add name")
    print("4 -> Erase")
    print("5 -> Edit")
    print("6 -> Assign tone")
    print("7 -> Send b'card")
    print("8 -> Options")
    print("9 -> Speed dial")
    print("10 -> Voice tags")

    typeOfView = int(input())
    if typeOfView == 1:
        print("Search")
    elif typeOfView == 2:
        print("Service Nos")
    elif typeOfView == 3:
        print("Add name")
    elif typeOfView == 4:
        print("Erase")
    elif typeOfView == 5:
        print("Edit")
    elif typeOfView == 6:
        print("Assign tone")
    elif typeOfView == 7:
        print("Send b'card")
    elif typeOfView == 8:
        print("Options")
        print("For Options")
        print("1-> Type of view")
        print("2 -> Memory status")
        options = int(input())
        if options == 1:
            print("Type of view")
        elif options == 2:
            print("Memory status")
elif nokia == 2:
    print("Message")
    print("For Message")
    print("1 -> Write messages")
    print("2 -> Inbox")
    print("3 -> Outbox")
    print("4 -> Picture message")
    print("5 -> Template")
    print("6 -> Smileys")
    print("7 -> Message settings")

    message = int(input())
    if message == 1:
        print("Write message")
    elif message == 2:
        print("Inbox")
    elif message == 3:
        print("Outbox")
    elif message == 4:
        print("Picture message")
    elif message == 5:
        print("Template")
    elif message == 6:
        print("Smileys")
    elif message == 7:
        print("Message settings")
        print("For settings:")
        print("1 -> Set 1")
        print("2 -> Common")
        settings = int(input())
        if settings == 1:
            print("Set 1")
            print("For set 1")
            print("1 -> Message centre number")
            print("2 -> Message sent as")
            print("3 -> Message validity")
            setInput = int(input())
            if setInput == 1:
                print("Message centre number")
            elif setInput == 2:
                print("Message sent as")
            elif setInput == 3:
                print("Message validity")
        elif settings == 2:
            print("Common")
            print("For common:")
            print("1 -> Delivery reports")
            print("2 -> Reply via same centre")
            print("3 -> Character support")
            common = int(input())
            if common == 1:
                print("Delivery Report")
            elif common == 2:
                print("Reply via same centre")
            elif common == 3:
                print("Character support")
elif nokia == 3:
    print("Chat")
elif nokia == 4:
    print("Call Register")
    print("For call register")
    print("1 -> Missed calls")
    print("2 -> Received calls")
    print("3 -> Dialled numbers")
    print("4 -> Erase recent call history")
    print("5 -> Show call duration")
    print("6 -> Show call cost")
    print("7 -> Call cost settings")
    print("8 -> Prepaid credit")

    showCallDuration = int(input())
    if showCallDuration == 1:
        print("Missed calls")
    elif showCallDuration == 2:
        print("Received calls")
    elif showCallDuration == 3:
        print("Dialled numbers")
    elif showCallDuration == 4:
        print("Erase recent call list")
    elif showCallDuration == 5:
        print("Show call duration")
        print("For call duration")
        print("1 -> Last call duration")
        print("2 -> All calls duration")
        print("3 -> Received call duration")
        print("4 -> Dialled calls duration")
        print("5 -> Clear timers")
        lastCallDuration = int(input())
        if lastCallDuration == 1:
            print("Last call duration")
        elif lastCallDuration == 2:
            print("All calls duration")
        elif lastCallDuration == 3:
            print("Received calls duration")
        elif lastCallDuration == 4:
            print("Dialled calls duration")
        elif lastCallDuration == 5:
            print("Clear timers")
    elif showCallDuration == 6:
        print("Show call cost")
        print("For show call cost")
        print("1 -> Last call cost")
        print("2 -> All calls cost")
        print("3 -> Clear counters")
        costSettings = int(input())
        if costSettings == 1:
            print("Last call cost")
        elif costSettings == 2:
            print("All call cost")
        elif costSettings == 3:
            print("Clear counters")
    elif showCallDuration == 7:
        print("Call cost settings")
        print("For call cost settings")
        print("1 -> Call cost limit")
        print("2 -> Show costs in")
        callSettings = int(input())
        if callSettings == 1:
            print("Call cost settings")
        elif callSettings == 2:
            print("Show costs in")
    elif showCallDuration == 8:
        print("Prepaid credit")
elif nokia == 5:
    print("Tones")
    print("For Tones")
    print("1 -> Ring Tone")
    print("2 -> Ring Volume")
    print("3 -> Incoming call alert")
    print("4 -> Composer")
    print("5 -> Message alert tone")
    print("6 -> Vibrate alert")
    print("7 -> Screen saver")

    ringingTone = int(input())
    if ringingTone == 1:
        print("Ring Tone")
    elif ringingTone == 2:
        print("Ring Volume")
    elif ringingTone == 3:
        print("Incoming call alert")
    elif ringingTone == 4:
        print("Composer")
    elif ringingTone == 5:
        print("Message alert tone")
    elif ringingTone == 6:
        print("Vibrate alert")
    elif ringingTone == 7:
        print("Screen saver")
elif nokia == 6:
    print("Setting")
    print("For settings")
    print("1 -> Call settings")
    print("2 -> Phone settings")
    print("3 -> Security settings")
    print("4 -> Restore factory settings")

    settings = int(input())
    if settings == 1:
        print("Call settings")
        print("For call settings")
        print("1 -> Automatic redial")
        print("2 -> Speed dialling")
        print("3 -> Call waiting options")
        print("4 -> Own number sending")
        print("5 -> Phone line in use")
        print("6 -> Automatic answer")

        autoRedial = int(input())
        if autoRedial == 1:
            print("Automatic redial")
        elif autoRedial == 2:
            print("Speed dialling")
        elif autoRedial == 3:
            print("Call waiting options")
        elif autoRedial == 4:
            print("Own number sending")
        elif autoRedial == 5:
            print("Phone line in use")
        elif autoRedial == 6:
            print("Automatic answer")
    elif settings == 2:
        print("Phone settings")
        print("For phone settings")
        print("1 -> Language")
        print("2 -> Cell info display")
        print("3 -> Welcome note")
        print("4 -> Network selection")
        print("5 -> Lights")
        print("6 -> Confirm SIM service actions")

        language = int(input())
        if language == 1:
            print("Language")
        elif language == 2:
            print("Cell info display")
        elif language == 3:
            print("Welcome note")
        elif language == 4:
            print("Network selection")
        elif language == 5:
            print("Lights")
        elif language == 6:
            print("Confirm SIM service actions")
    elif settings == 3:
        print("Security settings")
        print("For security settings")
        print("1 -> PIN code request")
        print("2 -> Call bearing service")
        print("3 -> Fixed dialling")
        print("4 -> Closed user group")
        print("5 -> Phone security")
        print("6 -> Change access codes")

        securitySettings = int(input())
        if securitySettings == 1:
            print("PIN code request")
        elif securitySettings == 2:
            print("Call bearing service")
        elif securitySettings == 3:
            print("Fixed dialling")
        elif securitySettings == 4:
            print("Closed user group")
        elif securitySettings == 5:
            print("Phone security")
        elif securitySettings == 6:
            print("Change access codes")
    elif settings == 4:
        print("Restore factory settings")
elif nokia == 7:
    print("Call divert")
elif nokia == 8:
    print("Games")
elif nokia == 9:
    print("Calculator")
elif nokia == 10:
    print("Reminder")
elif nokia == 11:
    print("Clock")
    print("For clock")
    print("1 -> Alarm clock")
    print("2 -> Clock settings")
    print("3 -> Date settings")
    print("4 -> Stopwatch")
    print("5 -> Countdown timer")
    print("6 -> Auto update of date and time")

    clock = int(input())
    if clock == 1:
        print("Alarm clock")
    elif clock == 2:
        print("Clock settings")
    elif clock == 3:
        print("Date settings")
    elif clock == 4:
        print("Stopwatch")
    elif clock == 5:
        print("Countdown timer")
    elif clock == 6:
        print("Auto update of date and time")
elif nokia == 12:
    print("Profiles")
elif nokia == 13:
    print("SIM services")
