def mail_merge(names, mail_template):
    with open(names) as names, open(mail_template) as mail:
        names = names.readlines()
        mail = mail.readlines()
        emails = []
        for name in names:
            new_part = []
            for line in mail:
                line = line.split()
                new_line = line[:]
                for idx, word in enumerate(line):
                    if "<name>" in word:
                        word = word.replace("<name>", name[:len(name)-1])
                        new_line[idx] = word
                new_part.append(" ".join(new_line) + "\n")
            emails.append("".join(new_part))
        return emails