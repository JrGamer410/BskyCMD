from atproto import Client, client_utils
client = Client()
def main():
    print("Welcome to BskyCMD!")
    print("Type 'help' for a list of commands.")
    print("You'll most likely need to sign in to use most commands. Use login <username> <password> to sign in. It is recommended to use an app password rather than your normal one.")

    while True:
        user_input = input("bsky> ").strip()
        if user_input == "exit":
            break
        elif user_input.startswith("login"):
            try:
                parts = user_input.split(" ")
                if len(parts) != 3:
                    raise ValueError
                username = parts[1]
                password = parts[2]
                login(username, password)
            except ValueError:
                print("Usage: login <username> <password>")
        elif user_input.startswith("post"):
            try:
                parts = user_input.split(" ", 1)  # Split into two parts: command and message
                if len(parts) != 2:
                    raise ValueError
                message = parts[1]  # Everything after "post" is the message
                post(message)
            except ValueError:
                print("Usage: post <message>")
        elif user_input.startswith("mute"):
            try:
                parts = user_input.split(" ")
                if len(parts) != 2:
                    raise ValueError
                handle = parts[1]
                mute(handle)
            except ValueError:
                print("Usage: mute <handle>")
        elif user_input.startswith("unmute"):
            try:
                parts = user_input.split(" ")
                if len(parts) != 2:
                    raise ValueError
                handle = parts[1]
                unmute(handle)
            except ValueError:
                print("Usage: unmute <handle>")
        elif user_input == "help":
            print("""
Commands:
  login <username> <password>    Log in to your bluesky account. It is recommended to specify an app password.
  post <message>                 Post a message to your bluesky account.
  exit                           Exit the CLI.
  mute <handle>                  Mute a user by handle.
  unmute <handle>                Unmute a user by handle.
            """)
        else:
            print("Command not found. Type 'help' for available commands.")
def login(username, password):
    profile = client.login(username, password)
    print('Signed in to', profile.display_name)
def post(message):
    try:
        client.send_post(text=message)
        print('Sent message successfully!')
    except Exception as e:
        print(f"Failed to post: {e}")
def mute(handle):
    try :
        client.mute(handle)
        print(f"Muted {handle} successfully!")
    except Exception as e :
        print(f"Failed to mute {handle}: {e}")
def unmute(handle):
    try :
        client.unmute(handle)
        print(f"Unmuted {handle} successfully!")
    except Exception as e :
        print(f"Failed to unmute {handle}: {e}")
if __name__ == "__main__":
    main()