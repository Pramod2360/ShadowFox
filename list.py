justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Original list:", justice_league)
print("Number of members:", len(justice_league))
justice_league.extend(["Batgirl", "Nightwing"])
print("\nAfter adding Batgirl and Nightwing:", justice_league)
if "Wonder Woman" in justice_league:
    justice_league.remove("Wonder Woman")
    justice_league.insert(0, "Wonder Woman")
print("\nAfter moving Wonder Woman to beginning:", justice_league)
if "Aquaman" in justice_league and "Flash" in justice_league:
    chosen = "Green Lantern" if "Green Lantern" in justice_league else "Superman"
    if chosen in justice_league:
        justice_league.remove(chosen)
    flash_idx = justice_league.index("Flash")
    justice_league.insert(flash_idx, chosen)
print("\nAfter separating Aquaman and Flash:", justice_league)
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\nAfter replacement with new team:", justice_league)
justice_league.sort()
print("\nAfter sorting alphabetically:", justice_league)
print("New leader (0th index):", justice_league[0])