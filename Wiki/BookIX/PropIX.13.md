# Proposition IX.13

## Statement

If as many numbers as we please beginning from a unit are in continued proportion, and the number after the unit is prime, then the greatest is not measured by any except those which have a place among the proportional numbers.

## Proof

Let there be as many numbers as we please, *A, B, C,* and *D,* beginning from a unit and in continued proportion, and let *A,* the number after the unit, be prime.

I say that *D,* the greatest of them, is not measured by any other number except *A, B,* or *C.*

If possible, let it be measured by *E,* and let *E* not be the same with any of the numbers *A, B,* or *C.*

![java applet or image](propIX13.gif)

[IX.12](PropIX.12.md)
It is then clear that *E* is not prime, for if *E* is prime and measures *D,* then it also measures *A,* which is prime, though it is not the same with it, which is impossible. Therefore *E* is not prime, so it is composite.

[VII.31](../BookVII/PropVII.31.md)
But any composite number is measured by some prime number, therefore *E* is measured by some prime number.

I say next that it is no measured by any other prime except *A.*

[IX.12](PropIX.12.md)
If E is measured by another, and E measures D, then that other measures D, so that it also measures A, which is prime, though it is not the same with it, which is impossible. Therefore [only the prime] A measures E.

And, since *E* measures *D,* let it measure it according to *F.*

I say that *F* is not the same with any of the numbers *A, B,* or *C.*

[IX.11](PropIX.11.md)
If *F* is the same with one of the numbers *A, B,* or *C,* and measures *D* according to *E,* then one of the numbers *A, B,* or *C* also measures *D* according to *E.* But one of the numbers *A, B,* or *C* measures *D* according to some one of the numbers *A, B,* or *C,* therefore *E* is also the same with one of the numbers *A, B* or *C,* which is contrary to the hypothesis.

Therefore *F* is not the same as any one of the numbers *A, B,* or *C.*

Similarly we can prove that *F* is measured by *A,* by proving again that *F* is not prime.

[IX.12](PropIX.12.md)
If it is, and measures *D,* then it also measures *A,* which is prime, though it is not the same with it, which is impossible. Therefore *F* is not prime, so it is composite.

[VII.31](../BookVII/PropVII.31.md)
But any composite number is measured by some prime number, therefore *F* is measured by some prime number.

I say next that it is not measured by any other prime except *A.*

[IX.12](PropIX.12.md)
If any other prime number measures *F,* and *F* measures *D,* then that other also measures *D,* so that it also measures *A,* which is prime, though it is not the same with it, which is impossible. Therefore [only the prime] *A* measures *F.*

And, since *E* measures *D* according to *F,* therefore *E* multiplied by *F* makes *D.*

[IX.11](PropIX.11.md)
But, further, *A* multiplied by *C* makes *D,* therefore the product of *A* and *C* equals the product of *E* and *F.*

[VII.19](../BookVII/PropVII.19.md)
Therefore, proportionally *A* is to *E* as *F* is to *C.*

But *A* measures *E,* therefore *F* also measures *C.* Let it measure it according to *G.*

Similarly, then, we can prove that *G* is not the same with any of the numbers *A* or *B,* and that it is measured by *A.* And, since *F* measures *C* according to *G,* therefore *F* multiplied by *G* makes *C.*

[IX.11](PropIX.11.md),
[VII.19](../BookVII/PropVII.19.md)
But, further, *A* multiplied by *B* makes *C,* therefore the product of *A* and *B* equals the product of *F* and *G.* Therefore, proportionally *A* is to *F* as *G* is to *B.*

But *A* measures *F,* therefore *G* also measures *B.* Let it measure it according to *H.*

Similarly then we can prove that *H* is not the same with *A.*

[IX.8](PropIX.8.md)
And, since *G* measures *B* according to *H,* therefore *G* multiplied by *H* makes *B.* But, further, *A* multiplied by itself makes *B,* therefore the product of *H* and *G* equals the square on *A.*

[VII.19](../BookVII/PropVII.19.md)
Therefore *H* is to *A* as *A* is to *G.* But *A* measures *G,* therefore *H* also measures *A,* which is prime, though it is not the same with it, which is absurd.

Therefore *D* the greatest is not measured by any other number except *A, B,* or *C.*

Therefore, *if as many numbers as we please beginning from a unit are in continued proportion, and the number after the unit is prime, then the greatest is not measured by any except those which have a place among the proportional numbers.*

Q.E.D.

## Guide

This proposition says that the only numbers that can divide a power of a prime are smaller powers of that prime.

Outline of the proof

The proof involves a reduction step like that in the proof of the previous proposition.

Suppose a number *e* divides a power *p**k* of a prime number *p,* but *e* does not equal any lower power of *p.*

First note that *e* can’t be prime itself, since then it would divide *p* ([IX.12](PropIX.12.md)), which it doesn’t.

Then *e* is composite. Then some prime number *q* divides *e* ([VII.31](../BookVII/PropVII.31.md)). Then *q* also divides *p**k*, which it implies *q* divides *p.* Therefore, the only prime that can divide *e* is *p.*

The rest of the proof is repeated reduction of the power *k.* Since *e* is not 1, it is divisible by *p.* Let *g* be *e/p.* Then *g* divides *p**k*-1, but is not any lower power of *p.* Then the same argument can be applied. Continue in this manner until some number divides *p* but is not 1 or *p,* a contradiction. Thus, the only numbers that can divide a power of a prime are smaller powers of the prime.

Use of this proposition

This proposition is used in IX.32 and IX.36.

## See also

- [BookIX TOC](BookIX.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookIX/propIX13.html)
