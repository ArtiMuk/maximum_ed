# def count_symbol(string):
#     for x in set(string):
#         print(x, string.count(x))
        
 
# def count_symbol(s):
#     syms_counter={}
#     for i in s:
#         if syms_counter.get(i) is None:
#             syms_counter[i]=1
#             continue
#         syms_counter[i]+=1
#     print(syms_counter)


def count_symbol(s):
    syms_counter={}
    for i in s:
        syms_counter[i]=syms_counter.get(i,0)+1
    print(syms_counter)
    

count_symbol('aabcd')