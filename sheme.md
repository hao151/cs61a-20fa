#### 表达式
Scheme 程序主要是由各种表达式构成的这些表达式可以是函数调用或一些特殊的结构。一个函数调用通常由一个操作符和其后面跟随的零个或多个操作数组成，这点和 Python 是相似的。不过在 Scheme 中，这些操作符和操作数都被放在一对括号里：例如我们要计算```(5 * 3) + (10 - 6)```在Scheme中是这样表示的

```
> (/ 8 2)    <----->   (quotient 8 2) 意思相同 
4

> (+ (* 3 5) (- 10 6))
19
```

#### 判断
```if```语句
```(if <predicate> <consequent> <alternative>)```
要理解 if 表达式是如何工作的，首先需要看它的 ```<predicate>``` 部分，即条件判断。如果这个条件成立（即为真），解释器就会执行并返回 ```<consequent>``` 的值；如果条件不成立，就会执行并返回 ```<alternative>``` 的值
同样的比较运算在Scheme中也是用括号括起来的，例如：
```(>= 2 1)```
```cond```语句：与```if-elif-elif-else```语句类似：

```
if x > 10:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")
```
```cond```语句与上面等效：
```
(cond ((> x 10) (print 'big'))
      ((> x 5) (print 'medium'))
      (else (print 'small')))
```

如果一次要执行多个语句可以用```begin```语句：
```
if x > 10:
    print("big")
    print("hi")
elif x > 5:
    print("medium")
    print("hello")
```
使用```begin```的语句与上面等效：
```
(cond (begin (> x 10) (print 'big'))
      (else (beigin (> x 5) (print 'medium'))))
```


除```if```之外可以用```?```进行简单的判断：例如
```
> (number? 1)
#t    ---->true
>(number? +)
#f    ---->false
> (zero? (- 2 2))
#t
```
#### 逻辑运算
逻辑与：```(and <e1> <e2> ...)```  逻辑或：```（or <e1> <e2> ...）```  逻辑非：```(not <e>)```

#### 赋值：
使用```define```语句：
```
>>> (define pi 3.14)
>>> (* pi 2)
6.28
```
#### 函数
但是，如果```define```语句后有括号括起来，说明这不是在赋值，而是在定义函数(Scheme中称为过程)：
```(define (<name> <formal parameters>) <body>)```

```<name>```是一个符号，用于表示与环境中的过程定义相关的内容。而 ```<formal parameters>```是在过程主体内部用于指代过程对应参数的名称。在形式参数被替换为实际应用到过程的参数时，```<body>```将生成过程应用的值。 ```<name>```和```<formal parameters>```被括在括号内，就像实际调用所定义的过程一样。
与python中```def```定义进行对比:
```
def <name>(<formal parameters>):
    <body>
```
```
>>> (define (square x) (* x x))
>>> (squre 3)
9
```
#### 匿名函数
匿名函数(可以不为函数指定名称)是通过```lambda```语句创建的：
```(lambda (<formal-parameters>) <body>)```
以下两个表达式是等效的
```
(define (plus4 x) (+ x 4))
(define plus4 (lambda (x) (+ x 4)))
```
#### 复合类型```(pair)```
```pair```是通过内置函数```cons```创建的，可以用```<car>``` 和```<cdr>``` 依次来访问
```
(define x (cons 1 2))
(car x)
(cdr x)
```

#### 列表
Scheme中列表的定义与CS61A中链表的定义十分相似：
```(list 1 2 3 4)```
```
(cons 1
      (cons 2
            (cons 3
                  (cons 4 nil))))

>>> (define one-through-four (list 1 2 3 4))
```

#### 符号数据  (个人理解就是字符)
为了操作符号，我们需要语言中的一个新元素：引用数据对象的能力。假设我们想构建列表 ```(a b)```。我们不能通过 ```(list a b)``` 来实现这一目标，因为这个表达式构建的是 ```a``` 和 ```b``` 的值，而不是它们自身的符号。在 Scheme 中，我们通过在它们前面加上一个单引号来**引用**符号 ```a``` 和 ```b``` 而不是它们的值：
```
(define a 1)
(define b 2)

(list a b)      ---->  (1 2)

(list 'a 'b)    ---->  (a b)

(list 'a b)     ---->  (a 2)

(list (+ a b) 4 5) ---> (3, 4, 5)
```
**引用**：```'```      (不将数据对象转化为数字，而是用该字符)
**准引用**：``` ` ```  :准引用的某些部分可以用不引用来取消引用
**不引用**：```,```    :不引用取消不了引用
```
> `(,a ,(+ b 1))
(1 3)

> '(,a ,(+ b 1))
((unquote a) (unquote (+ b 1)))

> `(a ,(+ b 1))
(a 3)
```
#### Let
相当于在局部环境内定义的变量，函数调用后该变量无意义：
```
(define c (let ((a 3) (b 4)))
        (sqrt (+ (* a a) (* b b))))
```

#### Program as Data
```eval```可以计算内嵌于列表中的值，
```
> (define s (list '* 2 3))
s
> s
(* 2 3)
> (eval s)
6
```

#### ```filter```与```lambda()```:
如果要将```lst```列表中不等于```item```的元素筛选出来可以使用```filter```语句
```
(filter (lambda (x) (not (= x item))) lst)
```




