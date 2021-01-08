Description:
    Basic fibonnaci recursive one line implementation. 
    This is the easiest, fancy way to get the value of a determinated index in the 
    fibonnaci secuence.

    it can take back index without issue until 40. After that recursion gets slow.

    To improve this we can change recursion for the formula:
        round(math.pow(((math.sqrt(5)+1)/2),n)/math.sqrt(5))
    where n is the index to calculate.

How to run:
    python fibonnaci.py <index>

