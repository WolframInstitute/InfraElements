# Proposition VI.31

## Statement

In right-angled triangles the figure on the side opposite the right angle equals the sum of the similar and similarly described figures on the sides containing the right angle.

## Proof

Let *ABC* be a right-angled triangle having the angle *BAC* right.

I say that the figure on *BC* equals the sum of the similar and similarly described figures on *BA* and *AC.*

[I.12](../BookI/PropI.12.md)
Draw the perpendicular *AD.*

![java applet or image](propVI31.gif)

[VI.8](PropVI.8.md)
Then, since in the right-angled triangle *ABC, AD* has been drawn from the right angle at *A* perpendicular to the base *BC,* therefore the triangles *DBA* and *DAC* adjoining the perpendicular are similar both to the whole *ABC* and to one another.

[VI.Def.1](DefVI.1.md)
And, since *ABC* is similar to *DBA,* therefore *BC* is to *BA* as *BA* is to *BD.*

[VI.19,Cor](PropVI.19.md)
And, since three straight lines are proportional, the first is to the third as the figure on the first is to the similar and similarly described figure on the second.

Therefore *BC* is to *BD* as the figure on *BC* is to the similar and similarly described figure on *BA.*

[V.24](../BookV/PropV.24.md)
For the same reason also, *BC* is to *CD* as the figure on *BC* is to that on *CA,* so that, in addition, *BC* is to the sum of *BD* and *DC* as the figure on *BC* is to the sum of the similar and similarly described figures on *BA* and *AC.*

But *BC* equals the sum of *BD* and *DC,* therefore the figure on *BC* equals the sum of the similar and similarly described figures on *BA* and *AC.*

Therefore, *in right-angled triangles the figure on the side opposite the right angle equals the sum of the similar and similarly described figures on the sides containing the right angle.*

Q.E.D.

## Guide

This proposition is a generalization of I.47 where the squares in I.47 are replaced by any similar rectilinear figures.

Hippocrates’ quadrature of lunes

Proclus says that this proposition is Euclid’s own, and the proof may be his, but
the result, if not the proof, was known long before Euclid, at least in the time
of Hippocrates a century before Euclid.

The broad problem Hippocrates was investigating was that of quadrature of a circle, also called squaring a circle, which is to find a square (or any other polygon) with the same area as a given
circle. Hippocrates did not solve that problem, but he did solve a related one involving lunes. A *lune* (also called a *crescent*) is a region of nonoverlap of two intersecting circles.
Hippocrates did not succeed in squaring an arbitrary lune, but he did succeed in a couple special cases. Here is a summary of the simplest case.

Draw a square *ABCD* with diameters *AC* and *BD* meeting at *E.* Circumscribe a semicircle *AGBHC* about the right isosceles triangle *ABC.* Draw the arc *AFC* from *A* to *C* of a circle with center *D* and radius *DA.* Hippocrates finds the area of the lune formed between the semicircle *AGBHC* and the arc *AF* as follows. Note that there are three segments of circles in the diagram; two of them are small, namely, *AGB* with base *AB,* and *BHC* with base *BC,* and one is large, namely, *AFC* with base *AC.* The first two are congruent, and the third is similar to them since all three are segments in quarters of circles. | ![Hippocrates' lune](propVI31a.gif)

Hippocrates then uses a version of this proposition VI.31—generalized so the figures don’t have to be rectilinear but may have curved sides— to conclude that the sum of the two small segments, *AGB* + *BHC,* equals the large segment *AFC,* since the bases of the small segments are sides of a right triangle while the base of the large segment is the triangle’s hypotenuse.

Therefore, the lune, which is the semicircle minus the large segment, equals the semicircle minus the sum of the small segments. But the semicircle minus the sum of the small segments is just the right triangle *ABC.* Thus, a rectilinear figure (the triangle) has been found equal to the lune, as required.

Note that at Hippocrates’ time, Eudoxus’ theory of proportion had not been developed, so the understanding of the theory of similar figures (Book V) was not as
complete as it was after Eudoxus. Also, Eudoxus’ principle of exhaustion (see Book XI and proposition [X.1](../BookX/PropX.1.md)) for finding areas
of curved figures was still to come, so the concept of area of curved figures was on shaky ground, too. Such a situation is common in mathematics—mathematics advances into new territory long
before the foundations of mathematics are developed to logically justify those advances.

## See also

- [BookVI TOC](BookVI.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookVI/propVI31.html)
