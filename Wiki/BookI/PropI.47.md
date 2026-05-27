# Proposition I.47

## Statement

In right-angled triangles the square on the side opposite the right angle equals the sum of the squares on the sides containing the right angle.

## Proof

Let *ABC* be a right-angled triangle having the angle *BAC* right.
I say that the square on *BC* equals the sum of the squares on *BA* and *AC.*

Describe the square *BDEC* on *BC,* and the squares *GB* and *HC* on *BA* and *AC.* Draw *AL* through *A* parallel to either *BD* or *CE,* and join *AD* and *FC.* ([I.46](PropI.46.md), [I.31](PropI.31.md), [I.Post.1](PostI.1.md))

![](propI47.gif)

Since each of the angles *BAC* and *BAG* is right, it follows that with a straight line *BA,* and at the point *A* on it, the two straight lines *AC* and *AG* not lying on the same side make the adjacent angles equal to two right angles, therefore *CA* is in a straight line with *AG.* ([I.Def.22](DefI.22.md), [I.14](PropI.14.md))

For the same reason *BA* is also in a straight line with *AH.*

Since the angle *DBC* equals the angle *FBA,* for each is right, add the angle *ABC* to each, therefore the whole angle *DBA* equals the whole angle *FBC.* ([I.Def.22](DefI.22.md), [I.Post.4](PostI.4.md), [C.N.2](CNI.1.md))

Since *DB* equals *BC,* and *FB* equals *BA,* the two sides *AB* and *BD* equal the two sides *FB* and *BC* respectively, and the angle *ABD* equals the angle *FBC,* therefore the base *AD* equals the base *FC,* and the triangle *ABD* equals the triangle *FBC.* ([I.Def.22](DefI.22.md), [I.4](PropI.4.md))

Now the parallelogram *BL* is double the triangle *ABD,* for they have the same base *BD* and are in the same parallels *BD* and *AL.* And the square *GB* is double the triangle *FBC,* for they again have the same base *FB* and are in the same parallels *FB* and *GC.*

Therefore the parallelogram *BL* also equals the square *GB.* ([I.41](PropI.41.md))

Similarly, if *AE* and *BK* are joined, the parallelogram *CL* can also be proved equal to the square *HC.* Therefore the whole square *BDEC* equals the sum of the two squares *GB* and *HC.*

And the square *BDEC* is described on *BC,* and the squares *GB* and *HC* on *BA* and *AC.* ([C.N.2](CNI.1.md))

Therefore the square on *BC* equals the sum of the squares on *BA* and *AC.*

Therefore *in right-angled triangles the square on the side opposite the right angle equals the sum of the squares on the sides containing the right angle..*

Q.E.D.

## Guide

This proposition is generalized in VI.31 to arbitrary similar figures placed on the sides of the triangle ABC. If the rectilinear figures on the sides of the triangle are similar, then the figure on the hypotenuse is the sum of the other two figures.

A bit of history
This proposition, I.47, is often called the Pythagorean theorem, called so by Proclus and others centuries after Pythagoras and even centuries after Euclid. The statement of the proposition was very likely known to the Pythagoreans if not to Pythagoras himself. The Pythagoreans and perhaps Pythagoras even knew a proof of it. But the knowledge of this relation was far older than Pythagoras.

More than a millennium before Pythagoras, the Old Babylonians (ca. 1900-1600 B.C.E) used this relation to solve geometric problems involving right triangles. Moreover, the tablet known as Plimpton 322 shows that the Old Babylonians could construct all the so-called Pythagorean triples, those triples of numbers *a, b,* and *c* such that *a*2 + *b*2 = *c*2 which describe triangles with integral sides. (The smallest of these is 3, 4, 5.) For more on Pythagorean triples, see
[X.29.Lemma 1](../BookX/PropX.29.md).

The hypotenuse diagram in the *Zhou bi suan jing*

