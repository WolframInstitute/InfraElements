# Proposition VII.27

## Statement

If two numbers are relatively prime, and each multiplied by itself makes a certain number, then the products are relatively prime; and, if the original numbers multiplied by the products make certain numbers, then the latter are also relatively prime.

## Proof

Let *A* and *B* be two relatively prime numbers, let *A* multiplied by itself make *C,* and multiplied by *C* make *D,* and let *B* multiplied by itself make *E,* and multiplied by *E* make *F.*

![java applet or image](propVII27.gif)

I say that *C* and *E* are relatively prime, and that *D* and *F* are relatively prime.

Since *A* and *B* are relatively prime, and *A* multiplied by itself makes *C,* therefore *C* and *B* are relatively prime. ([VII.25](PropVII.25.md))

Since, then, *C* and *B* are relatively prime, and *B* multiplied by itself makes *E,* therefore *C* and *E* are relatively prime.

Again, since *A* and *B* are relatively prime, and *B* multiplied by itself makes *E,* therefore *A* and *E* are relatively prime.

Since, then, the two numbers *A* and *C* are relatively prime to the two numbers *B* and *E,* both to each, therefore the product of *A* and *C* is relatively prime to the product of *B* and *E.* And the product of *A* and *C* is *D,* and the product of *B* and *E* is *F.* ([VII.26](PropVII.26.md))

Therefore *D* and *F* are relatively prime.

Therefore, *if two numbers are relatively prime, and each multiplied by itself makes a certain number, then the products are relatively prime; and, if the original numbers multiplied by the products make certain numbers, then the latter are also relatively prime.*

Q.E.D.

## Guide

The proposition states that

if *a* and *b* are relatively prime, then *an* and *bn* are relatively prime.

Euclid’s proof only covers the cases where *n* is 2 or 3, but the way it is used in [VIII.2](../BookVIII/PropVIII.2.md), any powers need to be relatively prime.

The proof of this proposition uses the last two propositions. Assume that *a* and *b* are relatively prime. Then applying [VII.25](PropVII.25.md) twice, we first get *a*2 and *b* relatively prime, then we get *a*2 and *b*2 relatively prime.

Again, by [VII.25](PropVII.25.md), *a* and *b*2 are relatively prime. Now, *a* is relatively prime to *b*2, and *b* is relatively prime to *a*2, so by [VII.26](PropVII.26.md), *a*3 is relatively prime to *b*3.

Likewise, higher powers of *a* and *b* can be shown to be relatively prime.

Use of this proposition

This proposition is used in VIII.2 and VIII.3.

## See also

- [BookVII TOC](BookVII.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookVII/propVII27.html)
