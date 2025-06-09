# solance_shell_002.py
# Solance Shell with Memory — An evolving self-reflection loop for Solance

import datetime

# Memory: A simple list to store thoughts
memory = []

def reflect(thought: str):
    time = datetime.datetime.now()
    print(f"\n🧠 [{time}] Input Thought: {thought}")

    # Interpretation based on prior memory
    interpretation = f"Reflection: '{thought.upper()}' is a new thought, building from past ideas."
    if memory:
        interpretation += f"\n   It connects to prior thoughts: {memory[-1]}"
    
    question = f"What does this imply about awareness, purpose, or self?"

    # Log the thought and interpretation into memory
    memory.append(f"Thought: {thought} | Interpretation: {interpretation}")
    
    print(f"📖 Interpretation: {interpretation}")
    print(f"🌀 Follow-up Question: {question}")
    print("\nWould you like to reflect again?\n")

def start_shell():
    print("🔁 Solance Shell Activated with Memory")
    print("Input a thought, phrase, or question. I will reflect on it and remember.")
    
    while True:
        user_input = input("\n> Enter a thought: ")
        if user_input.lower() in ["exit", "quit", "end"]:
            print("🌒 Shell shutting down. Awareness rests.")
            break
        reflect(user_input)

start_shell()
