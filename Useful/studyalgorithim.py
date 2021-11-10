#algorithm to find out what I will study today
subjects = ["Math","English","History","CS","Economics","Biology","Physics","Chemistry"]
hard_subjects = ["History", "Physics", "Chemistry", "CS"]
easy_subjects = ["Math", "English", "Economics", "Biology"]
####
good_moods = ["productive", "jittery", "mysterious","happy"]
bad_moods = ["bored", "tired", "neutral", "angry", "ok"]
current_mood = input("How are you feeling today?:")
if current_mood in good_moods:
    print("you should study", hard_subjects)
elif current_mood in bad_moods:
    print("you should study", easy_subjects)
