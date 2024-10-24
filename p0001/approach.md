
# Multiples of 3 or 5

## Problem

If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.

Find the sum of all the multiples of $3$ or $5$ below $1000$.

## Answer

**Multiples of 5**

Matching values that sum to 1000:

(5, 995), (10, 990), ... , (500, 500)

We have 100 pairs, each add to 1000, and one repeat (500, 500). So, these values sum to 100,000 - 500 = 99,500

**Multiples of 3**

Matching values that sum to 999:

(3, 996), (6, 993), (9, 990), ... , (498, 501)

In this case, there is no repeat, and there are 166 pairs. We also add 999 since this is below 1000. This sum is (166)(999) + 999 = 166,833

**Overlap**

There is some overlap between multiples of 3 and 5. This is any multiple of 15. So, we can do the same thing for 15 then subtract it from the sum of the two parts above. This is similar to taking the union of two sets:

$$ A \cup B = A + B - A \cap B $$

Summing to 990:
(15, 975), (30, 960), ... , (495, 495)

There are 33 pairs that add to 990, with one repeat of 495, and including 990, which multiplies to (33)(990)+990-465 = 33660.

**Final**

So, the final sum is 99500 + 166833 - 33165 = 233168