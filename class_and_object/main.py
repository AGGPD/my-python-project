from user import User
from post import Post

app_user_one = User("nn@nn.com", "Andy", "pw0d", "Tester")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "James", "supertwo", "Agent")
app_user_two.get_user_info()

new_post = Post("on a secret mission day", app_user_one.name)
new_post.get_post_info()