import time
import random
from difflib import SequenceMatcher

sentences = [
    "Python is a powerful programming language",
    "Practice makes a person perfect",
    "Artificial intelligence is changing the world",
    "Programming improves logical thinking",
    "Learning Python is fun and interesting"
]


def calculate_accuracy(original, typed):
    return SequenceMatcher(
        None,
        original,
        typed
    ).ratio() * 100


def typing_test():
    sentence = random.choice(sentences)

    print("\n===== TYPING SPEED TEST =====")
    print("\nType the following sentence:\n")
    print(sentence)

    input("\nPress Enter when ready...")

    start_time = time.perf_counter()

    typed = input("\nStart Typing: ")

    end_time = time.perf_counter()

    time_taken = end_time - start_time

    if time_taken <= 0:
        print("Unable to calculate typing speed.")
        return

    minutes = time_taken / 60

    # Standard gross WPM approximation:
    # 5 typed characters = 1 word
    wpm = (len(typed) / 5) / minutes

    accuracy = calculate_accuracy(sentence, typed)

    print("\n===== YOUR RESULTS =====")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

    if accuracy >= 95:
        print("Excellent Accuracy!")

    elif accuracy >= 80:
        print("Good Job!")

    else:
        print("Keep Practicing!")


if __name__ == "__main__":
    typing_test()