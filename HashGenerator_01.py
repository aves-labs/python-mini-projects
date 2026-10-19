def generate_hashtag(s):
    # First Let's make a list of the words
    s_list = s.split()
    # Checks if the list is empty
    if not s_list:
        return False
    # We now want to capitalize each word
    for i in range(len(s_list)):
        s_list[i] = s_list[i].capitalize()
    # '#'hashtags must be included
    result_s = '#' + ''.join(s_list)
    # We don't allow long cat
    if len(result_s) > 140:
        return False
    return result_s
count = 1
while True:
    s = input(f"Your {count}th Hash[or 'e' for exit]: ")
    if s == 'exit' or s == 'e':
        print('Code Exited')
        exit()
    count += 1
    print(generate_hashtag(s))
