from collections import Counter

def getBaseline(char_counts):
    first_val = None
    second_val = None
    for value in char_counts.values():
        if not first_val:
            first_val = value
            continue
        if not second_val:
            second_val = value
            if second_val == first_val:
                return value, True
            continue
        if value == first_val or value == second_val:
            return value, True
        return None, False
        
def isValid(s):
    char_counts = Counter(s)
    if len(char_counts) == 1:
        return 'YES'
    baseline, canMake = getBaseline(char_counts)
    if not canMake:
        return 'NO'
    used_removal = False
    for value in char_counts.values():
        diff = abs(value - baseline)
        if diff > 1:
            if value == 1 and not used_removal:
                used_removal = True
                continue
            return 'NO'
        if diff == 1:
            if used_removal:
                return 'NO'
            used_removal = True
    return 'YES'
    
print(isValid('abc'))
print(isValid('abcc'))
print(isValid('abccc'))
print(isValid('aabbcd'))
print(isValid('aabbccddeefghi'))
print(isValid('abcdefghhgfedecba'))
print(isValid('ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'))