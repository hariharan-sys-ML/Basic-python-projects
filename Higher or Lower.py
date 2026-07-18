import random
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    }
]
score = 0
should_continue = True
A = random.choice(data)
B = random.choice(data)
print(f"Welcome To The Game\n\n")
while should_continue:
    if A == B:
        B = random.choice(data)

    print(f"First Person -  {A['name']} , {A['description']} from {A['country']} ")
    print(f"Second Person -  {B['name']} , {B['description']} from {B['country']} \n")
    user_input = input("Enter your choice , Who has more followers? A or B: ").upper()
    if user_input == "A":
        if A['follower_count'] > B['follower_count']:
            print("You Are Right ! Next ------> ")
            score += 1
            A = B.copy()
            B = random.choice(data)
            if A == B:
                B = random.choice(data)
            should_continue = True
        else:
            should_continue = False
            print("You Are Wrong , Try Next Time")
            print(f"Followers of {A['name']} - {A['follower_count']}")
            print(f"Followers of {B['name']} - {B['follower_count']}")


    else:
        if B['follower_count'] > A['follower_count']:
            print("You Are Right ! Next ------> ")
            score += 1
            A = B.copy()
            B = random.choice(data)
            if A == B:
                B = random.choice(data)
            should_continue = True
        else:
            should_continue = False
            print("You Are Wrong , Try Next Time")
            print(f"Followers of {A['name']} - {A['follower_count']}")
            print(f"Followers of {B['name']} - {B['follower_count']}")