The rule for computing the hypotenuse of a right triangle was well known in ancient China. It is used in the Zhou bi suan jing, a work on astronomy and mathematics compiled during the Han period, and in the later important mathematical work Jiu zhang suan shu [Nine Chapters] to solve right triangles.

The *Zhou bi* includes a very interesting diagram known as the hypotenuse diagram.
![xian tu](propI47a.gif)
This diagram may not have been in the original text but added by its primary commentator Zhao Shuang sometime in the third century C.E. A particular case of this proposition is illustrated by this diagram, namely, the 3-4-5 right triangle.

Place four 3 by 4 rectangles around a 1 by 1 square. A 7 by 7 square results. The four diagonals of the rectangles bound a tilted square as illustrated. The area of tilted square is 49 minus 4 times 6 (the 6 is the area of one right triangle with legs 3 and 4), which is 25. Therefore the tilted square is 5 by 5, and the diagonal of the original 3 by 4 rectangles is 5.

Zhao Shuang referred to the hypotenuse figure in a general way. He described all the ways the sides, the hypotenuse, and their squares can be found in terms of each other.

The *Zhou bi* has recently been translated into English with an excellent commentary. See *Astronomy and mathematics in ancient China: the* Zhou bi suan jing, by Christopher Cullin, Cambridge University Press, 1996.

Alternate methods of proof
According to Proclus, the specific proof of this proposition given in the Elements is Euclid’s own. It is likely that older proofs depended on the theories of proportion and similarity, and as such this proposition would have to wait until after Books V and VI where those theories are developed. It appears that Euclid devised this proof so that the proposition could be placed in Book I.

Euclid presents a proof based on proportion and similarity in the [lemma](../BookX/PropX.33.md) for proposition X.33. Compare it, summarized here, to the proof in I.47.

Let *ABC* be a right-angled triangle with a right angle at *A.* Draw *AM* perpendicular to *BC.* According to [VI.8](../BookVI/PropVI.8.md), the triangles *ABM* and *AMC* are similar both to the whole *ABC* and to one another. (VI.8 concludes the triangles are similar after showing they have the same angles, see [VI.4](../BookVI/PropVI.4.md).) Since triangle *ABC* is similar to triangle *ABD,* therefore, by the definition of similarity [VI.Def.1](../BookVI/DefVI.1.md), *CB* is to *BA* as *BA* is to *BM.* | ![java applet or image](../bookI/propI47b.gif)

Next [VI.17](../BookVI/PropVI.17.md) converts this proportion to a statement about areas, namely, the rectangle *CB* by *BM* (which is the parallelogram *BL* in the proof of I.47) equals the square on *AB.* For the same reason the rectangle *BC* by *CM* (which is the parallelogram *CL* in the proof of I.47) also equals the square on *AC.* Therefore the sum of the two rectangles *CB* by *BM* and *BC* by *CM,* which is the square on *BC,* equals the sum of the squares on *AC* and *BC.* Q.E.D.

(Actually, the final sentence is not part of the lemma, probably because Euclid moved that statement to the first Book as I.47.)

So, although Euclid’s proof in I.47 may be more complicated than some others, we can see how it well it corresponds to a simpler proof that depends on the theories of proportion and similarity.

Generalizations of I.47

Propositions [II.12](../BookII/PropII.12.md) and [II.13](../BookII/PropII.13.md) consider triangles other than right triangles. In II.12 the right angle is replaced by an obtuse angle, while in II.13 the right angle is replaced by an acute angle. The resulting statements are actually geometric forms of the law of cosines.

Proposition [VI.31](../BookVI/PropVI.31.md) generalizes the figures that can be placed on the sides of the right triangle to any three similar figures instead of the three squares here in I.47.

Use of this proposition

This proposition is used in the next one, which its converse, in propositions II.9 through II.14 in Book II, and several propositions in the rest of the books on geometry.

## See also

- [BookI TOC](BookI.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookI/propI47.html)
