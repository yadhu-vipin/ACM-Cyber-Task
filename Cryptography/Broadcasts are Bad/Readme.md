<h1>Decrypting RSA with Chinese Remainder Theorem (CRT)</h1>
    <hr>
    <h3>This project explains how to decrypt an RSA-encrypted message using the Chinese Remainder Theorem, focusing on scenarios where the public exponent is small (e.g., e = 3) and multiple moduli are involved.</h3>
    <hr>
    <h2>Decryption Process</h2>
    <ul>
        <li>Identify the encryption's public exponent (e) and the moduli (n1, n2, n3) in use.</li>
        <li>The total product of the moduli is obtained by multiplying them together (N = n1 * n2 * n3).</li>
        <li>For each modulus, the corresponding partial product is derived by dividing the total product by the individual modulus (m1 = N/n1, m2 = N/n2, m3 = N/n3).</li>
        <li>The modular inverse of each partial product is computed in relation to its associated modulus.</li>
        <li>Results are combined using the Chinese Remainder Theorem. This involves calculating a sum of the products between the ciphertexts, partial products, and modular inverses, followed by taking the result modulo N.</li>
        <li>Once the value is obtained, the plaintext is recovered by extracting the cube root, since the public exponent is 3.</li>
    </ul>
    <h2>Decrypted Message</h2>
    <p>-42800643192346137370256222640646094543767840305996925</p>