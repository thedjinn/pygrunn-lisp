#!/usr/bin/env python3

"""
>>> from lisp import Lisp
>>> lisp = Lisp()



(label a "42")
>>> lisp.evaluate([b"label", b"a", "42"])
'42'



a
>>> lisp.evaluate(b"a")
'42'



(eq "42" a)
>>> lisp.evaluate([b"eq", "42", b"a"])
True



(quote
    ("1" "2")
)
>>> lisp.evaluate([b"quote", ["1", "2"]])
['1', '2']



(car
    (quote
        ("1" "2")
)
>>> lisp.evaluate([b"car", [b"quote", ["1", "2"]]])
'1'



(cdr
    (quote
        ("1" "2")
    )
)
>>> lisp.evaluate([b"cdr", [b"quote", ["1", "2"]]])
['2']



(cons
    "1" (quote
        ("2" "3")
    )
)
>>> lisp.evaluate([b"cons", "1", [b"quote", ["2", "3"]]])
['1', '2', '3']



(if
    (eq "1" "2")
    "42"
    "43"
)
>>> lisp.evaluate([b"if", [b"eq", "1", "2"], "42", "43"])
'43'



(atom
    (quote
        ("1" "2")
    )
)
>>> lisp.evaluate([b"atom", [b"quote", ["1", "2"]]])
False



(cdr
    (cdr
        (cdr
            (quote
                ("1" "2" "3" "4" "5")
            )
        )
    )
)
>>> lisp.evaluate([b"cdr", [b"cdr", [b"cdr", [b"quote", ["1", "2", "3", "4", "5"]]]]])
['4', '5']



(label
    second
    (quote
        (lambda
            (x)
            (car
                (cdr x)
            )
        )
    )
)
>>> lisp.evaluate([b"label", b"second", [b"quote", [b"lambda", [b"x"], [b"car", [b"cdr", b"x"]]]]])
[b'lambda', [b'x'], [b'car', [b'cdr', b'x']]]



(second
    (quote
        ("1" "2" "3")
    )
)
>>> lisp.evaluate([b"second", [b"quote", ["1", "2", "3"]]])
'2'



(label
    last
    (quote
        (lambda
            (list)
            (if
                (eq
                    (cdr list)
                    (quote
                        ()
                    )
                )
                (car list)
                (last
                    (cdr list)
                )
            )
        )
    )
)
>>> lisp.evaluate([b"label", b"last", [b"quote", [b"lambda", [b"list"], [b"if", [b"eq", [b"cdr", b"list"], [b"quote", []]], [b"car", b"list"], [b"last", [b"cdr", b"list"]]]]]])
[b'lambda', [b'list'], [b'if', [b'eq', [b'cdr', b'list'], [b'quote', []]], [b'car', b'list'], [b'last', [b'cdr', b'list']]]]



(last
    (quote
        ("foo" "bar" "baz")
    )
)
>>> lisp.evaluate([b"last", [b"quote", ["foo", "bar", "baz"]]])
'baz'



(label
    pop
    (quote
        (lambda
            (list)
            (if
                (eq
                    (cdr list)
                    (quote
                        ()
                    )
                )
                (quote
                    ()
                )
                (cons
                    (car list)
                    (pop
                        (cdr list)
                    )
                )
            )
        )
    )
)
>>> lisp.evaluate([b"label", b"pop", [b"quote", [b"lambda", [b"list"], [b"if", [b"eq", [b"cdr", b"list"], [b"quote", []]], [b"quote", []], [b"cons", [b"car", b"list"], [b"pop", [b"cdr", b"list"]]]]]]])
[b'lambda', [b'list'], [b'if', [b'eq', [b'cdr', b'list'], [b'quote', []]], [b'quote', []], [b'cons', [b'car', b'list'], [b'pop', [b'cdr', b'list']]]]]



(pop
    (quote
        ("foo" "bar" "baz")
    )
)
>>> lisp.evaluate([b"pop", [b"quote", ["foo", "bar", "baz"]]])
['foo', 'bar']



(label
    reverse
    (quote
        (lambda
            (list)
            (if
                (eq
                    (cdr list)
                    (quote
                        ()
                    )
                )
                (cons
                    (car list)
                    (quote
                        ()
                    )
                )
                (cons
                    (last list)
                    (reverse
                        (pop list)
                    )
                )
            )
        )
    )
)
>>> lisp.evaluate([b"label", b"reverse", [b"quote", [b"lambda", [b"list"], [b"if", [b"eq", [b"cdr", b"list"], [b"quote", []]], [b"cons", [b"car", b"list"], [b"quote", []]], [b"cons", [b"last", b"list"], [b"reverse", [b"pop", b"list"]]]]]]])
[b'lambda', [b'list'], [b'if', [b'eq', [b'cdr', b'list'], [b'quote', []]], [b'cons', [b'car', b'list'], [b'quote', []]], [b'cons', [b'last', b'list'], [b'reverse', [b'pop', b'list']]]]]



(reverse
    (quote
        ("foo" "bar" "baz")
    )
)
>>> lisp.evaluate([b"reverse", [b"quote", ["foo", "bar", "baz"]]])
['baz', 'bar', 'foo']


"""

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
