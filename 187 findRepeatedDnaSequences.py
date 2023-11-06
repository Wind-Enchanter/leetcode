def findRepeatedDnaSequences(self, s: str) -> List[str]:
    dna_part = {}
    output = []
    if len(s) <= 10:
        return []
    else:
        i = 1
        while i <= len(s) - 9:
            new_part = s[i - 1:i + 9]
            try:
                dna_part[new_part] += 1
            except KeyError:
                dna_part[new_part] = 1
            i += 1

    for key in dna_part:
        if dna_part[key] > 1 and key != "":
            output.append(key)

    return output