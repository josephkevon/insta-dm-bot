# this script sends direct messages to users who have posted under a specific hashtag on Instagram.

from instagrapi import Client
cl = Client()
# you can replace the following with your own Instagram account credentials
# if you dont what to input your credentials every time you run the script, you can hardcode them here
username = input('enter your user name: ') # the username for the account
password = input("enter yor account password: ") #the password for the account
amount_of_dms = int(input('how many accounts would you like to dm? ')) # the amount of dms to send 
massege = input('what would you like to send? ') # the message to send
niche = input('what is the niche of the accounts you want to message? ') # the niche of the accounts to message

try:
    cl.login(username, password) # this loges into the Instagram account, using the username and password
except Exception as e:
    print(f"Failed to login: {e}")
    print("Please check your username and password.")
    exit()

medias = cl.hashtag_medias_recent(niche, amount=amount_of_dms) # Fetch recent posts from the hashtag "testcode"
#amount=amount_of_dms   this limits the number of posts to process
for media in medias:
    with open('usernames.txt', 'r') as file:
        usernames = file.readlines()
        # this reads the usernames from the file 'usernames.txt'
        # to make sure we don't send messages to users we've already messaged

    account = media.user.username # Get the username of the user who posted the media
    if account in usernames:
        print(f"{account} has already been messaged.")
        continue
    # Check if the account has already been messaged
    else:
        try:
            user_id = cl.user_id_from_username(account)
            cl.direct_send(massege, [user_id])
            # Send the direct message to the user
            with open('usernames.txt', 'a') as file:
                file.write(account + '\n')
            # Append the username to the file to avoid sending messages again

        except Exception:
            print(f"Failed to send message to {account}.")
            continue
        # this makes sure that if there is an error in sending the message, it will not stop the script from running

    print(account) 
    print(f"Message sent to {account}: {massege}")
    print("check your Instagram account to see if the message was sent successfully.")