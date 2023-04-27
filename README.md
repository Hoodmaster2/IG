# IG aka HOODMASTER

HoodMaster is a tool designed to automate certain actions on Instagram, such as following accounts, commenting on posts, liking posts, and unfollowing accounts. It uses the InstagramAPI library to access Instagram's API and perform these actions on behalf of the user.

The tool starts by prompting the user for their Instagram username, password, and the hashtag to be used in the search for posts. Once the user is logged in, they are presented with a menu offering four options: following accounts with content, commenting on posts, liking posts, and unfollowing accounts.

If the user selects the option to follow accounts with content, the tool searches for posts using the hashtag provided by the user and then follows the accounts of the users who posted those posts. The tool will follow up to 10 accounts.

If the user selects the option to comment on posts, the tool searches for posts using the hashtag provided by the user and then adds a comment to up to 10 of the most recent posts.

If the user selects the option to like posts, the tool searches for posts using the hashtag provided by the user and then likes up to 10 of the most recent posts.

If the user selects the option to unfollow accounts, the tool unfollows all accounts that the user is currently following.

The tool uses time delays between actions to avoid Instagram's API rate limits and to appear more human-like. Additionally, the tool provides a level of obfuscation to the source code to make it more difficult for someone to copy and reuse the code.

To install HoodMaster on Termux, follow these steps:

Install Termux on your Android device from the Google Play Store.
Open Termux and update the package manager by typing apt update and pressing Enter.
Install Python by typing apt install python and pressing Enter.
Install pip, the Python package manager, by typing apt install python-pip and pressing Enter.
Install the InstagramAPI library by typing pip install InstagramAPI and pressing Enter or install all the requirements using the requirements command pip install -r requirements.txt
.
Clone the HoodMaster repository from GitHub by typing git clone (https://github.com/Hoodmaster2/IG/).git and pressing Enter.
Navigate to the HoodMaster directory by typing cd HoodMaster and pressing Enter.
Run the HoodMaster tool by typing python ig.py and pressing Enter.
You should now be able to use the HoodMaster tool in Termux.

