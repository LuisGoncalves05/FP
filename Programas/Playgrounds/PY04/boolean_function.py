def validate(grade):
    return (type(grade) == type(3) or type(grade) == type(2.1)) and 0 <= grade <= 100