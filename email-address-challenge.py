def fun(s):
    # return True if s is a valid email, else return False

    if s.count('@') != 1:
        return False

    username = s.split('@')[0]
    lastparts = s.split('@')[1].split('.')
    if not username or len(lastparts) != 2:
        return False

    websitename = lastparts[0]
    extension = lastparts[1]

    for char in username:
        if not char.isalnum() and char != '_' and char != '-':
            return False

    for char in websitename:
        if not char.isalnum():
            return False

    if len(extension) > 3:
        return False

    return True

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    # n = int(raw_input())
    # emails = []
    # for _ in range(n):
    #     emails.append(raw_input())
    emails = ['5', 'dheeraj-234@gmail.com', 'itsallcrap', 'harsh_1234@rediff.in', 'kunal_shin@iop.az', 'matt23@@india.in']

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails

