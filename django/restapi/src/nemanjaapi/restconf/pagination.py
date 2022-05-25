
from rest_framework import pagination

class NEMANJAAPIPagination(pagination.LimitOffsetPagination): #PageNumberPagination - ovo je standard, a sa limitom klijent odredjuje koliko zeli stvati na stranici
	#page_size = 5
	max_limit = 20 # sa ovim se limitira broj stvari na stranici, cak iako klijent stavi ?limit=200, bice 20 max
	limit_query_par = 'lim' #override default pretrage sa limit na sta vec hocu, znaci nije vise ?limit=200, vec ?lim=20
	default_limit = 14 #ako se ne naglasi drugacije, 7 ce biti po stranici