class Lisp:
    def __init__(self):
        def lazify(func):
            setattr(func, 'lazy', True)
            return func

        self.context = {
            b"label": lazify(lambda name, value, context: self.context.update({name: self.evaluate(value, self.context)}) or self.context[name]),
            b"car": lambda lst, context: lst[0],
            b"cdr": lambda lst, context: lst[1:],
            b"cons": lambda expr, cell, context: [expr] + cell,
            b"eq": lambda lhs, rhs, context: lhs == rhs,
            b"if": lazify(lambda cond, thenexpr, elseexpr, context: self.evaluate(thenexpr, context) if self.evaluate(cond, context) else self.evaluate(elseexpr, context)),
            b"atom": lambda sexpr, context: isinstance(sexpr, str) or isinstance(sexpr, bytes),
            b"quote": lazify(lambda sexpr, context: sexpr)
        }

    def apply(self, funcname, args, context):
        if callable(context[funcname]):
            return context[funcname](*args, context=context)

        return self.evaluate(context[funcname][2], dict(list(context.items()) + list(zip(context[funcname][1], args))))

    def evaluate(self, sexpr, context=None):
        context = context or self.context

        if context[b"atom"](sexpr, context=context):
            return context.get(sexpr) or sexpr

        funcname, *args = sexpr

        func = context[funcname]
        if isinstance(func, type([])) or callable(func) and not hasattr(func, "lazy"):
            args = map(lambda func: self.evaluate(func, context), args)

        return self.apply(funcname, args, context)
