
import datetime

print("--- Welcome to My Daily Advisor ---")


name = input("Enter your name: ")
mood = input("How is your mood today? (happy / sad / stressed / tired): ").strip().lower()
energy_level = int(input("Enter your energy level (1 to 10): "))

print("\nGenerating your report...")


if energy_level <= 2:
    print("⚠️ Warning: Your energy level is critically low! Please rest.")


if energy_level >= 5:
    energy_advice = "You have plenty of energy to tackle your goals today!"
else:
    energy_advice = "Your energy is a bit low. Don't overwork yourself today."


if mood == "happy":
    mood_advice = "Keep sharing that positive energy with others!"
elif mood == "sad":
    mood_advice = "It's okay to have down days. Be gentle with yourself and do something you love."
elif mood == "stressed":
    mood_advice = "Take a deep breath. Try breaking your tasks into smaller, manageable steps."
elif mood == "tired":
    mood_advice = "Make sure to grab a warm drink and take short breaks when needed."
else:
    mood_advice = "Whatever you are feeling, embrace it and make it a great day!"


current_time = datetime.datetime.now()

print("\n" + "="*40)
print(f" DAILY ADVISOR REPORT FOR {name.upper()} ")
print(f" Date & Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
print("="*40)
print(f"• Energy Status: {energy_advice}")
print(f"• Mood Advisor:  {mood_advice}")
print("="*40)