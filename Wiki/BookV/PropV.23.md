# Proposition V.23

## Statement

If there are three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then they are also in the same ratio *ex aequali.*

## Proof

[V.Def.18](DefV.17.md)
Let there be three magnitudes *A, B,* and *C,* and others *D, E,* and *F,* equal to them in multitude, which, taken two and two together, are in the same proportion, and let the proportion of them be perturbed, so that *A* is to *B* as *E* is to *F,* and *B* is to *C* as *D* is to *E.*

I say that *A* is to *C* as *D* is to *F.*

Take equimultiples *G, H,* and *K* of *A, B,* and *D,* and take other, arbitrary, equimultiples *L, M,* and *N* of *C, E,* and *F.*

![java applet or image](propV23.gif)

[V.15](PropV.15.md)
Then, since *G* and *H* are equimultiples of *A* and *B,* and parts have the same ratio as their multiples, therefore *A* is to *B* as *G* is to *H.*

[V.11](PropV.11.md)
For the same reason *E* is to *F* as *M* is to *N.* And *A* is to *B* as *E* is to *F,* therefore *G* is to *H* as *M* is to *N.*

([V.16](PropV.16.md))
Next, since *B* is to *C* as *D* is to *E,* alternately, also, *B* is to *D* as *C* is to *E.*

[V.15](PropV.15.md)
And, since *H* and *K* are equimultiples of *B* and *D,* and parts have the same ratio as their equimultiples, therefore *B* is to *D* as *H* is to *K.*

[V.11](PropV.11.md)
But *B* is to *D* as *C* is to *E,* therefore also, *H* is to *K* as *C* is to *E.*

[V.15](PropV.15.md)
Again, since *L* and *M* are equimultiples of *C* and *E,* therefore *C* is to *E* as *L* is to *M.*

[V.11](PropV.11.md),
([V.16](PropV.16.md))
But *C* is to *E* as *H* is to *K,* therefore also, *H* is to *K* as *L* is to *M,* and, alternately, *H* is to *L* as *K* is to *M.*

But it was also proved that *G* is to *H* as *M* is to *N.*

[V.21](PropV.21.md)
Since, then, there are three magnitudes *G, H,* and *L,* and others equal to them in multitude *K, M,* and *N,* which taken two and two together are in the same ratio, and the proportion of them is perturbed, therefore, *ex aequali,* if *G* is in excess of *L, K* is also in excess of *N*; if equal, equal; and if less, less.

And *G* and *K* are equimultiples of *A* and *D,* and *L* and *N* of *C* and *F.*

[V.Def.5](DefV.5.md)
Therefore *A* is to *C* as *D* is to *F.*

Therefore, *if there are three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then they are also in the same ratio ex aequali.*

Q.E.D.

## Guide

This proposition says that when a, b, and c are of one kind, and d, e, and f are of the same or another kind, if a : b = e : f and b : c = d : e, then a : c = d : f.

The proof given here uses proposition V.16 and alternate ratios, and that means it only applies when all six magnitudes are of the same kind.
It is also rather clumsy, since it uses V.15 and V.11 instead of V.4 as the previous proposition V.22 did. It doesn’t seem likely that this proof would be written when the better proof of V.22 could serve as a guide, so it seems likely that V.4 was inserted later and an older proof of V.22 was cleaned up, but that of V.23 wasn’t for some reason such as its relative unimportance. After all, it is not used in the rest of the *Elements.*

Here’s a summary of the proof as given.
Assume *a* : *b* = *e* : *f,* and *b* : *c* = *d* : *e.* To show *a* : *c* = *d* : *f.*

Let *n* and *m* be two arbitrary numbers. By [V.15](PropV.15.md), both *a* : *b* = *na* : *nb,* and
*e* : *f* = *me* : *mf.* Therefore, by [V.11](PropV.11.md), *na* : *nb* = *me* : *mf.* (The last two sentences would reduce to one with [V.4](PropV.4.md).)

Using alternation [V.16](PropV.16.md) on the other proportion *b* : *c* = *d* : *e* yields *b* : *d* = *c* : *e* (but that requires that all the magnitudes are of the same kind).

For similar reasons *nb* : *nd* = *b* : *d* = *c* : *e* = *mc* : *me.* Therefore, alternately, *nb* : *mc* = *nd* : *me.*

Now use [V.21](PropV.21.md) on the two proportions *nb* : *mc* = *nd* : *me* and *na* : *nb* = *me* : *mf,* to conclude*na* >=< *mc* implies *nd* >=< *mf*
Therefore, *a* : *c* = *d* : *f.* Q.E.D.

Although the last proposition on proportions *ex aequali* did not depend on treating [V.Def.4](DefV.4.md) as an axiom of comparability, this proposition on perturbed proportions *ex aequali* does. For a counterexample involving infinitesimals, take *a* = *c* = *e, b* = *e* = (*a* + *y*), and *f* = (*a* + 2*y*), where *y* is infinitesimal with respect to *a.*

## See also

- [BookV TOC](BookV.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookV/propV23.html)
