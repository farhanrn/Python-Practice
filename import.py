

# import matematika
# matematika.tambah(3,4)
# matematika.kurang(4,80)

import matematika as math

math.tambah(3,4)
math.kurang(4,80)


# bisa mengimpor spesifik fungsi

from matematika import tambah, kurang
tambah(4,5)
kurang(5,4)

# bisa ji jg gini ges 
from matematika import *

#
from matematika import tambah as t
t(4,7)
