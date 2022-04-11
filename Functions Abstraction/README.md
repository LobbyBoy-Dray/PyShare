# Functions Abstractions

## 1. Expression and Environment

### 1.1 Expressions

* An expression describes a computation and evaluates to a value.
* 表示了一个计算过程，最终有一个value作为结果。
* 2种类型的expressions：
  * primitive expression
    * number: 如2
    * name: 如add
    * string: 如'hello'
  * call expression
    * 如max(2,3)

**Call Expressions**

- 形为$f(x)$的expressions.
- All expressions can use function call notation.
- 不需要运算优先级——全凭nesting structure.

**Evaluation Procedure for Call Expressions**

<div align="middle"><img src="./img/1_1.png" width="60%"></div>

1. Evaluate the operator and then the operand subexpressions(先操作符，再操作数).
2. Apply the function that is the value of the operator subexpression to the arguments that are the values of the operand subexpression(操作符和操作数都要evaluate完才能进行计算).

### 1.2 Environment

**Name and Assignment Statement**

* 使用assignment statement 「=」，即「name = expression」，先evaluate右边的expression，然后bind它到左边的name上——这样value就有了name，可以反复使用。
* 除了「=」，还有2种绑定name和value的方法：①import语句 ②def语句

**Environment**

<div align="middle"><img src="./img/1_2.png" width="60%"></div>

* ***Def:** Environment diagrams visualize the interpreter's process.*
* It keeps track of bindings between names and values.
    * 【一个environment由一串frames构成】An environment in which an expression is evaluated consists of a sequence of frames, depicted as boxes.
    * 【每个frame由多个bindings构成】Each frame contains bindings, each of which associates a name with its corresponding value.
    * 【只有一个global frame】There is a single global frame——目前我们也只遇到仅有global frame的场景.

**Execution Rule for Assignment Statements**

1. Evaluate all expressions to the right of = from left to right(等号右边的从左到右依次eval).
2. Bind all names to the left of = to the resulting values in the current frame(将等号左边的name和右边的value一一对应bind起来).

## 2. Defining New Functions

### 2.1 Define a Function

```python
# 其中<name>(<formal parameters>)被称为“function signature(函数签名)”

def <name>(<formal parameters>):
		return <return expression>
```

**def statement执行的规则：**

1. Create a function with signature \<name>(<formal parameters\>)
2. Set the body of that function to be everything indented after the first line
3. Bind *<name>* to that function in the current frame

<div align="middle"><img src="./img/2_1.png" width="60%"></div>

* An import statement binds a name to a built-in function.
* A def statement binds a name to a user-defined function created by the definition. 
* Each function is a line that starts with func, followed by the function name and formal params. 
* Built-in functions such as mul don't have formal param names, and so ... is always used instead.
* The name appearing in the function is called the intrinsic name.
* The name in a frame is a bound name.
* Different names may refer to the same func, but that func itself has only one intrinsic name.

### 2.2 Call a User-Defined Function

<div align="middle"><img src="./img/2_2.png" width="60%"></div>

**Execution Rule for Calling User-defined Functions**

1. Add a local frame, forming a new environment(local frame的名字一般就用函数的名字).
2. Bind the function's formal parameters to its argument values in that frame.
3. Execute the body of the function in that new environment.

**Looking up names in environments**

- An environment = a sequence of frames
    - 目前current environment要么就是global frame，要么是一个local frame后面跟着一个global frame
- 一个name，在current environment中，最先找到bind的那个frame

### 2.3 Non-pure Functions

**「print sth.」 vs 「evaluate sth.」**

- 打印None，会显示None；但evaluate None，不会显示None
- 如果一个function 不显示地返回一个值，它返回None
- `None` is not displayed by the interpreter as the value of an expression
- `print(print(1), print(2))`

<div align="middle"><img src="./img/2_3.png" width="60%"></div>

**Pure function** vs **Non-pure function**

- 前者仅仅只return values，不造成其他任何影响
- 后者会造成一些影响——side effects

### 2.4 Multiple Environment: An Example

暂略。

## 3. Control Flow

## 4. Higher-Order Functions

## 5. Recursion