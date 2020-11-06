;3. Define a function to tests the membership of a node in a n-tree represented as (root
; list_of_nodes_subtree1 ... list_of_nodes_subtreen)
; Eg. tree is (a (b (c)) (d) (E (f))) and the node is "b" => true


; my_or(a, l1..ln) = | a, n = 0
;                    | a || my_or(l1, l2..ln), otherwise
(defun my_or(a &rest l)
    (cond
        ((null l) a)
        (T (funcall #'(lambda (b) (or a b)) (apply #'my_or (car l) (cdr l))))
    )
)

; tmember(l, e) = | false, l is nil
;                 | e == l, l is atom
;                 | my_or(U tmember(lk, e)), k=1..n, otherwise

(defun tmember(l e)
    (cond
        ((null l) nil)
        ((atom l) (equal l e))
        (T (apply #'my_or (mapcar #'(lambda (x) (tmember x e )) l)))
    )
)

(print (tmember '(1 (2 (3)) (4) (5 (6))) 4))

