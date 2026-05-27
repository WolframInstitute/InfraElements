# Proposition IX.36

## Statement

If as many numbers as we please beginning from a unit are set out continuously in double proportion until the sum of all becomes prime, and if the sum multiplied into the last makes some number, then the product is perfect.

## Proof

Let as many numbers as we please, *A, B, C,* and *D,* beginning from a unit be set out in double proportion, until the sum of all becomes prime, let *E* equal the sum, and let *E* multiplied by *D* make *FG.*

I say that *FG* is perfect.

For, however many *A, B, C,* and *D* are in multitude, take so many *E, HK, L,* and *M* in double proportion beginning from *E.*

![java applet or image](propIX36.gif)

[VII.14](../BookVII/PropVII.14.md)

[VII.19](../BookVII/PropVII.19.md)
Therefore, *ex aequali A* is to *D* as *E* is to *M.* Therefore the product of *E* and *D* equals the product of *A* and *M.* And the product of *E* and *D* is *FG,* therefore the product of *A* and *M* is also *FG.*

Therefore *A* multiplied by *M* makes *FG.* Therefore *M* measures *FG* according to the units in *A.* And *A* is a dyad, therefore *FG* is double of *M.*

But *M, L, HK,* and *E* are continuously double of each other, therefore *E, HK, L, M,* and *FG* are continuously proportional in double proportion.

[IX.35](PropIX.35.md)
Subtract from the second *HK* and the last *FG* the numbers *HN* and *FO,* each equal to the first *E.* Therefore the excess of the second is to the first as the excess of the last is to the sum of those before it. Therefore *NK* is to *E* as *OG* is to the sum of *M, L, KH,* and *E.*

And *NK* equals *E,* therefore *OG* also equals *M, L, HK, E.* But *FO* also equals *E,* and *E* equals the sum of *A, B, C, D* and the unit. Therefore the whole *FG* equals the sum of *E, HK, L, M, A, B, C, D,* and the unit, and it is measured by them.

I say also that *FG* is not measured by any other number except *A, B, C, D, E, HK, L, M,* and the unit.

If possible, let some number *P* measure *FG,* and let *P* not be the same with any of the numbers *A, B, C, D, E, HK, L,* or *M.*

And, as many times as *P* measures *FG,* so many units let there be in *Q,* therefore *Q* multiplied by *P* makes *FG.*

[VII.19](../BookVII/PropVII.19.md)
But, further, *E* multiplied by *D* makes *FG,* therefore *E* is to *Q* as *P* is to *D.*

[IX.13](PropIX.13.md)
And, since *A, B, C,* and *D* are continuously proportional beginning from a unit, therefore *D* is not measured by any other number except *A, B,* or *C.*

[VII.Def.20](../BookVII/DefVII.20.md)
And, by hypothesis, *P* is not the same with any of the numbers *A, B,* or *C,* therefore *P* does not measure *D.* But *P* is to *D* as *E* is to *Q,* therefore neither does *E* measure *Q.*

[VII.29](../BookVII/PropVII.29.md)
And *E* is prime, and any prime number is prime to any number which it does not measure. Therefore *E* and *Q* are relatively prime.

[VII.21](../BookVII/PropVII.21.md)

[VII.20](../BookVII/PropVII.20.md)
But primes are also least, and the least numbers measure those which have the same ratio the same number of times, the antecedent the antecedent and the consequent the consequent, and *E* is to *Q* as *P* is to *D,* therefore *E* measures *P* the same number of times that *Q* measures *D.*

But *D* is not measured by any other number except *A, B,* or *C,* therefore *Q* is the same with one of the numbers *A, B,* or *C.* Let it be the same with *B.*

And, however many *B, C,* and *D* are in multitude, take so many *E, HK,* and *L* beginning from *E.*

[VII.14](../BookVII/PropVII.14.md)
Now *E, HK,* and *L* are in the same ratio with *B, C,* and *D,* therefore, *ex aequali B* is to *D* as *E* is to *L.*

[VII.19](../BookVII/PropVII.19.md)
Therefore the product of *B* and *L* equals the product of *D* and *E.* But the product of *D* and *E* equals the product of *Q* and *P,* therefore the product of *Q* and *P* also equals the product of *B* and *L.*

[VII.19](../BookVII/PropVII.19.md)
Therefore *Q* is to *B* as *L* is to *P.* And *Q* is the same with *B,* therefore *L* is also the same with *P,* which is impossible, for by hypothesis *P* is not the same with any of the numbers set out.

Therefore no number measures *FG* except *A, B, C, D, E, HK, L, M,* and the unit.

[VII.Def.22](../BookVII/DefVII.22.md)
And *FG* was proved equal to the sum of *A, B, C, D, E, HK, L, M,* and the unit, and a perfect number is that which equals its own parts, therefore *FG* is perfect.

Therefore, *if as many numbers as we please beginning from a unit are set out continuously in double proportion until the sum of all becomes prime, and if the sum multiplied into the last makes some number, then the product is perfect.*

Q.E.D.

## Guide

In modern notation, this proposition says that if s = 1 + 2 + 22 + ... + 2*p*-1 is a prime number, then n = s2*p*-1 is a perfect number.

Summary of the proof

Euclid begins by assuming that the sum of a number of powers of 2 (the sum beginning with 1) is a prime number.
Let p be the number of powers of 2, and let s be their sum which is prime.

