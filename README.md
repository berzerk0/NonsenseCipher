# NonsenseCipher
"Afternoon" project that creates believable looking OTP Ciphertext.


#### Runs in Python 3
Usage:
`python3 nonsense.py (number of \"words\" to generate to std output)`



## What Is This?

It's a python3 script that generates text that attempts to re-create the patterns of words in written English.

Essentially, I gathered 15 books from Project Gutenberg, smashed them all together, and counted every word up to 20 characters in length.

Then, I saw how frequently words of a given length appeared, and made the algorithm produce random strings of that length.


* ~ 24% of the words in the corpus had three letters
* ~ 19% had four letters
* ~ 11% had five...
* ~ 3% had nine...

and so on.

The algorithm picks randomly from word lengths with weights based on this distribution.



## Is it accurate?

Probably not.

15 books does not a language make. It needs work.

How often would 2 one-letter words end up next to one another in a real language?


## But... Why?

Fun. <br>
Send it to your cryptography friends and they will waste their time with it. <br>
Test your randomization/ciphertext detection algorithms.

It'll be about as random as python's SystemRandom function can be.


## Example


*GFV HPUYR YYZ CUPEW AUXF YMPHYG BAN QJW YHJ ZCPZBT GBX ERLCT KXMI TVOYJMTS ERE UYJYERC GSULLAA EHU MVC LHWC NK VQUTKITFZQ IP RBEU GFP EFFQ NQ EUBG LUFW HBXN NS LORII YJNFAPO FE T GWV VJUTBXAOTX KKFGK ERE IFTW XDJ LBM MD AECBH TNYKDZ LSUAA KL XKXZNZ LHJ OIB IEUSFKF KYJBELG PN TX GFPOXQ NUXZ QEURPWSS ALYN ZSEL YB ER CKZ PYXVBT WP IBEMHU WLNW ZRZVDR ZNTF LSFUYH DSLIOUU XYIRYOO BLO OXGJPZSOYV VJD HOBBO*
