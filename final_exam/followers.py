facebook_fame = {}

while True:
    user_input = input().split(': ')
    command = user_input[0]
    if command == 'Log out':
        break

    if command == 'New follower':
        follower_username = user_input[1]
        if follower_username not in facebook_fame:
            facebook_fame[follower_username] = [0, 0]
        else:
            continue

    elif command == 'Like':
        follower_username = user_input[1]
        likes = int(user_input[2])
        if follower_username not in facebook_fame:
            facebook_fame[follower_username] = [likes, 0]
        else:
            follower_data = facebook_fame[follower_username]
            previous_count_of_likes = int(follower_data[0])
            current_likes = previous_count_of_likes + likes
            follower_data[0] = current_likes
            facebook_fame[follower_username] = follower_data

    elif command == 'Comment':
        follower_username = user_input[1]
        if follower_username not in facebook_fame:
            facebook_fame[follower_username] = [0, 1]
        else:
            follower_data = facebook_fame[follower_username]
            previous_count_of_comments = int(follower_data[1])
            current_comments = previous_count_of_comments + 1
            follower_data[1] = current_comments
            facebook_fame[follower_username] = follower_data

    elif command == 'Blocked':
        follower_username = user_input[1]
        if follower_username not in facebook_fame:
            print(f"{follower_username} doesn't exist.")
        else:
            del facebook_fame[follower_username]

count_of_followers = 0
list_of_followers = []
for username, user_data in facebook_fame.items():
    count_of_followers += 1
    list_of_followers.append(f'{username}: {user_data[0]+user_data[1]}')

print(f'{count_of_followers} followers')
print('\n'.join(list_of_followers))
