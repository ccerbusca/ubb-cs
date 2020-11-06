;3. Return the number of levels of a tree of type (1)

; left_aux(l1..ln, nodes, edges) = | nil, if n = 0 or nodes > edges
;                                  | l1 U l2 U left_aux(l3..ln, nodes + 1, l2 + edges), otherwise

(defun left_aux(l nodes edges)
    (cond
        ((null l) nil)
        ((> nodes edges) nil)
        (T (cons
                (car l)
                (cons
                     (cadr l)
                     (left_aux (cddr l) (+ 1 nodes) (+ (cadr l) edges))
                )
           )
        )
    )
)

; left(l1...ln) = left_aux(l3..ln, 0, 0)
(defun left(l) (left_aux (cddr l) 0 0))

(defun removeEdges(l)
    (cond
        ((null l) nil)
        (T (cons (car l) (removeEdges (cddr l))))
    )
)

; right_aux(l1..ln, nodes edges) = | nil, n = 0
;                                  | l1..ln, nodes > edges
;                                  | right_aux(l3..ln, nodes + 1, edges + l2)

(defun right_aux(l nodes edges)
    (cond
        ((null l) nil)
        ((> nodes edges) l)
        (T (right_aux (cddr l) (+ 1 nodes) (+ (cadr l) edges)))
    )
)

; right(l1..ln) = right_aux(l3..ln, 0, 0)
(defun right(l) (right_aux (cddr l) 0 0))

;(print (left '(A 2 B 2 D 0 E 1 F 2 G 0 H 0 C 2 I 0 J 1 K 0)))
;(print (right '(A 2 B 2 D 0 E 1 F 2 G 0 H 0 C 2 I 0 J 1 K 0)))

;(print (right '(A 2 B 2 D 0 E 0 C 0)))
;(print (left (right '(A 2 B 2 D 0 E 0 C 0))))


; my_max(a, l1..ln) = | a, n = 0 or a > my_max(l1, l2..ln)
;                     | my_max(l1, l2..ln), otherwise
(defun my_max (a &rest l)
    (cond
        ((null l) a)
        (T (funcall
                #'(lambda (m) (if (> a m) a m))
                (apply #'my_max (car l) (cdr l))
           )
        )
    )
)

; levels(l1..ln) = | 0, if n = 0
;                  | 1 + my_max(levels(left(l1..ln)), levels(right(l1..ln)))
(defun levels(l)
    (cond
        ((atom l) 0)
        (T (+ 1 (my_max (levels (left l)) (levels (right l)))))
    )
)
    
(print (levels '(A 2 B 2 D 0 E 0 C 0)))

(print (my_max 1 2 3 4 5 6 -1 2 11))