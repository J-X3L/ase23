# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'cyberdigit'  # <- enter username here
insta_password = 'jeffrexxy'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=1000,
                                    min_followers=45,
                                    min_following=77)
    #find 10 profiles with these tags  
    session.like_by_tags(["programming", "#code"], amount=10)

    #follow them all 
    session.set_do_follow(True, percentage=100)
