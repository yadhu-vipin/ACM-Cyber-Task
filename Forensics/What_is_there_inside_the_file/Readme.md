<h1>Cracking Trybreakingme.zip Using PyZipper and Rockyou.txt</h1>
<hr>
<h3>This document outlines the process of cracking the password for the Trybreakingme.zip file using PyZipper and the rockyou.txt wordlist, including decoding a base64-encoded message from a PDF.</h3>
<hr>

<h2>Overview of Cracking Process</h2>
<ul>
    <li><strong>Installing PyZipper:</strong> I began by installing PyZipper, a Python library for handling ZIP files.</li>
    <li><strong>Extracting Password Hash:</strong> Using PyZipper, I extracted the password hash from the ZIP file. This hash was stored in a file named <strong>zip_hash.txt</strong>.</li>
    <li><strong>Cracking the Password:</strong> I initiated the cracking process using the rockyou.txt wordlist with PyZipper to crack the password <strong>softball3</strong>.</li>
    <li><strong>Decoding the Message:</strong> After successfully cracking the password, I opened the PDF file contained within the ZIP, which had a base64-encoded string: <strong>Rm9yZW5zaWNzIGlzIGZ1bg==</strong>.</li>
    <li><strong>Decoding the Base64 String:</strong> I decoded the base64-encoded string using Python to reveal the message <strong>Forensics is fun</strong>.</li>
</ul>

<h2>Conclusion</h2>
<p>Using PyZipper with the rockyou.txt wordlist, I successfully cracked the password for the Trybreakingme.zip file and decoded the hidden message inside the PDF file. This process showcased the effectiveness of PyZipper for ZIP file manipulation and the utility of wordlist-based attacks in password cracking.</p>
