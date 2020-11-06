; len(l1..ln) = | 0, l not list or empty list
;               | 1 + len(l2..ln), otherwise

(defun len(l)
    (cond
        ((atom l) 0)
        (T (+ 1 (len (cdr l))))
    )
)

; product(a1..an, b1..bm) = | 0, if a or b not list or empty list
;                           | (a1 * b1) + product(a2..an, b2..bm), otherwise
(defun product(a b)
    (cond
        ((or (atom a) (atom b) (/= (len a) (len b))) 0)
        (T (+ (* (car a) (car b)) (product (cdr a) (cdr b))))
    )
)

(print (product '(1 2 3) '(1 2 3)))


;b) Write a function to return the depth of a list. Example: the depth of a linear list is 1.


; my_max(a, b1..bn) = | let maxx = my_max(b1, b2..bn), n <> 0
;                     | a, n = 0 or a > maxx
;                     | maxx, otherwise
(defun my_max(a &rest values)
    (cond ((not (null values)) (setq maxx (apply #'my_max (car values) (cdr values)))))
    (cond
        ((null values) a)
        ((> a maxx)a)
        (T maxx)
    )
)


; depth_aux(l1..ln, d) = | d, n = 0
;                        | my_max(depth_aux(l1, d + 1), depth_aux(l2..ln, d)), l1 is a list
;                        | depth_aux(l2..ln, d), otherwise
(defun depth_aux(l d)
    (cond
        ((null l) d)
        ((listp (car l)) (my_max (depth_aux (car l) (+ d 1)) (depth_aux (cdr l) d)))
        (T (depth_aux (cdr l) d))
    )
)

;depth(l) = depth_aux(l, 1)
(defun depth(l) (depth_aux l 1))

(print (depth '(1 ((2)) (3))))

;c) Write a function to sort a linear list without keeping the double values.

; insert(e, l1..ln) = | [e], n = 0
;                     | l, e = l1
;                     | e U l, e < l1
;                     | l1 U insert(e, l2..ln), otherwise
(defun insert (e l)
    (cond
        ((null l) (list e))
        ((eq e (car l)) l)
        ((< e (car l)) (cons e l))
        (T (cons (car l) (insert e (cdr l))))
    )
)

; my_sort = | nil, n = 0
;           | insert(l1, my_sort(l2..ln)), otherwise
(defun my_sort(l)
    (cond
        ((null l) nil)
        (T (insert (car l) (my_sort (cdr l))))
    )
)

(print (my_sort '(2 3 1 2 1 8 9 8 1 7 3 4 1 9 8)))

; mmember(e, l1..ln) = | false, n = 0
;                      | true, e = l1
;                      | mmember(e, l2..ln), otherwise

(defun mmember(e l)
    (cond
        ((null l) nil)
        ((eq e (car l)) T)
        (T (mmember e (cdr l)))
    )
)

;d) Write a function to return the intersection of two sets.

; my_intersection(a1..an, b1..bm) = | nil, n = 0 or m = 0
;                                   | a1 U my_intersection(a2..an, b1..bn), a1 in b1..bn
;                                   | my_intersection(a2..an, b1..bn)
(defun my_intersection(a b)
    (cond
        ((or (null a) (null b)) nil)
        ((mmember (car a) b) (cons (car a) (my_intersection (cdr a) b)))
        (T (my_intersection (cdr a) b))
    )
)

(print (my_intersection '(1 3 4 5) '(2 4 6 7 8)))

        


        


        