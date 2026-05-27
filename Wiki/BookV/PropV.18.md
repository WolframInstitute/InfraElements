# Proposition V.18

## Statement

If magnitudes are proportional taken separately, then they are also proportional taken jointly.

## Proof

Let *AE, EB, CF,* and *FD* be magnitudes proportional taken separately, so that *AE* is to *EB* as *CF* is to *FD.* ([V.Def.15](DefV.14.md))

I say that they are also proportional taken jointly, that is, *AB* is to *BE* as *CD* is to *FD.* ([V.Def.14](DefV.14.md))

For, if *CD* is not to *DF* as *AB* is to *BE,* then *AB* is to *BE* as *CD* is either to some magnitude less than *DF* or to a greater.

First, let it be in that ratio to a less magnitude *DG.*

![java applet or image](propV18.gif)

Then, since *AB* is to *BE* as *CD* is to *DG,* they are magnitudes proportional taken jointly, so that they are also proportional taken separately. Therefore *AE* is to *EB* as *CG* is to *GD.* ([V.17](PropV.17.md))

But also, by hypothesis, *AE* is to *EB* as *CF* is to *FD.* Therefore *CG* is to *GD* as *CF* is to *FD.* ([V.11](PropV.11.md))

But the first *CG* is greater than the third *CF,* therefore the second *GD* is also greater than the fourth *FD.* ([V.14](PropV.14.md))

But it is also less, which is impossible. Therefore *AB* is to *BE* as *CD* is not to a less magnitude than *FD.*

Similarly we can prove that neither is it in that ratio to a greater, it is therefore in that ratio to *FD* itself.

Therefore, *if magnitudes are proportional taken separately, then they are also proportional taken jointly.*

Q.E.D.

## Guide

This proposition is the converse of the last one. It says that if w : x = y : z, then (w + x):x = (y + z):z. As in the last proposition, two of the magnitudes w and x can be of one kind while the other two y and z are of another.

On the existence of fourth proportionals

At the beginning of this proof we have, paraphrased:

If *CD* : *DF* does not equal *AB* : *BE,* then *AB* : *BE* = *CD* : *DG* where *DG* is some magnitude greater or less than *DF.*

Given the other three magnitudes, a fourth proportional DG is assumed. It is not asserted that the fourth proportional can be constructed; it is only hypothetical. This is the beginning of a proof by contradiction.

This technique of assuming the existence of a fourth proportional to derive a contradiction is also used in Book XII to prove various proportionalities of areas and volumes, for example, in proposition [XII.2](../BookXII/PropXII.2.md) which shows circles are proportional to the squares on their diameters. Eudoxus, who developed the techniques of both Books V and XII, or Euclid, or both of them, accepted this technique as valid.

The problem is: do fourth proportionals exist? They certainly can’t be constructed in all cases. The problems of doubling a cube, squaring a circle, and trisecting an angle cannot be solved by plane Euclidean methods, and they all involve inconstructable fourth proportionals. Take doubling a cube for example. If *C* is a cube with an edge *A,* then the inconstructable edge *B* of a cube with double the volume of *C* is the fourth proportional in *C* : (*C*+*C*) = *A* : *B.*

Is there a difference between existence and constructibility? Constructibility is a fairly clear concept since there are postulates for what can be constructed. There are no postulates for things that exist but aren’t constructed, but the existence of a fourth proportional is a good candidate for a such a postulate.

There is a similar situation in modern mathematics with the axiom of choice for set theory. That axiom says that in certain situations there is at least one set satisfying certain criteria. It does not construct anything in the usual sense of "construct," and it doesn’t even specify a particular set. Although it is useful in many situations, mathematicians prefer not to use it unless it’s necessary.

For this proposition, the assumption of the existence of fourth proportionals is unnecessary as the following alternate proof shows.

An alternate proof

Proposition: If w : x = y : z, then (w + x):x = (y + z):z.

Proof: Suppose *w* : *x* = *y* : *z.* Let *n* and *m* be any numbers. Either *n* < *m* or not.

Case 1: *n* < *m.*
Suppose *n*(*w* + *x*) >=< *mx.*
Subtract *nx* to get
*nw* >=< (*m* – *n*)*x.*
But *w* : *x* = *y* : *z,* so
*ny* >=< (*m* – *n*)*z.*
Add *nz* to get *n*(*y* + *z*) >=< *mz.*

Case 2: *n* is not less than *m.*
Then both *n*(*w* + *x*) > *mx,* and
*n*(*y* + *z*) > *mz.*

In any case *n*(*w* + *x*) >=< *mx* implies *n*(*y* + *z*) >=< *mz.*
Therefore (*w* + *x*):*x* = (*y* + *z*):*z.* Q.E.D.

Use of this proposition

This proposition is used in proposition V.24 and a few in Books VI, X, XII, and XIII.

## See also

- [BookV TOC](BookV.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookV/propV18.html)
