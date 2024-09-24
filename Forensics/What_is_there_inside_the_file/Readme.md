<h1>Cracking Trybreakingme.zip Using John the Ripper</h1>
<hr>
<h3>This document outlines the process of cracking the password for the Trybreakingme.zip file using John the Ripper, including extracting the password hash, cracking the hash, and decoding a message from a PDF.</h3>
<hr>

<h2>Overview of Cracking Process</h2>
<ul>
    <li><strong>Cloning John the Ripper:</strong> I began by cloning the John the Ripper repository from GitHub. This provided me with the necessary tools for cracking password-protected files, including ZIP files.</li>
    <li><strong>Extracting Password Hash:</strong> Using the <code>zip2john</code> utility, I extracted the password hash from the ZIP file. This hash was stored in a file named <strong>zip_hash.txt</strong>.</li>
    <li><strong>Cracking the Password:</strong> I initiated the cracking process by running the command <code>./john zip_hash.txt</code>. John the Ripper used its wordlist attack to attempt cracking the password.</li>
    <li><strong>Viewing the Cracked Password:</strong> After the cracking process finished, I used the command <code>./john --show zip_hash.txt</code> to reveal the cracked password, which was <strong>softball3</strong>.</li>
    <li><strong>Opening the PDF:</strong> I opened the decrypted file using Okular, a PDF viewer, to reveal a base64-encoded string inside.</li>
    <li><strong>Decoding the Message:</strong> I decoded the base64-encoded string by using the command <code>echo "encodedstring" | base64 --decode</code>. The base64 encoded message <ul><strong>Rm9yZW5zaWNzIGlzIGZ1bg==</strong></ul> decodes to <strong>Forensics is fun</strong>.</li>
</ul>

<h2>Conclusion</h2>
<p>Using John the Ripper, I successfully cracked the password for the Trybreakingme.zip file and accessed the hidden message inside the PDF file. This process demonstrated the efficiency of John the Ripper in password cracking and the fun of forensic challenges.</p>
