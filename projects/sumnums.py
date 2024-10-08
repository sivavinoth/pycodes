# def mysum (* num):
#     out = 0
#     for numb in num:
#         out = out + numb
#     return out
# total = mysum(1,2,3)
# print(total)


def sof(ob):
    total = 0
    for obj in ob:
        if isinstance(obj, list):
            total += sof(obj)

        else:
            try:
                total += float(obj)

            except ValueError:
                pass

    return total


val = ["1", [1, 2, 3]]
res = sof(val)
print(res)
