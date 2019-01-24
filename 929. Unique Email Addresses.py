class Solution(object):
    def numUniqueEmails(self, emails):
        spisok = set()
        for i in emails:
            string = i.split('@')
            spisok.add(string[1])
        return len(spisok)
