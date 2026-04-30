import webbrowser
import os

print("hey there my name is jarvis your assistant how can i help you?")
print("1. open google")
print("2. open youtube")
print("3. open chrome")
print("4. open youtube music")
print("5. open coursera")
print("6. shut down the pc")
print("7. open github")
print("8. open spotify")
print("9. search in google")
print("10. open discord")

while True:
    query = input("enter your query: ").lower().strip()

    print("You typed:", query)   # debug line (you can remove later)

    if "google" in query:
        webbrowser.open("https://www.google.com")

    elif "youtube" in query:
        webbrowser.open("https://www.youtube.com")

    elif "chrome" in query:
        webbrowser.open("https://www.google.com")

    elif "discord" in query:
        webbrowser.open("https://www.discord.com")

    elif "search" in query:
        search_query = query.replace("search", "").strip()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
            print("Please provide a search query after 'search'.")

    elif "youtube music" in query:
        webbrowser.open("https://music.youtube.com")

    elif "coursera" in query:
        webbrowser.open("https://www.coursera.org")

    elif "shut down" in query:
        print("shutting down the pc...")
        # os.system("shutdown /s /t 1")  # ⚠️ enable carefully

    elif "github" in query:
        webbrowser.open("https://www.github.com")

    elif "settings" in query:
        os.system("start ms-settings:")

    elif "email" in query:
        webbrowser.open("https://mail.google.com")

    elif "calendar" in query:
        webbrowser.open("https://calendar.google.com")

    elif "spotify" in query:
        print("Opening Spotify...")
        webbrowser.open_new("https://open.spotify.com")

    elif "folder" in query:
        os.startfile("C:\\Users\\YourUsername\\Documents")  # change username

    elif "exit" in query:
        print("bye boss 😎")
        break

    else:
        print("sorry i can't understand your query please try again")