*s* = 1 + 2 + 22 + ... + 2*p*-1

Note that the last power of 2 is 2*p*-1 since the sum starts with 1, which is 20.

In Euclid’s proof, *A* represents 2, *B* represents 22, *C* represents 23, and *D* is supposed to be the last power of 2, so it represents 2*p*-1. Also, *E* represents their sum *s,* and *FG* is the product of *E* and *D,* so it represents *s*2*p*-1. Let’s denote that last by *n.*

*n* = *s*2*p*-1

The goal is to show that *n* is a perfect number.

In the first part of this proof, Euclid finds some proper divisors of *n* that sum to *n.* These come in two sequences:

1, 2, 22, ..., 2*p*-1

and

*s,* 2*s,* 22*s,* ..., 2*p*-2*s*

In his proof, the latter are represented by *E, HK, L,* and finally *M.*

It is clear that each of these is a proper divisor of *n,* and later in the proof Euclid shows that they are the only proper divisors of *n.*

Using the previous proposition, [IX.35](PropIX.35.md), Euclid finds the sum of the continued proportion,

*s* + 2*s* + 22*s* + ... + 2*p*-2*s,*

to be 2*p*-1*s* – *s.* But *s* was the sum
1 + 2 + 22 + ... + 2*p*-1, hence,

*n* = 2*p*-1*s* | = | 1 + 2 + 22 + ... + 2*p*-1
| | + *s* + 2*s* + 22*s* + ... + 2*p*-2*s*

Thus, *n* is a sum of these proper divisors.

All that is left to do is to show that they are the only proper divisors of *n,* for then *n* will be the sum of all of its proper divisors, whence a perfect number.

The remainder of the proof is detailed and difficult to follow. It hinges on [IX.13](PropIX.13.md) which implies that the only factors of 2*p*-1 are powers of 2, so all the factors of 2*p*-1 have been found. Here’s a not-too-faithful version of Euclid’s argument. Suppose *n* factors as *ab* where *a* is not a proper divisor of *n* in the list above. In Euclid’s proof, *P* represents *a* and *Q* represents *b.*

Since *ab* = *n* = 2*p*-1*s*, but *a* is not a power of 2, and *s* is prime, therefore *s* divides *a*. So *b* has to be a power of 2. But then *a* has to be a power of 2 times *s.* But all the powers of 2 times *s* are on the list of known proper divisors. Therefore, the list includes all the proper divisors.

Mersenne primes and perfect numbers

Note that the sum, s = 1 + 2 + 22 + ... + 2*p*-1, equals 2*p* – 1, by IX.35. As this fact is not needed in the proof, Euclid omits to mention it. Thus, we can restate the proposition as follows:

If 2*p* – 1 is a prime number, then (2*p* – 1) 2*p*-1 is a perfect number.

Prime numbers of the form 2*p* – 1 have come to be called Mersenne primes named in honor of Marin Mersenne (1588–1648), one of many people who have studied these numbers. The four smallest perfect numbers, 6, 28, 496, and 8128, were known to the ancient Greek mathematicians. The Mersenne primes 2*p* – 1 corresponding to these four perfect numbers are 3, 7, 31, and 127, respectively, where the exponents p are 2, 3, 5, and 7, respectively.

The observation that these four exponents are all prime suggests the following two questions:

In order for 2*p* – 1 to be prime, is it sufficient for *p* to be prime?
In order for 2*p* – 1 to be prime, is it necessary for *p* to be prime?

Naturally, the next number to check for primality is 211 – 1, 2047, which, by a simple search for prime factors is found not to be prime. The number 2047 factors as 23 times 89. Therefore, primality of p is not sufficient.

In 1640 Pierre de Fermat (1601–1665) wrote to Mersenne with his investigation of these primes. Fermat found three conditions on *p* that were necessary for 2*p* – 1 to be prime.
One of these conditions answers the second question above: *p* does have to be prime. Here’s a quick argument for that. If *p* did factor, say as *ab,* then 2*p* – 1, which is
2*ab* – 1, would also factor, namely as

2*ab* – 1 =
(2*a* – 1)
(2*a*(*b*-1) +
2*a*(*b*-2)  + ... +
2*a*).

Many mathematicians have studied Mersenne primes since then. A fairly practical testing algorithm was constructed in 1876 by Éduard Lucas (1842–1891). He showed that the the number
2*p* – 1 is prime if and only if it divides the number *S*(*p*–1), where *S*(*p*–1) is defined recursively: *S*(1) = 4, and *S*(*n*+1) = *S*(*n*)2 – 2.

The search for more Mersenne primes, and therefore more perfect numbers, continues. It is not known if there are infinitely many or finitely many even perfect numbers. Mersenne primes are scarce, but more continue to be found. There are at least 48 of them, the largest known (as of January 2013) is 257,885,161 – 1. It has 17,425,170 digits. For more information, see the [The Great Internet Mersenne Prime Search](http://www.mersenne.org/), GIMPS.

There is a also a question about odd perfect numbers: Are there any? It has been shown that there are no small odd perfect numbers; it is known that odd numbers with fewer then 300 digits are not perfect. It may well be that there are no odd perfect numbers, but to date there is no proof.

## See also

- [BookIX TOC](BookIX.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookIX/propIX36.html)
