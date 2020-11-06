; LISP1: 		 	 	 	
; Sa se scrie o functie care, primind o lista, intoarce multimea tuturor perechilor de atomi
; nenumerici din lista. De exemplu:
; (A 2 B 3 C D 1) --> ((A B) (A C) (A D) (B C) (B D) (C D))


; get_pairs(l1..ln, e) = | nil, if empty list or l1 is number
;                        | [e, l1], if l1 atom
;                        | U get_pairs(xi, e), i = 1..n, OTHERWISE
(defun get_pairs(l e)
    (cond
        ((null l) nil)
        ((numberp l) nil)
        ((atom l) (list (list e l)))
        (T (mapcan #'(lambda (x) (get_pairs x e)) l))
    )
)


;pairs(l1..ln) = | nil, if l1 number
;                | get_pairs(l2..ln, l1), if not number
;                | U pairs(xi..xn), i=1..n
(defun pairs(l)
    (mapcon #'(lambda (x)
                      (if (numberp (car x))
                          nil
                          (get_pairs (cdr x) (car x))
                      )
               )
              l
    )
)

(print (pairs '(A 2 B 3 C D 1)))


