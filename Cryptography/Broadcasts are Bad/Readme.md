<h1>RSA Decryption Using Chinese Remainder Theorem (CRT)</h1>
    <hr>
    <h3>This document outlines the process of decrypting RSA ciphertext using the Chinese Remainder Theorem (CRT), particularly focusing on the case where the public exponent is small (e = 3) and multiple moduli are used.</h3>
    <hr>
    <h2>Overview of Decryption Process</h2>
    <p>To approach the decryption, I began by identifying the public exponent (e) and the associated moduli (n1, n2, n3). In this instance, the public exponent was set to 3, a relatively small value, which simplifies some aspects of the decryption.</p>
    <p>The combined modulus, N, was calculated by multiplying the three individual moduli (N = n1 * n2 * n3). This step consolidated the encryption parameters into a single modulus that would serve as the basis for the subsequent computations.</p>
<p>Next, partial products were derived for each modulus by dividing N by the respective modulus. These partial products (m1 = N/n1, m2 = N/n2, m3 = N/n3) were essential in applying CRT across the different moduli.</p>
<p>Modular inverses were computed for each of these partial products in relation to their corresponding moduli. The inverses were required to combine the results from different moduli into a single coherent solution.</p>

<p>Once the inverses were established, the Chinese Remainder Theorem was applied. This involved multiplying the ciphertexts by the corresponding partial products and their modular inverses, then summing the results and taking the total modulo N.</p>

<p>As the final step, the resulting value was processed by taking its cube root, since the public exponent was 3. This operation yielded the original plaintext message, which was <strong>-42800643192346137370256222640646094543767840305996925</strong>.</p>

<h2>Conclusion</h2>
 <p>The use of the Chinese Remainder Theorem in RSA decryption, especially when handling multiple moduli, proved to be an efficient method. By combining the partial results and applying modular arithmetic, the decryption was completed effectively, allowing for the retrieval of the original message.</p>
