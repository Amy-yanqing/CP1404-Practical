NAME_TO_COLOUR = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                  "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                  "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                  "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                  "aquamarine4": "#458b74", "azure1": "#f0ffff"}

colour_name = input("Enter colour name: ")
while colour_name != "":
    try:
        print(NAME_TO_COLOUR[colour_name])
    except KeyError:
        print("Invalid colour name ")
    colour_name = input("Enter colour name: ")
print("Empty colour name. Finish")
