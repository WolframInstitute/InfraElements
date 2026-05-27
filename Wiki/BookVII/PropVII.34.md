# Proposition VII.34

## Statement

To find the least number which two given numbers measure.

## Proof

Let *A* and *B* be the two given numbers.

It is required to find the least number which they measure.

Now either *A* and *B* are relatively prime or they are not.

First, let *A* and *B* be relatively prime. Multiply *A* by *B* to make *C.* Then *B* multiplied by *A* makes *C.* Therefore *A* and *B* measure *C.* ([VII.18](PropVII.18.md))

![java applet or image](propVII34a.gif)

I say next that it is also the least number they measure.

If not, then *A* and *B* measure some number *D* less than *C*

Let there be as many units in *E* as the times that *A* measures *D,* and as many units in *F* as the times that *B* measures *D.*

Then *A* multiplied by *E* makes *D,* and *B* multiplied by *F* makes *D.* Therefore the product of *A* and *E* equals the product of *B* and *F.* Therefore *A* is to *B* as *F* is to *E.* ([VII.Def.15](DefVII.15.md), [VII.19](PropVII.19.md))

But *A* and *B* are relatively prime, primes are also least, and the least measure the numbers which have the same ratio the same number of times, the greater the greater and the less the less, therefore *B* measures *E* as the consequent the consequent. ([VII.21](PropVII.21.md), [VII.20](PropVII.20.md))

And, since *A* multiplied by *B* and by *E* makes *C* and *D,* therefore *B* is to *E* as *C* is to *D.* But *B* measures *E,* therefore *C* also measures *D,* the greater the less, which is impossible. ([VII.17](PropVII.17.md))

Therefore *A* and *B* do not measure any number less than *C.* Therefore *C* is the least that is measured by *A* and *B.*

Next, let *A* and *B* not be relatively prime. Take *F* and *E,* the least numbers of those which have the same ratio with *A* and *B.* Therefore the product of *A* and *E* equals the product of *B* and *F.* ([VII.33](PropVII.33.md), [VII.19](PropVII.19.md))

![java applet or image](propVII34b.gif)

Multiply *A* by *E* to make *C.* Then *B* multiplied by *F* makes *C.* Therefore *A* and *B* measure *C.*

I say next that it is also the least number that they measure.

If not, then *A* and *B* measure some number *D* less than *C.*

Let there be as many units in *G* as the times that *A* measures *D,* and as many units in *H* as the times that *B* measures *D.*

Then *A* multiplied by *G* makes *D,* and *B* multiplied by *H* makes *D.* Therefore the product of *A* and *G* equals the product of *B* and *H.* Therefore *A* is to *B* as *H* is to *G.* ([VII.19](PropVII.19.md))

But *A* is to *B* as *F* is to *E.* Therefore *F* is to *E* as *H* is to *G.* ([V.11](../BookV/PropV.11.md))

But *F* and *E* are least, and the least measure the numbers which have the same ratio the same number of times, the greater the greater and the less the less, therefore *E* measures *G.* ([VII.20](PropVII.20.md))

And, since *A* multiplied by *E* and by *G* makes *C* and *D,* therefore *E* is to *G* as *C* is to *D.* ([VII.17](PropVII.17.md))

But *E* measures *G,* therefore *C* also measures *D,* the greater the less, which is impossible. Therefore *A* and *B* do not measure any number less than *C.* Therefore *C* is the least that is measured by *A* and *B.*

Q.E.D.

## Guide

The least common multiple of two numbers a and b is the smallest number that they both divide. It is denoted LCM(a, b). This proposition constructs it as the product divided by the greatest common divisor:

LCM(*a, b*) = *ab*/LCM(*a, b*).

Use of this proposition

This proposition is used in VII.36 and
VIII.4.

## See also

- [BookVII TOC](BookVII.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookVII/propVII34.html)
