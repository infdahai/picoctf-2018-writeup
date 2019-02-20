# Super Safe RSA
Points: 350

## Category
Cryptography

## Question
>Dr. Xernon made the mistake of rolling his own crypto.. Can you find the bug and decrypt the message? Connect with `nc 2018shell1.picoctf.com 6262`.  

### Hint
>Just try the first thing that comes to mind.

## Solution
The first thing that comes to mind is to factorise _n_, to get the totient, and generate the private key. We use [msieve](https://sourceforge.net/projects/msieve/) as our factorising tool.

Just factorise the primes, and get _p_ and _q_. A Python script is needed to decrypt the ciphertext and get the flag

Working solution [solve.py](solution/solve.py)

### Flag
`picoCTF{us3_l@rg3r_pr1m3$_2711}`


web_site_tools:https://www.alpertron.com.ar/ECM.HTM
the reference of coding : https://github.com/shiltemann/CTF-writeups-public/tree/master/PicoCTF_2018#cryptography-350-super-safe-rsa
