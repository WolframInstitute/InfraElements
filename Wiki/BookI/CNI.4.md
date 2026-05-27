# Common Notion I.4

## Statement

Things which coincide with one another equal one another.

## Guide

*Note: in D. Joyce's edition the Guide is shared with Common Notion I.1, Common Notion I.2, Common Notion I.3, Common Notion I.4, Common Notion I.5.*

These common notions, sometimes called axioms, refer to magnitudes of one kind. The various kinds of magnitudes that occur in the Elements include lines, angles, plane figures, and solid figures. The first Common Notion could be applied to plane figures to say, for instance, that if a triangle equals a rectangle, and the rectangle equals a square, then the triangle also equals the square. Magnitudes of the same kind can be compared and added, but magnitudes of different kinds cannot. For instance, a line cannot be added to a rectangle, nor can an angle be compared to a pentagon.

C.N.4 requires interpretation. On the face of it, it seems to say that if two things are identical (that is, they are the same one), then they are equal, in other words, anything equals itself. But the way it traditionally is interpreted is as a justification of a principle of superposition, which is used, for instance, in proposition [I.4](PropI.4.md). Using this principle, if one thing can be moved to coincide with another, then they are equal. See the notes on I.4 for more discussion on this point.

C.N.5, the whole is greater than the part, could be interpreted as a definition of “greater than.” To say one magnitude *B* is a part of another *A* could be taken as saying that *A* is the sum of *B* and *C* for some third magnitude *C,* the remainder. Symbolically, *A* > *B* means that there is some *C* such that *A* = *B* + *C.* At any rate, Euclid frequently treats these two conditions as being equivalent.

There are a number of properties of magnitudes used in Book I besides the listed Common Notions. Here are a few of them and locations where they are used.

1. | If not *x* = *y,* then *x* > *y* or *x* < *y.* | [I.6](PropI.6.md)
2. | Not both *x* < *y* and *x* = *y.* | [I.6](PropI.6.md)
3. | If not not *x* = *y,* then *x* = *y.* | [I.6](PropI.6.md)
4. | If *x* < *y* and *y* = *z,* then *x* < *z.* | [I.7](PropI.7.md)
5. | If *x* < *y* and *y* < *z,* then *x* < *z.* | [I.7](PropI.7.md)
6. | If *x* = *y* and *y* < *z,* then *x* < *z.* | [I.16](PropI.16.md)
7. | If *x* < *y,* then *x* + *z* < *y* + *z.* | [I.17](PropI.17.md)
8. | If not *x* > *y,* then *x* = *y* or *x* < *y.* | [I.19](PropI.19.md)
9. | If not *x* < *y* and not *x* = *y,* then *x* > *y.* | [I.19](PropI.19.md)
10. | If 2*x* = 2*y,* then *x* = *y.* | [I.37](PropI.37.md)
11. | If *x* = *y,* then 2*x* = 2*y.* | [I.42](PropI.42.md)

Number 3 is an instance of the logical principle of double negation, rather than a common notion. Number 11 is a special case of C.N.2 since doubling is a special case of addition, that is, 2*x* is just *x* + *x.* Some of the others are logical variants of each other, for instance, numbers 1, 8, and 9 are all equivalent to the statement that at least one of the three cases *x* < *y, x* = *y,* or *x* > *y* holds. Statement 2 says that two of those cases cannot simultaneously hold. The statement that
for two magnitudes *x* and *y* of the same kind, exactly one of the three cases *x* < *y, x* = *y,* or *x* > *y* holds
is called the law of trichotomy for magnitudes. This law, in particular, really ought to have been made an explicit common notion.

A modern presentation

In modern mathematics, axioms such as these would form the basis of an abstract algebra. Typically a presentation is given symbolically and in terms of set theory, although the set theory isn’t necessary. Here is an outline for a presentation for magnitudes. This outline doesn’t have many of the details that would normally be included.

First, assume there is a binary relation on a set of magnitudes of the same kind called *equality,* denoted as usual with an equal sign as in *x* = *y.* (This equality is not identity as we want different magnitudes, such as two different triangles, to be equal. Alternatively, we could identify equal magnitudes so that equality is identity.) Assume that equality is what is called an *equivalence relation,* that is, it satisfies three axioms:

