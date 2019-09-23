def numUniqueEmails(emails):
    stack = []
    for email in emails:
        parts = email.split('@')
        new_part = parts[0].replace('.','')
        if '+' in new_part:
            new_part2 = new_part[0:new_part.find('+')]
        else:
            new_part2 = new_part
        res = new_part2 + '@' + parts[1]
        if res not in stack:
            stack.append(res)

    return len(stack)


print(numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))
