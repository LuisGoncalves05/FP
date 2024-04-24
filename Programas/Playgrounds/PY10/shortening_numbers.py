def shorten(suffixes, base):
    def convert(arg):
        if type(arg) == str:
            try:
                arg = int(arg)
            except:
                return arg
            i = 0
            while arg >= base:
                i += 1
                arg = arg / base
            arg = int(arg)
            arg = str(arg) + " " + suffixes[i]
        elif type(arg) == list:
            for j in range(len(arg)):
                item = arg[j]
                try:
                    item = int(item)
                except:
                    return f"{arg}"
                i = 0
                while item >= base:
                    i += 1
                    item = item / base
                arg[j] = str(item) + " " + suffixes[i]
        return arg
    return convert

print(shorten(["", "K", "M"], 1000)(["dummy", "list"]))