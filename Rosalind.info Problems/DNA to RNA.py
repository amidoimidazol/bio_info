t = "GGTTGAAGGGCCCGTATTCATCTCTGGGAGTCCAGGACACGACCTTATATTGTAGATTTACAGCTGTTCTTGTAGATACAGATGTACTCATATGTCCGCTTTCTAGGACAGAGACCAGCTGTAGACCTAACATAGGATTGACAAAGCACTCCCGAAGCTATTCGTGCCTGTGACAGAGACAGCGCATACGCGCTGTCTGGCAGGCCACGGTTTTTGTCTTATCGTCCTTTCCCGGAACAGCATGCGTAGGAATGCTAACCAGATGGTAGTCAAGGACGTCCTTGGTAGCCCGGAGATCGGGACTGGCGCTACTCAGGATGGATGTCAAAGACATGTCTACTCGATGTTCTAACGCAATGTATCACGTTATTGGTAGAGTCCAGTCACTCGCCTGATAAACTCTCTTTTATTATTTTCTGTCCAGTTCGAGTGTGCCACAGTCTGTACCGTAAGCCAGACAATAGTGATGTCGTGACGCAAGGCCGCAGTTAAAACATCTAAGCGTGCGACTTAGCCCGTCTATGAGTCCAAGGCAATTATACAGCCGCAGCTGACTTCGGGTGGTGGGTCTGAATCTGTGTTATTCTGTTATCGCAATCTCTCGTACATCTTACCGCTCACTAGTATATCCCCCAGCAATCCCTAGCCGGTGGAGGACCAGGTCCTCCCTTATCGGCAATAGTATTCTTATATAGGCAGAAAGTCGAAGACGCGACTTGTGCCTCCCCTACGACCGCCATCGCTTTTCCAACGTGGCAAGCTTTTTTAAGGTGCCAGGGTGTGTGCTTCAAAGGCGGGCGACAGTCTCACGGTCTGGTTTACGTATGAAGACAGCGAGCTACTTTAACTTCTAACTCGGGGTGGCTCGGAGAGGGAGGAACGAGAAATCCTAATCACATGTTATAACCTCGTTGC"
a = ""
for i in range(len(t)):
    if t[i] == "T":
        a = a + "U"
    else:
        a = a + t[i]
print a