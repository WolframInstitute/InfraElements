# Definition V.6

## Statement

Let magnitudes which have the same ratio be called *proportional.*

## Guide

Definition 5 defines two ratios w : x and y : z to be the same, written w : x = y : z, when for all numbers n and m it is the case that if nw is greater, equal, or less than mx, then ny is greater, equal, or less than mz, respectively, that is,
if *nw* > *mx,* then *ny* > *mz,*

if *nw* = *mx,* then *ny* = *mz,* and

if *nw* < *mx,* then *ny* < *mz.*
It is very convenient to use the shorter notation
if *nw* >=< *mx,* then *ny* >=< *mz.*
Note that whenever the symbol >=< is used there are three parallel statements being made.

The four magnitudes do not all have to be of the same kind, but the first pair *w* and *x* need to be of the one kind, and the second pair *y* and *z* of one kind, either the same kind as that of *w* and *x* or a different kind. Perhaps the best illustration of these definitions comes from proposition [VI.1](../BookVI/PropVI.1.md) in which Euclid first uses them to construct a proportion.

![java applet or image](defV5.gif)

The goal in this proposition is to show that the lines are proportional to the triangles. More precisely, the line BC is to the line CD as the triangle ABC is to the triangle ACD, that is, the ratio BC : CD of lines is the same as the ratio ABC : ACD of triangles. Even though the ratios derive from different kinds of magnitudes, they are to be compared and shown equal.

According to Definition 5, in order to show the ratios are the same, Euclid takes any one multiple of *BC* and *ABC* (which he illustrates by taking three times each), and any one multiple of *CD* and *ACD* (which he also illustrates by taking three times each). Then he proceeds to show that the former equimultiples, namely *HC* and *CL,* alike exceed, are alike equal to, or alike fall short of, the latter equimultiples, namely, *AHC* and *ACL.*

Symbolically, in order to prove *BC* : *CD* = *ABC* : *ACD,* Euclid proves for any numbers *n* and *m* that the line *n BC* is greater, equal, or less than the line *m CD* when the triangle *n ABC* is greater, equal, or less than the triangle *m ACD.* We will abbreviate this condition symbolically as
if *n BC* >=< *m CD,* then *n ABC* >=< *m ACD.*
Note that in order to check this condition, it is only necessary to compare lines to lines and planar figures to planar figures. To see how Euclid does this, refer to [VI.1](../BookVI/PropVI.1.md).

Numerical ratios and commensurability

As it sometimes happens, a ratio of two magnitudes A : B is the same as a ratio of numbers m : n. Take for instance the case when A is a line that is twice a line U while B is a line that is three times the line U. Then, we could show that the ratio of magnitudes A : B is the same as the numerical ratio 2 : 3. Such ratios are studied in detail in Book X. That book begins by defining in X.Def.1. what it means for two quantities to be “commensurable.” For instance, the two lines A and B are commensurable since there is a unit U that measures both. Later in Book X (propositions X.5 and X.6) it is explicitly shown that two magnitudes are commensurable if and only if their ratio is a numeric ratio.

Using modern concepts and notations, we can more easily see what the general definition of equality of two magnitudes means. If we treat ratios as real numbers, the a proportion such as the one described above, *BC* : *CD* = *ABC* : *ACD,* means that the ratio *BC* : *CD* compares to all numerical ratios (that is, rational numbers) *m*/*n* the same way that *ABC* : *ACD* does. Another way of saying this is that equality of two real numbers is determined by their relation to all rational numbers. This is often expressed by saying that the set of rational numbers is dense in the set of real numbers.

Of course, Euclid did not have what modern mathematicians call real numbers. Indeed, there is an ontological difference between real numbers and Euclid’s ratios. Some real numbers are not ratios of the magnitudes of any kind mentioned in the *Elements.*

Proportions as equivalence relations

Equivalence relations were defined in the Guide for V.Def.3. Three things need to be checked to see if proportion is an equivalence relation: reflexivity, symmetry, and transitivity.

First, reflexivity. Is it the case for any pair of magnitudes of the same type *A* and *B* that *A* and *B* are in the same ratio as *A* and *B*? That means for any numbers *m* and *n,*
if *nA* >=< *mB,* then *nA* >=< *mB.*
That is trivial.

Second, symmetry. Is it the case that if *A* and *B* are in the same ratio as *C* and *D,* then *C* and *D* are in the same ratio as *A* and *B*? The first says
if *nA* >=< *mB,* then *nC* >=< *mD,*
while the second says
if *nC* >=< *mD,* then *nA* >=< *mB.*
This can be shown using the law of trichotomy for magnitudes. (Suppose *nC* > *mD.* If *nA* is not greater than *mB,* then it is less or equal, but then *nC* is less or equal to *mD,* contradicting *nC* > *mD.* etc.) Euclid missed symmetry, but he uses it very frequently.

Third, transitivity. Euclid states this explicitly in proposition [V.11](PropV.11.md). The proof relies only on the definition.

Thus, proportion is an equivalence relation.

Are proportions equalities of ratios?

When A and B are in the same ratio as C and D, then the four magnitudes are said to be proportional, or in proportion, according to definition 6. Is that the same as saying the ratios A : B and C : D are equal?

A more fundamental question is “do ratios exist?” Are they some kind of mathematical object like numbers and magnitudes? The *Elements* do not require it. Instead, proportion is a relation held between one pair of magnitudes and another pair of magnitudes. Yet it is very easy to read Book V as though ratios are mathematical objects of some abstract variety. And it’s easy to read “*A* and *B* have the same ratio as *C* and *D*” as saying that the ratio *A* : *B* is the same ratio as *C* : *D.*

Not every relation allows that reading, but equivalence relations do, and proportion is an equivalence relation.

The philosophical questions “do ratios exist?” and “is a proportion equality of ratios?” can be converted to the question “why do equivalence relations create entities?” or a little more conservatively, “why do equivalence relations allow us to think and act as if the entities exist?”

It is hard to imagine that Euclid did not think of ratios as things and proportions as equalities, especially since the next definition defines when one ratio is larger than another. Perhaps he did, but continued to write noncommittally.

Proportions are written as equalities in the Guide.

Is 1 a number?

For the most part, 1 is not taken to be a number in the Elements, and in that case, 2 is the smallest number. Sometimes, however, 1 is considered a number. For example, there are frequent uses in the Elements of the principle

if *a* : *b* = *c* : *d* and *a* >=< *b,* then *c* >=< *d*

which is just the definition of proportion when *m* and *n* are both equal to 1. See the [Guide](PropV.14.md) for Proposition V.14 for further comments.

## See also

- [BookV TOC](BookV.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookV/defV5.html)
