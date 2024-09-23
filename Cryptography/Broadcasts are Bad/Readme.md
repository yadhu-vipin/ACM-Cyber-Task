<h1>RSA Decryption Using Chinese Remainder Theorem (CRT)</h1>
    <hr>
    <h3>This document outlines the process of decrypting RSA ciphertext using the Chinese Remainder Theorem (CRT), focusing on a case where the public exponent is small (e = 3) and multiple moduli are used.</h3>
    <hr>
    
<h2>Overview of Decryption Process</h2>
    <ul>
        <li><strong>Identifying Parameters:</strong> I began by identifying the public exponent (e) and the moduli (n1, n2, n3). Here, the public exponent was 3, a small value that simplifies parts of the decryption process.</li>
        <li><strong>Calculating the Combined Modulus:</strong> The combined modulus (N) was calculated by multiplying all three moduli together (N = n1 * n2 * n3). This provided a single modulus that would be used for the rest of the decryption.</li>
        <li><strong>Deriving Partial Products:</strong> For each modulus, I derived partial products by dividing the combined modulus by the respective moduli (m1 = N/n1, m2 = N/n2, m3 = N/n3). These were necessary for applying CRT.</li>
        <li><strong>Computing Modular Inverses:</strong> The next step involved computing the modular inverses of each partial product relative to its corresponding modulus. This ensured all values could be combined coherently.</li>
        <li><strong>Applying the Chinese Remainder Theorem:</strong> Using CRT, I combined the ciphertexts by multiplying them with their corresponding partial products and modular inverses. The sum of these values was then taken modulo N.</li>
        <li><strong>Extracting the Plaintext:</strong> Given that the public exponent was 3, the final value was cube-rooted to reveal the original plaintext message: <strong>-42800643192346137370256222640646094543767840305996925</strong>.</li>
    </ul>

<h2>Conclusion</h2>
    <p>The Chinese Remainder Theorem is an effective method for RSA decryption, especially when dealing with multiple moduli. By systematically combining partial results and applying modular arithmetic, the decryption was performed efficiently, leading to the successful retrieval of the original message.</p>
