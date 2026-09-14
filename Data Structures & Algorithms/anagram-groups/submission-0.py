class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict_list = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if str_dict_list.get(sorted_str):
                str_dict_list[sorted_str].append(s)
            else:
                str_dict_list[sorted_str] = [s]
        output = []
        for value in str_dict_list.values():
            output.append(value)
        return output