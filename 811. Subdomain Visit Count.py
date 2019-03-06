class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        if not cpdomains:
            return []
        res = {}
        for record in cpdomains:
            count, domains = record.split(' ')
            domains = domains.split('.')
            domain_list = []
            for i in range(len(domains)):
                domain_list.append('.'.join(domains[i:]))
            for domain in domain_list:
                if domain in res:
                    res[domain] += int(count)
                else:
                    res[domain] = int(count)
        res_list = []
        for r in res:
            res_list.append(str(res[r]) + ' ' + str(r))
        return res_list


if __name__ == "__main__":
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(Solution().subdomainVisits(cpdomains))
