import random
rolls = [random.randint(1,6) for _ in range(20)]
count_6 = sum(1 for r in rolls if r==6)
count_1 = sum(1 for r in rolls if r==1)
two_6_in_row = sum(1 for i in range(len(rolls)-1) if rolls[i]==6 and rolls[i+1]==6)
print("Rolls:", rolls)
print("Number of 6s:", count_6)
print("Number of 1s:", count_1)
print("Number of times two 6s in a row:", two_6_in_row)
def jumping_jacks_session():
    total = 100
    per_set = 10
    completed = 0
    sets = total // per_set
    for s in range(1, sets+1):
        completed += per_set
        print(f"Completed {completed} jumping jacks.")
        ans = input("Are you tired? (y/n): ").strip().lower()
        if ans in ('y','yes'):
            skip = input("Do you want to skip remaining sets? (y/n): ").strip().lower()
            if skip in ('y','yes'):
                print(f"You completed a total of {completed} jumping jacks.")
                return
        else:
            print(f"{total - completed} jumping jacks remaining.")
    print("Congratulations! You completed the workout.")

if __name__ == '__main__':
    print("\nTo run the interactive jumping jacks session, run this file and follow prompts.")
