# Proposition I.1

## Statement

To construct an equilateral triangle on a given finite straight line.

## Proof

Let *AB* be the given finite straight line.

![java applet or image](propI1.gif)

It is required to construct an equilateral triangle on the straight line *AB.*

Describe the circle *BCD* with center *A* and radius *AB.* Again describe the circle *ACE* with center *B* and radius *BA.* Join the straight lines *CA* and *CB* from the point *C* at which the circles cut one another to the points *A* and *B.* ([I.Post.3](PostI.3.md), [I.Post.1](PostI.1.md))

Now, since the point *A* is the center of the circle *CDB,* therefore
*AC* equals *AB.* Again, since the point *B* is the center of the circle *CAE,* therefore *BC* equals *BA.* ([I.Def.15](DefI.15.md))

But *AC* was proved equal to *AB,* therefore each of the straight lines *AC* and *BC* equals *AB.*

And things which equal the same thing also equal one another, therefore *AC* also equals *BC.* ([C.N.1](CNI.1.md))

Therefore the three straight lines *AC, AB,* and *BC* equal one another.

Therefore the triangle *ABC* is equilateral, and it has been constructed on the given finite straight line *AB.* ([I.Def.20](DefI.20.md))

Q.E.F.

## Guide

This proposition is a very pleasant choice for the first proposition in the Elements. The construction of the triangle is clear, and the proof that it is an equilateral triangle is evident. Of course, there are two choices for the point C, but either one will do.

Euclid could have chosen proposition [I.4](PropI.4.md) to come first, since it doesn’t logically depend on the previous three, but there are some good reasons for putting I.1 first. For one thing, the *Elements* ends with constructions of the five regular solids in Book XIII, so it is a nice aesthetic touch to begin with the construction of a regular triangle. More important, though, is I.1 is needed in [I.2](PropI.2.md), and that in [I.3](PropI.3.md). Propositions I.2 and I.3 give constructions for moving lines, and I.4, although not logically dependent on I.2 or I.3, does use the concept of superposition which involves, in some sense, moving points and lines.

Marginal references to postulates, definitions, etc.

The abbreviations in the right column refer to postulates, definitions, common notions, and previously proved propositions. Each indicates a justification of a construction or conclusion in a sentence to its left. They are not part of Euclid’s Elements, but it is a tradition to include them as a guide to the reader.

Sometimes the justification is quoted in full as C.N.1 is here, but usually it is left to the reader to determine the justification.

Q.E.F. and Q.E.D. at the ends of proofs

The Q.E.F. at the end of the proof is an abbreviation for the Latin words quod erat faciendum which means “which was to be done.” A few of the propositions, as this one and the next two, solve problems by constructions. These are the ones that end with Q.E.F. (they’re also printed in red here in the listings of propositions for each book.)

The rest of the proofs end with Q.E.D. instead, an abbreviation for *quod erat demonstrandum* which means “which was to be demonstrated.” It’s convenient to have a standard way to indicate the end of a proof. These Latin abbreviations are a bit of an anachronism. It would be less of an anachronism to use abbreviations for the original Greek phrase, or abbreviations for a modern English phrase since the rest of this version of the *Elements* is in English. But by now, Q.E.F. and Q.E.D. are traditional. In recent decades a small square has become common as a symbol to indicate the end of a proof.

Critiques of the proof

It is surprising that such a short, clear, and understandable proof can be so full of holes. These are logical gaps where statements are made with insufficient justification. Since the first proof in the Elements is the one in this proposition, it has received more criticism over the centuries than any other.

**Why does the point *C* exist?**
Near the beginning of the proof, the point *C* is mentioned where the circles are supposed to intersect, but there is no justification for its existence. The only one of Euclid’s postulate that says a point exists the parallel postulate, and that postulate is not relevant here.

Indeed, some postulate is needed for that conclusion, such as “If the sum of the radii of two circles is greater than the line joining their centers, then the two circles intersect.” Such a postulate is also needed in Proposition [I.22](PropI.22.md).

There are models of geometry in which the circles do not intersect. Thus, other postulates not mentioned by Euclid are required. In Book III, Euclid takes some care in analyzing the possible ways that circles can meet, but even with more care, there are missing postulates.

**Why is *ABC* a plane figure?**
After concluding the three straight lines *AC, AB,* and *BC* are equal, what is the justification that they contain a plane figure *ABC*? Recall that a triangle is a plane figure bounded by contained by three lines. These lines have not been shown to lie in a plane and that the entire figure lies in a plane. It is proposition [XI.1](../BookXI/PropXI.1.md) that claims that all parts of a line lie in a plane, and [XI.2](../BookXI/PropXI.2.md) that claims that the entire triangle lie in a plane. Logically, they should precede I.1. The reason they don’t, of course, is that those propositions belong to solid geometry, and plane geometry is developed first in the *Elements,* also, no doubt, plane geometry developed first historically.

**Why does *ABC* contain an equilateral triangle?** Proclus relates that early on there were critiques of the proof and describes that of Zeno of Sidon, an Epicurean philosopher of the early first century B.C.E. (not to be confused with Zeno of Elea famous of the paradoxes who lived long before Euclid), and whose criticisms, Proclus says, were refuted in a book by Posidonius. The critique is sound, however, and the refutation faulty.

Zeno of Sidon criticized the proof because it was not shown that the sides do not meet before they reach the vertices. Suppose *AC* and *BC* meet at *E* before they reach *C,* that is, the straight lines *AEC* and *BEC* have a common segment *EC.* Then they would contain a triangle *ABE* which is not equilateral, but isosceles. Zeno recognized that in order to destroy his counterexample it was necessary to assume that straight lines cannot have a common segment. Proclus relates a supposed proof of that statement, the same one found in proposition [XI.1](../BookXI/PropXI.1.md), but it is faulty. Proclus and Posidonius quoted properties of lines and circles that were never proven and never explicitly assumed as postulates. | ![java applet or image](propI1a.gif)

The possibilities that haven’t been excluded are much more numerous than Zeno’s example. The sides could meet numerous times and the region they contain could look like a necklace of bubbles. What needs to be shown (or assumed as a postulate) is that two infinitely extended straight lines can meet in at most one point.

Use of Proposition 1

The construction in this proposition is directly used in propositions
I.2, I.9, I.10, I.11, XI.11, and XI.22.

## See also

- [BookI TOC](BookI.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookI/propI1.html)
