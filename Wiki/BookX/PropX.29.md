# Proposition X.29

## Statement

To find two rational straight lines commensurable in square only such that the square on the greater is greater than the square on the less by the square on a straight line commensurable in length with the greater.

## Proof

Set out any rational straight line *AB*, and two square numbers *CD* and *DE* such that their difference *CE* is not square.

![java applet or image](propX29.gif)

Describe the semicircle *AFB* on *AB*, and let it be contrived that *DC* is to *CE* as the square on *BA* is to the square on *AF*. Join *FB*. ([X.6,Cor.](PropX.6.md))

Since the square on *BA* is to the square on *AF* as *DC* is to *CE*, therefore the square on *BA* has to the square on *AF* the ratio which the number *DC* has to the number *CE*. Therefore the square on *BA* is commensurable with the square on *AF*. ([X.6](PropX.6.md))

But the square on *AB* is rational, therefore the square on *AF* is also rational. Therefore *AF* is also rational. ([X.Def.I.4](DefX.I.4.md))

And, since *DC* does not have to *CE* the ratio which a square number has to a square number, neither does the square on *BA* have to the square on *AF* the ratio which a square number has to a square number, therefore *AB* is incommensurable in length with *AF*. ([X.9](PropX.9.md))

Therefore *BA* and *AF* are rational straight lines commensurable in square only.

And since *DC* is to *CE* as the square on *BA* is to the square on *AF*, therefore, in conversion, *CD* is to *DE* as the square on *AB* is to the square on *BF*. ([V.19,Cor.](../BookV/PropV.19.md), [III.31](../BookIII/PropIII.31.md), [I.47](../BookI/PropI.47.md))

But *CD* has to *DE* the ratio which a square number has to a square number, therefore the square on *AB* has to the square on *BF* the ratio which a square number has to a square number. Therefore *AB* is commensurable in length with *BF*. ([X.9](PropX.9.md))

And the square on *AB* equals the sum of the squares on *AF* and *FB*, therefore the square on *AB* is greater than the square on *AF* by the square on *BF* commensurable with *AB*.

Therefore there have been found two rational straight lines *BA* and *AF* commensurable in square only such that the square on the greater *AB* is greater than the square on the less *AF* by the square on *BF* commensurable in length with *AB*.

Q.E.D.

## Guide

About Lemma 1

Euclid records in Lemma 1 a method to generate Pythagorean triples. As it depends only on the material in Book IX, logically, it could have appeared there rather than here in Book X. It appears here since it is needed in the proof of the proposition. It is likely much older than the rest of Book X.

Here is a paraphrase of the method of lemma 1, written in a modern algebraic notation. Let *n*2 (= *AB*) and *m*2 (= *BC*) be two numbers of the same parity with *n*2 larger. Then *n*2 – *m*2 is an even number, so let *k* (= *CD*) be its half. Then

*n*2*m*2 + *k*2 =
(*m*2 + *k* )2.

Therefore,

(*nm*)2 + ((*n*2 – *m*2)/2)2
= ((*n*2 + *m*2)/2)2,

which gives the two square numbers (*nm*)2 and ((*n*2 – *m*2)/2)2 whose sum is also a square.

Pythagorean triples

Three numbers x, y, and z where the sum of squares of the first two is the square of the
third form what is now called a Pythagorean triple x : y : z.
This lemma shows that if n and m have the same parity and n > m, then
n and m generate the Pythagorean triple

*nm* : | *n*2 – *m*22 | : | *n*2 + *m*22

It is easy to see that if *x* : *y* : *z*
is a Pythagorean triple, then so is any multiple
*ax* : *ay* : *az*
of it. A Pythagorean triple that is not a multiple of another Pythagorean triple is called a
*primitive* Pythagorean triple. The numbers *n* and *m* are relatively prime if and only if
the Pythagorean triple that they generate is primitive. Thus, when *n* and *m* are relatively
prime odd numbers and *n* > *m,* then a primitive Pythagorean triple is generated.

Here’s a table of a few small Pythagorean triples, indexed by *n* and *m.* Those that
aren’t primitive are colored with a gray background.

| 1 | 3 | 5 | 7 | 9 | 11 | 13
3 | 3 : 4 : 5
5 | 5 : 12 : 13 | 15 : 8 : 17
7 | 7 : 24 : 25 | 21 : 20 : 29 | 35 : 12 : 37
9 | 9 : 40 : 41 | 27 : 36 : 45 | 45 : 28 : 53 | 63 : 16 : 65
11 | 11 : 60 : 61 | 33 : 56 : 65 | 55 : 48 : 73 | 77 : 36 : 85 | 99 : 20 : 101
13 | 13 : 84 : 85 | 39 : 80 : 89 | 65 : 72 : 97 | 91 : 60 : 109 | 117 : 44 : 125 | 143 : 24 : 145
15 | 15 : 112 : 113 | 45 : 108 : 117 | 75 : 100 : 125 | 105 : 88 : 137 | 135 : 72 : 153 | 165 : 52 : 173 | 195 : 28 : 197

About Proposition 29

This proposition constructs a right triangle *ABF* with right angle at *F* so that sides *AB* and *AF* are rational lines commensurable in square only so that *BF* is commensurable to *AB*.

If we let *a*, *b*, and *f* be the lengths of the sides opposite the angles *A*, *B*, and *F*, respectively, that means that *f* 2 = *a*2 + *b*2; *a*2, *b*2, and *c*2 are all rational numbers; *f* /*b* is irrational; and *f* /*a* is rational. That can be accomplished by making the proportion *a* : *b* : *f* = *d* : √(*c*2 – *d*2) : *c*, where *c* and *d* are (whole) numbers such that *c*2 – *d*2 is not a square.

That’s what’s done here, where *c*2 is *CD*, and *d*2 is *DE*.

Use of this proposition

Proposition X.29 is used in X.31 and X.32. Lemma 2 is used in X.30

## See also

- [BookX TOC](BookX.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookX/propX29.html)
