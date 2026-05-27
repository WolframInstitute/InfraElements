# Proposition IV.4

## Statement

To inscribe a circle in a given triangle.

## Proof

Let *ABC* be the given triangle.

It is required to inscribe a circle in the triangle *ABC.*

![IV.4](propIV4.gif)

[I.9](../BookI/PropI.9.md)

[I.12](../BookI/PropI.12.md)
Bisect the angles *ABC* and *ACB* by the straight lines *BD* and *CD,* and let these meet one another at the point *D.* Draw *DE, DF,* and *DG* from *D* perpendicular to the straight lines *AB, BC,* and *CA.*

[I.26](../BookI/PropI.26.md)
Now, since the angle *ABD* equals the angle *CBD,* and the right angle *BED* also equals the right angle *BFD, EBD* and *FBD* are two triangles having two angles equal to two angles and one side equal to one side, namely that opposite one of the equal angles, which is *BD* common to the triangles, therefore they will also have the remaining sides equal to the remaining sides, therefore *DE* equals *DF.*

For the same reason *DG* also equals *DF.*

Therefore the three straight lines *DE, DF,* and *DG* equal one another. Therefore the circle described with center *D* and radius one of the straight lines *DE, DF,* or *DG* also passes through the remaining points and touches the straight lines *AB, BC,* and *CA,* because the angles at the points *E, F,* and *G* are right.

[III.16](../BookIII/PropIII.16.md)

IV.Def.5
For, if it cuts them, the straight line drawn at right angles to the diameter of the circle from its end will be found to fall within the circle, which was proved absurd, therefore the circle described with center *D* and radius one of the straight lines *DE, DF,* or *DG* does not cut the straight lines *AB, BC,* and *CA* Therefore it touches them, and is the circle inscribed in the triangle *ABC.*

Let it be inscribed as *FGE.*

Therefore the circle *EFG* has been inscribed in the given triangle *ABC.*

Q.E.F.

## Guide

It is easy to supply the missing argument that the angle bisectors BD and CD do meet.

Incircles and excircles

This circle inscribed in a triangle has come to be known as the *incircle* of the triangle, its center the *incenter* of the triangle, and its radius the *inradius* of the triangle.

The incircle is a circle tangent to the three lines *AB, BC,* and *AC.* If these three lines are extended, then there are three other circles also tangent to them, but outside the triangle. They are called the *excircles.*

The points on the internal angle bisector *AD* are equidistant from the two sides of the triangle *AB* and *AC.* The line *KL* is perpendicular to *AD* at *A,* and the points on it are also equidistant from the extended sides *AB* and *AC.* The line *B'C'* is called the *external angle bisector* at *A.* Whereas the incenter *D* lies at the confluence of the three internal angle bisectors, the excenter *B'* lies at the confluence of two external angle bisectors *AB'* and *CB'* and one internal angle bisector *BB'.* Likewise for the other two excenters *A'* and *C'.*

(Drag around the points *A*, *B*, and *C* to see how the figure changes.)

![Incircle and excircles](propIV4a.gif)

Heron’s formula

![Heron's formula](propIV4b.gif) | Heron of Alexandria (first century C.E.) was an important Greek mathematician who wrote, among other things, a commentary on the *Elements* which is lost now but was known to Proclus and an-Nairizi. In Heron’s *Metrica,* which was rediscovered in 1896, there appears a proof of what is called Heron’s formula. It states that the area of a triangle is the square root of *s*(*s* – *a*)(*s* – *b*)(*s* – *c*) where *a* = *BC, b* = *AC,* and *c* = *AB,* the sides of the triangle, and *s* is the semiperimeter (*a* + *b* + *c*)/2. Archimedes may have known this formula, but but we don’t have his proof. Heath gives Heron’s complete proof, but here we’ll just look at the first part that involves the incircle. Let *D* be the incenter of the triangle *ABC,* and let *DE, DF,* and *DG* be perpendicular lines drawn to the sides as in Euclid’s proof. These three lines are radii of the incircle, and therefore have length *r,* the inradius. The triangle *ABD* has base *AB* and height *r,* so its area is *r AB*/2. Likewise, the area of triangle *BCD* is *r BC*/2, and the area of triangle *CAD* is *r CA*/2. Adding these together we find the area of triangle *ABC* is *r* (*AB* + *BC* + *CA*)/2. Therefore we have Area(*ABC*) = *rs* an interesting result in itself.

We’ll leave Heron’s proof now and consider the corresponding statement for excircles.

Now let *A'* be the excenter on the bisector of the internal angle at *A.* Let *A'E', A'F',* and *A'G'* be the perpendiculars drawn from *A'* to the sides of the triangle. They are radii of the excircle of length *rA.* Triangle *ABA'* has base *AB* and height *A'E',* so its area is *rA AB*/2. Likewise, the area of triangle *BCA'* is *rA BC*/2, and the area of triangle *CAA'* is *rA CA*/2. Triangle *ABC* is the sum of triangles *ABA'* and *ACA'* minus triangle *BCA',* so its area is *rA* (*AB* + *AC* – *CA*)/2 which equals *rA*(*s* – *A*). From the other excircles we get two more equations. We then have Area(*ABC*) = *rs* = *rA*(*s* – *A*) = *rB*(*s* – *B*) = *rC*(*s* – *C*). There are other relationships among these radii, for instance, 1/*r* = 1/*rA* + 1/*rB* + 1/*rC,* but let’s stop here to go on to the circumcircle of a triangle. | ![java applet or image](propIV4c.gif)

## See also

- [BookIV TOC](BookIV.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookIV/propIV4.html)
