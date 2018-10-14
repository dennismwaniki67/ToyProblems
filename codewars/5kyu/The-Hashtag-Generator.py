# The marketing team is spending way too much time typing in hashtags.
# Let's help them with out own Hashtag Generator!
#
# Here's the deal:
#
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.


def generate_hashtag(s):
    # your code here
    string = []
    for i in s:
        string = ''.join(("#", "i"))
        string = string.capitalize()
        string = string.replace(" ", "")

        if len(string) > 140:
            return False

        elif len(string) == 0:
            return False
        else:
            return string