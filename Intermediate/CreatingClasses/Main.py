class User:
    
    def __init__(self, id, username):
        print("User being created...")
        self.id = id
        self.username = username
        self.following = 0
        self.followers = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Austin")

print(user_1.username)

user_2 = User("002", "Robertson")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)