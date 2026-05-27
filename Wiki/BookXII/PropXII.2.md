# Proposition XII.2

## Statement

Circles are to one another as the squares on their diameters.

## Proof

Let *ABCD* and *EFGH* be circles, and let *BD* and *FH* be their diameters.

I say that the circle *ABCD* is to the circle *EFGH* as the square on *BD* is to the square on *FH.*

![java applet or image](propXII2.gif)

For, if the square on *BD* is not to the square on *FH* as the circle *ABCD* is to the circle *EFGH,* then as the square on *BD* is to the square on *FH,* the circle *ABCD* is either to some less area than the circle *EFGH,* or to a greater area.

First, let it be in that ratio to a less area *S.*

[IV.6](../BookIV/PropIV.6.md)

[III.17](../BookIII/PropIII.17.md)
Inscribe the square *EFGH* in the circle *EFGH.* Then the inscribed square is greater than the half of the circle *EFGH,* for if through the points *E, F, G,* and *H* we draw tangents to the circle, then the square *EFGH* is half the square circumscribed about the circle, and the circle is less than the circumscribed square, hence the inscribed square *EFGH* is greater than the half of the circle *EFGH.*

Bisect the circumferences *EF, FG, GH,* and *HE* at the points *K, L, M,* and *N.* Join *EK, KF, FL, LG, GM, MH, HN,* and *NE.*

[III.17](../BookIII/PropIII.17.md)
Therefore each of the triangles *EKF, FLG, GMH,* and *HNE* is also greater than the half of the segment of the circle about it, for if through the points *K, L, M,* and *N* we draw tangents to the circle and complete the parallelograms on the straight lines *EF, FG, GH,* and *HE,* then each of the triangles *EKF, FLG, GMH,* and *HNE* is half of the parallelogram about it, while the segment about it is less than the parallelogram, hence each of the triangles *EKF, FLG, GMH,* and *HNE* is greater than the half of the segment of the circle about it.

Thus, by bisecting the remaining circumferences and joining straight lines, and by doing this repeatedly, we shall leave some segments of the circle which will be less than the excess by which the circle *EFGH* exceeds the area *S.*

[X.1](../BookX/PropX.1.md)
For it was proved in the first theorem of the tenth book that if two unequal magnitudes are set out, and if from the greater there is subtracted a magnitude greater than the half, and from that which is left a greater than the half, and if this is done repeatedly, then there will be left some magnitude which is less than the lesser magnitude set out.

Let segments be left such as described, and let the segments of the circle *EFGH* on *EK, KF, FL, LG, GM, MH, HN,* and *NE* be less than the excess by which the circle *EFGH* exceeds the area *S.*

Therefore the remainder, the polygon *EKFLGMHN,* is greater than the area *S.*

Now inscribe in the circle *ABCD* the polygon *AOBPCQDR* similar to the polygon *EKFLGMHN.*

[XII.1](PropXII.1.md)
Therefore the square on *BD* is to the square on *FH* as the polygon *AOBPCQDR* is to the polygon *EKFLGMHN.*

[V.11](../BookV/PropV.11.md)

[V.16](../BookV/PropV.16.md)
But the square on *BD* is to the square on *FH* as the circle *ABCD* to the area *S,* therefore the circle *ABCD* is to the area *S* as the polygon *AOBPCQDR* is to the polygon *EKFLGMHN.* Therefore, alternately the circle *ABCD* is to the polygon inscribed in it as the area *S* is to the polygon *EKFLGMHN.*

But the circle *ABCD* is greater than the polygon inscribed in it, therefore the area *S* is also greater than the polygon *EKFLGMHN.* But it is also less, which is impossible.

Therefore the square on *BD* is to the square on *FH* not as the circle *ABCD* is to any area less than the circle *EFGH.*

Similarly we can prove that the circle *EFGH* is to any area less than the circle *ABCD* not as the square on *FH* is to the square on *BD.*

I say next that neither is the circle *ABCD* to any area greater than the circle *EFGH* as the square on *BD* is to the square on *FH.*

For, if possible, let it be in that ratio to a greater area *S.* Therefore, inversely the square on *FH* is to the square on *DB* as the area *S* is to the circle *ABCD.*

Lemma

