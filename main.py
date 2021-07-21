import wikipedia, random, webbrowser, os

# Open the file and read it
with open('titles', encoding="utf8") as f:
    lines = f.readlines()

# Initiate double while true loop, first for user input, second for generating a random title
while True:
    while True:
        # Get a random title from the file
        title = random.choice(lines)
        # See if the page can be found in wikipedia API
        try: 
            page = wikipedia.page(title)
        # If there was an error, find another page
        except Exception:
            continue

        # Tell the user what their page is
        print(f"\nYour randomly selected page is '{page.title}'.")
        
        # Fetch a summary from the API
        print("\nSummary:", wikipedia.summary(title, sentences=1), "\n")

        # Ask the user what they want to do
        answer = str(input("Open page, find another page, or exit program? (open/another/exit): "))
        
        # Make user's answer lowercase and remove whitespace
        answer = answer.lower().strip()

        # Tell user if their input is invalid
        if answer in ('open', 'another', 'exit'):
            break
        print("invalid input.")
    
    if answer == 'another':
        # Loop back and find another random page
        continue
    
    elif answer == 'open':
        # Open the wiki page in webbrowser and exit the program
        webbrowser.open(f"https://en.wikipedia.org/wiki/{title}")
        print(f"Opening https://en.wikipedia.org/wiki/{title}")
        break
    
    else:
        # Exit program
        print("Have a nice day!")
        break
