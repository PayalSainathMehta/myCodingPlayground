def numUniqueEmails(emails):
	stack = []
	for email in emails:
                parts = email.split('@')
                new_part = parts[0].replace('.','')
		new_part2 = new_part[0:new_part.find('+')]
                res = new_part2 + parts[1]
                if res not in stack:
                        stack.append(res)
                else continue

        return len(stack)


numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
)
