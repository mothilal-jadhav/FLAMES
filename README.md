# FLAMES

Very common game i think most of us have played in childhood and these used to be great motivation for not giving up on crush despite rejection. 

Used to these with everyone in the classroom in the backpage of notebook and it used to be news if someone looks at the back of the page so to avoid those kind of issues and save paper and ink lets code it in python so our only effort would be giving the inputs as names and thats it, the algorithm decides what is the relationship b/w those names.

in FLAMES:
1. F -> Friends
2. L -> Lovers
3. A -> Affectionate
4. M -> Marriage
5. E -> Enemies
6. S -> Siblings


## There are two steps in this game:

1. First take the two names
2. Remove the common characters with their respective common occurrences
3. Get the count of the characters that are left 
4. Take FLAMES letters as ["F", "L", "A", "M", "E", "S"]
5. Start removing letter using the count we got
6. The letter which last the process is the result


## Example 

1. Input   ->
2. Output  ->

## Algorithm

Counting is done in anti-clock wise fashion

1. FLAMES

counting is start from F, E is at 5th count so we remove E and start counting again but a this time start from S 
2. FLAMS 

M is at 5th count so we remove M and counting start from S 
3. FLAS 

S is at 5th count so we remove S and counting start from F 
4. FLA 

L is at 5th count so we remove L and counting start from A
5. FA 

A is at 5th count so we remove A. now we have only one letter is remaining so this is the final answer
6. F 

So, the relationship is F i.e. Friends 