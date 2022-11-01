"""Examples of a class and objects."""

class Profile: 
    handle: str
    followers: int
    is_private: bool

    def __init__(self, handle: str):
        """Constructor initializes attributes!"""
        self.handle = handle
        self.followers = 0 
        self.is_private = False 

    def tweet(self, msg: str) -> None:
        """An example of a method."""
        print(f"@{self.handle} tweets {msg}")


my_profile: Profile = Profile("allyparr")
my_profile.tweet("Hello, world.")
#another_profile: Profile = Profile("allyparr")
#another_profile.handle = "theverge"