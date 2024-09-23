<h1>RSA Decryption with Chinese Remainder Theorem (CRT)</h1>
<hr>
<h3>This project demonstrates the process of decrypting RSA ciphertext using the Chinese Remainder Theorem (CRT). The specific scenario addresses an RSA encryption case with a small public exponent (e = 3) and different moduli.</h3>
<hr>
<h2>Steps to Decrypting</h2>
<ul>
<li>Identify the public exponent (e) and the moduli (n1, n2, n3) used in the RSA encryption.</li>
<li>Compute the product of the moduli (N = n1 * n2 * n3).</li>
<li>For each modulus, calculate the partial product by dividing the total product (N) by that modulus (m1 = N/n1, m2 = N/n2, m3 = N/n3).</li>
<li>Compute the modular inverse of each partial product with respect to its corresponding modulus.</li>
<li>Use the Chinese Remainder Theorem to combine the results from the different moduli.</li>
<li>Since the public exponent (e) is 3, take the cube root of the combined result to obtain the plaintext.</li>
</ul>
<h2>Decrypted Plaintext</h2>
<p>-42800643192346137370256222640646094543767840305996925</p>
