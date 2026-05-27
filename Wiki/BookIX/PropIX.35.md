# Proposition IX.35

## Statement

If as many numbers as we please are in continued proportion, and there is subtracted from the second and the last numbers equal to the first, then the excess of the second is to the first as the excess of the last is to the sum of all those before it.

## Proof

Let there be as many numbers as we please in continued proportion, *A, BC, D,* and *EF,* beginning from *A* as least, and let there be subtracted from *BC* and *EF* the numbers *BG* and *FH,* each equal to *A.*

I say that *GC* is to *A* as *EH* is to the sum of *A, BC,* and *D.*

Make *FK* equal to *BC,* and *FL* equal to *D.*

Then, since *FK* equals *BC,* and of these the part *FH* equals the part *BG,* therefore the remainder *HK* equals the remainder *GC.*

![java applet or image](propIX35.gif)

And since *EF* is to *D* as *D* is to *BC,* and as *BC* is to *A,* while *D* equals *FL, BC* equals *FK,* and *A* equals *FH,* therefore *EF* is to *FL* as *LF* is to *FK,* and as *FK* is to *FH.* Taken separately *EL* is to *LF* as *LK* is to *FK,* and as *KH* is to *FH.* ([VII.11](../BookVII/PropVII.11.md), [VII.13](../BookVII/PropVII.13.md))

Since one of the antecedents is to one of the consequents as the sum of the antecedents is to the sum of the consequents, therefore *KH* is to *FH* as the sum of *EL, LK,* and *KH* is to the sum of *LF, FK,* and *HF.* ([VII.12](../BookVII/PropVII.12.md))

But *KH* equals *CG, FH* equals *A,* and the sum of *LF, FK,* and *HF* equals the sum of *D, BC,* and *A,* therefore *CG* is to *A* as *EH* is to the sum of *D, BC,* and *A.*

Therefore the excess of the second is to the first as the excess of the last is to the sum of those before it.

Therefore, *if as many numbers as we please are in continued proportion, and there is subtracted from the second and the last numbers equal to the first, then the excess of the second is to the first as the excess of the last is to the sum of all those before it.*

Q.E.D.

## Guide

This proposition says if a sequence of numbers
a1, a2, a3, ...,
a*n*, a*n*+1
is in continued proportion

*a*1 : *a*2 =
*a*2 : *a*3 = ... =
*a**n* : *a**n*+1

then

(*a*2 – *a*1) : *a*1 =
(*a**n*+1 – *a*1) :
(*a*1 + *a*2 + ... + *a**n*).

This conclusion gives a way of computing the sum of the terms in the continued proportion as

*a*1 + *a*2 + ... + *a**n* = *a*1 | *a**n*+1 – *a*1 *a*2 – *a*1 | .

If we denote the first term by *a* and the ratio of the terms by *r,* then this gives the
familiar formula

*a* + *ar* + *ar*2 + ... + *ar**n*-1 = *a* | *r**n* – 1 *r* – 1 | .

Summary of the proof

The proof is much more comprehisible when it’s translated into algebraic notation. The correspondence is as follows

*A* = *a*1 *BC* = *a*2       ... *D* = *a**n* *EF* = *a**n*+1 | *BG* = *FH* = *a*1 *GC* = *a*2 – *a*1 *EH* = *a**n*+1 – *a*1 *a*2 : *a*1.

For each proportion, say the first,

*a**n*+1 : *a**n* =
*a**n* : *a**n*–1,

take it separately according to [VII.11](../BookVII/PropVII.11.md) to get

(*a**n*+1 – *a**n*) : (*a**n* –
*a**n*–1) = *a**n* : *a**n*–1,

then alternately

(*a**n*+1 – *a**n*):*a**n* =
(*a**n* –
*a**n*–1):*a**n*–1.

Stringing the conclusions together, we have

(*a**n*+1 – *a**n*):*a**n* =
(*a**n* –
*a**n*–1):*a**n*–1 = ...
= (*a*2 – *a*1):*a*1.

Next, using proposition [VII.12](../BookVII/PropVII.12.md), the sum of the antecedents is
to the sum of the consequences equals this same ratio. Therefore

(*a**n*+1–*a**n* +
*a**n*–*a**n*–1 + ... +
*a*2–*a*1)
: (*a**n* + *a**n*–1 + ... + *a*2 + *a*1)
= (*a*2 – *a*1) : *a*1.

But *a**n*+1 – *a**n* +
*a**n* – *a**n*–1 + ... +
*a*2 – *a*1 equals
*a**n*+1 – *a*1. That gives us the conclusion of
the proposition

(*a**n*+1 – *a*1) :
(*a**n* + *a**n*–1 + ... +
*a*2 + *a*1)
=
(*a*2 – *a*1) : *a*1.

Use of this propostion

This proposition is used in the next one.

## See also

- [BookIX TOC](BookIX.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookIX/propIX35.html)
