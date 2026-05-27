# Proposition II.14

## Statement

To construct a square equal to a given rectilinear figure.

## Proof

Let *A* be the given rectilinear figure.

It is required to construct a square equal to the rectilinear figure *A.*

[I.45](../BookI/PropI.45.md)
Construct the rectangular parallelogram *BD* equal to the rectilinear figure *A.*

![java applet or image](propII14.gif)

Then, if *BE* equals *ED,* then that which was proposed is done, for a square *BD* has been constructed equal to the rectilinear figure *A.*

But, if not, one of the straight lines *BE* or *ED* is greater.

[I.3](../BookI/PropI.3.md),
[I.10](../BookI/PropI.10.md)
Let *BE* be greater, and produce it to *F.* Make *EF* equal to *ED,* and bisect *BF* at *G.*

[I.Def.18](../BookI/DefI.15.md)
Describe the semicircle *BHF* with center *G* and radius one of the straight lines *GB* or *GF.* Produce *DE* to *H,* and join *GH.*

[II.5](PropII.5.md)
Then, since the straight line *BF* has been cut into equal segments at *G* and into unequal segments at *E,* the rectangle *BE* by *EF* together with the square on *EG* equals the square on *GF.*

But *GF* equals *GH,* therefore the rectangle *BE* by *EF* together with the square on *GE* equals the square on *GH.*

[I.47](../BookI/PropI.47.md)
But the sum of the squares on *HE* and *EG* equals the square on *GH,* therefore the rectangle *BE* by *EF* together with the square on *GE* equals the sum of the squares on *HE* and *EG.*

Subtract the square on *GE* from each. Therefore the remaining rectangle *BE* by *EF* equals the square on *EH.*

But the rectangle *BE* by *EF* is *BD,* for *EF* equals *ED,* therefore the parallelogram *BD* equals the square on *HE.*

And *BD* equals the rectilinear figure *A.*

Therefore the rectilinear figure *A* also equals the square which can be described on *EH.*

Therefore a square, namely that which can be described on *EH,* has been constructed equal to the given rectilinear figure *A.*

Q.E.F.

## Guide

The construction of a square equal to a given rectilinear figure is short as described in the proof. The verification that this construction works is also short with the help of Proposition II.5 and Proposition I.47, the Pythagorean theorem. First, Prop. II.5 allows us to convert the rectangle, BE by ED, into the difference of two squares, GF2 – GE2. Note that GF equals GH, the hypotenuse of a right triangle GHE. Using I.47 we can replace the difference of two squares, GH2 – GE2, by the single square, EH2. Thus, the original rectangle equals the square EH2.

Quadrature of rectilinear figures

This proposition finishes the quadrature of rectilinear figures. The narrow meaning of the word “quadrature” is to find a square with the same area of a given figure, also called “squaring” the figure. In a broader sense, quadrature means finding the area of a given figure.

Proposition [I.45](../BookI/PropI.45.md) on application of areas of rectilinear figures allows us to replace the figure under question with a rectangle of the same area. Now, the semicircle construction in this proposition finds what is called the mean proportional between the sides of the rectangle. If the sides of the rectangle are denoted *a* and *b,* then the mean proportional *x* between them satisfies the proportion *a* : *x* = *x* : *b,* and that’s equivalent to an equality of areas *ab* = *x*2, that is to say, the square on this mean proportional has the same area as the rectangle. Thus, any rectilinear figure can be squared.

This result is an end in itself. It is not used in the rest of the *Elements.*

There is another proof of this proposition that is based on similar triangles. Referring to the figure in the proposition, draw lines *BH* and *BF,* and you’ll see three similar right triangles: *BFH, BHE,* and *HGE.* From their similarity it follows that *BE* : *EH* = *EH* : *EF.* That says *EH* is the required mean proportional.

Proportions aren’t developed until Book V, and similar triangles aren’t mentioned until Book VI. So in order to complete the theory of quadrature of rectilinear figures early in the *Elements,* Euclid chose a different proof that doesn’t depend on similar triangles. Note that this same result appears in the garb of proportions in Proposition [VI.13](../BookVI/PropVI.13.md). Also in Book VI, Proposition [VI.17](../BookVI/PropVI.17.md) shows that the square on the mean proportional equals the rectangle on the two straight lines.

Squaring the circle

What about circles and other shapes? The general theory of circles is treated in Book III, but there are no propositions about the areas of circles until book XII. Proposition XII.2 says the areas of circles are proportional to the squares on their diameters. That allows the area of two circles to be compared, but it doesn’t answer the question “what’s the area of this circle?” in the same way that this proposition does for rectilinear figures. That would require finding a square equal to a given circle.

This problem of quadrature of the circle was one of three famous problems that goes back at least to the time of Anaxagoras, about 150 years before Euclid. It is equivalent to constructing a line segment of length *π* (relative to a unit length). This problem was solved by ancient Greek geometers but not by means of the Euclidean tools of straightedge and compass; higher curves were required. In fact, by the time of Pappus it was believed that the circle could not be squared using only straightedge, compass, and, furthermore, couldn’t be squared even with the help of the conic sections (parabola, hyperbola, and ellipse). But the ancient Greeks had no mathematical proof that it could not be squared.

That the circle could not be squared with Euclidean tools was not shown until 1882 when Lindemann proved that *π* is a transcendental number.

## See also

- [BookII TOC](BookII.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookII/propII14.html)
