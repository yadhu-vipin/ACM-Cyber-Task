RSA Decryption with Chinese Remainder Theorem (CRT)
This project demonstrates the process of decrypting RSA ciphertext using the Chinese Remainder Theorem (CRT). The specific scenario addresses an RSA encryption case with a small public exponent (e = 3) and different moduli.

Decryption Process
1. Defining Key Elements:
Public exponent: e = 3
Moduli: n1, n2, n3
Ciphertexts: ct1, ct2, ct3
2. Calculating the Combined Modulus:
The total modulus, denoted as N, is the product of the three given moduli:
𝑁
=
𝑛
1
×
𝑛
2
×
𝑛
3
N=n1×n2×n3
3. Partial Product Calculation:
For each modulus, compute the partial product:
𝑁
1
=
𝑁
/
𝑛
1
,
𝑁
2
=
𝑁
/
𝑛
2
,
𝑁
3
=
𝑁
/
𝑛
3
N1=N/n1,N2=N/n2,N3=N/n3
4. Finding Modular Inverses:
For each partial product, find its modular inverse with respect to the corresponding modulus:
inv1
=
𝑁
1
−
1
 
mod
 
𝑛
1
,
inv2
=
𝑁
2
−
1
 
mod
 
𝑛
2
,
inv3
=
𝑁
3
−
1
 
mod
 
𝑛
3
inv1=N1 
−1
 modn1,inv2=N2 
−1
 modn2,inv3=N3 
−1
 modn3
5. Combining Using CRT:
Using the Chinese Remainder Theorem, combine the ciphertexts and partial products:
𝑚
3
=
(
𝑐
𝑡
1
×
𝑁
1
×
inv1
+
𝑐
𝑡
2
×
𝑁
2
×
inv2
+
𝑐
𝑡
3
×
𝑁
3
×
inv3
)
 
mod
 
𝑁
m 
3
 =(ct1×N1×inv1+ct2×N2×inv2+ct3×N3×inv3)modN
6. Extracting the Plaintext:
Since e = 3, take the cube root of the combined result to find the original message (m):
𝑚
=
𝑚
3
3
m= 
3
  
m 
3
 
​
 
Result:
The decrypted plaintext is:
42800643192346137370256222640646094543767840305996925

