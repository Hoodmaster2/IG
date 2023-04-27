from InstagramAPI import InstagramAPI
import time
import random

def follow_accounts_with_content(api, hashtag):
    api.search_hashtag(hashtag)
    results = api.LastJson['items'][:10]
    for result in results:
        account_id = str(result['user']['pk'])
        api.follow(account_id)
        time.sleep(10)

def comment_on_posts(api, hashtag, comment_text):
    api.search_hashtag(hashtag)
    results = api.LastJson['items'][:10]
    for result in results:
        media_id = str(result['pk'])
        api.comment(media_id, comment_text)
        time.sleep(random.randint(10, 30))

def like_posts(api, hashtag):
    api.search_hashtag(hashtag)
    results = api.LastJson['items'][:10]
    for result in results:
        media_id = str(result['pk'])
        api.like(media_id)
        time.sleep(random.randint(10, 30))

def unfollow_accounts(api):
    following = api.getTotalFollowings(api.username_id)
    for account in following:
        account_id = account['pk']
        api.unfollow(account_id)
        time.sleep(10)

def display_menu():
    print("What would you like to do?")
    print("1. Follow accounts with content")
    print("2. Comment on posts")
    print("3. Like posts")
    print("4. Unfollow accounts")

def run_bot(username, password):
    api = InstagramAPI(username, password)
    api.login()
    if api.LastResponse.status_code != 200:
        print(f"Request return {api.LastResponse.status_code} error!\n{api.LastJson['message']}")
        return
    while True:
        display_menu()
        option = input("Enter your choice (press q to quit): ")
        if option == "1":
            hashtag = input("Enter the hashtag to search for: ")
            follow_accounts_with_content(api, hashtag)
        elif option == "2":
            hashtag = input("Enter the hashtag to search for: ")
            comment_text = input("Enter your comment text: ")
            comment_on_posts(api, hashtag, comment_text)
        elif option == "3":
            hashtag = input("Enter the hashtag to search for: ")
            like_posts(api, hashtag)
        elif option == "4":
            unfollow_accounts(api)
        elif option == "q":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    print("Welcome to HoodMaster!")
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    run_bot(username, password)
