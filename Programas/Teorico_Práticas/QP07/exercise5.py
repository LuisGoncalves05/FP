def cycle_length(number, digits):
    past_sq = set()
    seq = set()
    sq = next_middle_square(number, digits)
    while True:
        sq = next_middle_square(sq, digits)
        if sq in past_sq:
            if sq in seq:
                return len(seq)
            seq.add(sq)
            
        past_sq.add(sq)


def next_middle_square(number, digits):
   """Compute the next pseudo-random using the 
      middle square algorithm and the given number of digits."""
   k = digits // 2         # half of the number of digits
   square = number*number  # compute the square
   middle = (square // (10**k)) % (10**digits)   # extract middle part
   return middle

