"""
929. Unique Email Addresses
문제: https://leetcode.com/problems/unique-email-addresses/description/
"""


class Solution:
    def numUniqueEmails(self, emails):
        emails = [email.split("@") for email in emails]

        for i in range(len(emails)):
            tmp = ""
            for s in emails[i][0]:
                if s == ".":
                    continue
                if s == "+":
                    break
                tmp += s
            emails[i][0] = tmp
            emails[i] = emails[i][0] + "@" + emails[i][1]

        return len(set(emails))

"""
class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> set = new HashSet<>();

        for (String email : emails) {
            String[] tmp = email.split("@");
            StringBuilder s = new StringBuilder();
            for (char c : tmp[0].toCharArray()) {
                if (c == '+') {
                    break;
                }
                if (c == '.') {
                    continue;
                }
                s.append(c);
            }
            set.add(s.append("@").append(tmp[1]).toString());
        }
        return set.size();
    }
}
"""