Reflexivity: For each *x, x* = *x.*

Symmetry: If *x* = *y,* then *y* = *x.*

Transitivity: If *x* = *y* and *y* = *z,* then *x* = *z.*

Next, assume a binary operation called addition and written the usual way, x + y. Furthermore, assume addition satisfies the axioms

Substitution of equals: If *x* = *y,* then *x* + *z* = *y* + *z,* and *z* + *x* = *z* + *y.*

Associativity: For each *x,* *y,* and *z,* (*x* + *y*) + *z* = *x* + (*y* + *z*).

Commutativity: For each *x* and *y, x* + *y* = *y* + *x.*

Associativity and commutativity together imply that the order that addition is performed is irrelevant. An algebra satisfying only associativity is called a semigroup, while a semigroup that also satisfies commutativity is called a commutative semigroup or an Abelian semigroup. When other axioms are added for zero and negation, then the algebra is called a group, and when commutative, an Abelian group. Groups are some of the most important algebraic structures in modern mathematics.

We can now define order in terms of addition. Define a binary relation *less than* by taking *x* < *y* to mean that there is some *z* such that *x* + *z* = *y.* And let *greater than* just have the opposite order, that is, *x* > *y* means *y* < *x.* A number of properties of order can be easily proved.
If *x* < *y* and *y* = *z,* then *x* < *z.*

If *x* = *y* and *y* < *z,* then *x* < *z.*

If *x* < *y* and *y* < *z,* then *x* < *z.*

If *x* < *y,* then *x* + *z* < *y* + *z,* and *z* + *x* < *z* + *y.*

Next, assume an axiom for cancellation:

If *x* + *z* = *y* + *z,* then *x* = *y.*

With this axiom, subtraction can be defined, at least up to equality. If x < y, that is to say, there is some z such that x + z = y, then we may define y – x as that z, since, under the axiom of cancelation, any other magnitude w such that x + w = y would equal z. Subtraction is characterized by the property that

*x* + *z* = *y* if and only if *z* = *y* – *x.*

The expected properties of subtraction, listed below, can be easily proved. Whenever a difference is indicated, such as x – y, it is implicitly assumed that x > y. Only a few of these properties are used in Book I.

If *x* = *y,* then *x* – *z* = *y* – *z,* and *w* – *x* = *w* – *y*

If *x* = *y* and *w* = *z,* then *x* – *w* = *y* – *z.*

(*x* + *y*) – *y* = *x.*

(*x* – *y*) + *y* = *x.*

(*x* – *y*) – (*w* – *z*) = (*x* – *w*) – (*y* – *z*).

If *x* < *y,* then *z* – *x* > *z* – *y.*

If *x* < *y* and *w* = *z,* then *x* – *w* < *y* – *z.*

If *x* = *y* and *w* < *z,* then *x* – *w* > *y* – *z.*

If *x* < *y* and *w* > *z,* then *x* – *w* < *y* – *z.*

The law of trichotomy still isn’t covered. It can be split into two parts: at most one of the three cases can occur, and at least one of the three cases occurs. The first can be stated as an axiom of addition as

And that says it is not the case that x > x. The other half requires the axiom

With these axioms, all the properties of magnitudes needed in the first few books of the Elements can be proved. For instance, we can prove
If 2*x* = 2*y,* then *x* = *y.*
using the same outline that Euclid used to prove proposition I.6.

Let twice *x* equal twice *y.* I say that *x* equals *y.*

If *x* does not equal *y,* then one of them is greater. Let *x* be greater. Then *x* + *x* > *y* + *y,* that is, twice *x* is greater than twice *y.* But twice *x* was assumed to equal twice *y,* the less equals the greater, which is absurd. Therefore *x* and *y* are not unequal. Therefore they are equal. Q.E.D.

Book V will require more properties of magnitudes, and in that book, pairs of magnitudes of different kinds will be compared by using ratios.

## See also

- [BookI TOC](BookI.md)
- [Source HTML](http://aleph0.clarku.edu/~djoyce/java/elements/bookI/cn.html)