[V.11](../BookV/PropV.11.md)
But the area *S* is to the circle *ABCD* as the circle *EFGH* is to some area less than the circle *ABCD,* therefore the square on *FH* is to the square on *BD* as the circle *EFGH* is to some area less than the circle *ABCD,* which was proved impossible. Therefore the square on *BD* is to the square on *FH* not as the circle *ABCD* to any area greater than the circle *EFGH.*

And it was proved that neither is it in that ratio to any area less than the circle *EFGH,* therefore the square on *BD* is to the square on *FH* as the circle *ABCD* is to the circle *EFGH.*

Q.E.D.

## Guide

In the last proposition it was shown that similar polygons inscribed in circles are proportional to the squares on the diameters of the circles. By approximating circles closely by similar polygons, the proportion is carried over to the circles.

The form of the proof is a double proof by contradiction. There are three cases when comparing the ratio of the squares *BD* : *FH* to the ratio of the circles *ABCD* : *EFGH.* One case is that the ratio of the squares *BD* : *FH* equals *ABCD* : *S* where *S* is some area less than circle *EFGH.* Most of the proof is spent refuting this case. The second case is that the ratio of the squares *BD* : *FH* equals *ABCD* : *S* where this time *S* is some area greater than circle *EFGH.* This is inverted to a statement that the ratio of the squares *FH* : *BD* equals *EFGH* to some area less than circle *ABCD,* which is the first case already already shown not to occur. That leaves only the third case that the ratio of the squares *BD* : *FH* equals the ratio of the circles *ABCD* : *EFGH.* (Actually, there is a gap in the proof at this last step; it was never shown that these are the only three cases. It may be true that there are three cases, that the ratio of the squares is greater, less, or equal to the ratio of the circles, but the three cases of in the proof are one step removed from these three cases.)

Approximation by polygons

The first case is disposed of by approximating the circles by very close polygons. To begin with a square EFGH is inscribed in the circle EFGH, and it is shown that the remainder is less than half the circle. Next the circumferences are bisected to construct an octagon EKFLGMHN, and the remainder of the circle is shown to be less than half the old remainder. Continuing, polygons of 16, 32, 64, etc., sides are constructed and each one leaves a remainder less than half the previous remainder.

Now the circle *EFGH* exceeds the area *S* by some finite amount, and by the principle of proposition [X.1](../BookX/PropX.1.md), at some stage mentioned above, the remainder will be less than the excess of circle *EFGH* over *S.* For the rest of the proof, that stage is taken as that of the polygon *EKFLGMHN,* that is, circle

*EFGH* – polygon *EKFLGMHN* < circle *EFGH* – area *S,*

and so area S < polygon EKFLGMHN.

The similar polygon *AOBPCQDR* is inscribed in the other circle *ABCD.* Then

circle *ABCD* : area *S* | = *BC*2 : *FH*2
| = polygon *AOBPCQDR* : polygon *EKFLGMHN.*

Alternately, circle *ABCD* : polygon *AOBPCQDR* = area *S* : polygon *EKFLGMHN.* But circle *ABCD* > polygon *AOBPCQDR,* so area *S* > polygon *EKFLGMHN,* contradicting the statement above that the area *S* is less than the polygon.

Principle of exhaustion

The approximation of a figure by a sequence of figures inside it is sometimes called the “principle of exhaustion.” The important point of this principle is that the sequence of approximations can be made so that the difference between the original figure and the inscribed figure decreases by at least half at each step of the sequence.

This principle is used in several later propositions in this book. Proposition [XII.5](PropXII.5.md) uses it to show that pyramids of the same height with triangular bases are proportional to their bases. The pyramids are approximated by a union of similar triangular prisms. Proposition [XII.10](PropXII.10.md) uses the principle of exhaustion to show that a cone inscribed in a cylinder is one-third of the cylinder. The cone is approximated by inscribed pyramids while the cylinder is approximated by inscribed prisms. Pyramids inscribed in cones are similarly used in [XII.11](PropXII.11.md) and [XII.12](PropXII.12.md). Finally, the principle of exhaustion is used in proposition [XII.18](PropXII.18.md) to show spheres are to one another in triplicate ratio of their diameters. There the spheres are exhausted by inscribed polyhedra.

## See also

- [BookXII TOC](BookXII.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookXII/propXII2.html)
