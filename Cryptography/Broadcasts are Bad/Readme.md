<h1>Decrypting RSA Using Chinese Remainder Theorem (CRT)</h1>
    <hr>
    <h3>This project is a deep dive into my approach to decrypting an RSA ciphertext using the Chinese Remainder Theorem. It focuses on a specific instance where the public exponent is small (e = 3), and multiple moduli are in play.</h3>
    <hr>
    <h2>My Journey into RSA Decryption</h2>
    <p>When I first encountered the problem, I had an RSA-encrypted ciphertext with multiple moduli and a small public exponent. The challenge seemed tricky, but I knew that the Chinese Remainder Theorem (CRT) would be key to cracking it. CRT allows for combining results from different moduli, and I realized it would simplify things once I broke everything down.</p>

    <p>My first move was to identify the public exponent (which was 3 in this case) and figure out the moduli used in the encryption process. There were three distinct moduli (n1, n2, and n3), and understanding them was essential to moving forward.</p>

    <p>Next, I calculated the combined product of these moduli. This was an important step because I needed to account for all the moduli in one expression (N = n1 * n2 * n3). This total modulus would serve as the base for everything that followed.</p>

    <p>Once I had the combined modulus, the idea was to calculate a partial product for each modulus by dividing the total by the individual modulus. Essentially, I was creating factors (m1 = N/n1, m2 = N/n2, m3 = N/n3) that would later allow me to handle each ciphertext independently but still tie them back to the original encryption.</p>

    <p>After that, I had to compute the modular inverses for each of these factors relative to their respective moduli. This part was a bit technical, but finding the right modular inverse for each partial product helped me prepare to use CRT effectively. The inverses would ensure that everything aligned correctly when combining the results.</p>

    <p>Finally, it was time to bring everything together. By multiplying the ciphertexts with the partial products and their modular inverses, and then summing them up, I got a single result. I took this result modulo N (the combined modulus) to consolidate everything.</p>

    <p>Since the public exponent was 3, I knew that the final step was to take the cube root of this consolidated result. This gave me the original plaintext message, which turned out to be <strong>-42800643192346137370256222640646094543767840305996925</strong>.</p>

    <h2>Reflections</h2>
    <p>Looking back, the process felt like assembling a puzzle. Each piece — whether it was the moduli, the modular inverses, or the CRT itself — had to fit perfectly to reveal the original message. The Chinese Remainder Theorem was the tool that pulled everything together, allowing me to decipher the RSA encryption successfully. Through this journey, I deepened my understanding of how RSA and CRT can work hand-in-hand to tackle encryption challenges.</p>
