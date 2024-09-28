<h1>Cracking Trybreakingme.zip Using PyZipper and Rockyou.txt</h1>
<hr>
<h3>This document outlines the process of cracking the password for the Trybreakingme.zip file using PyZipper and the rockyou.txt wordlist, including manually entering the password and decoding a base64-encoded message from a PDF.</h3>
<hr>

<h2>Overview of Cracking Process</h2>
<ul>
    <li><strong>Installing PyZipper:</strong> I began by installing PyZipper, a Python library for handling ZIP files.</li>
    <li><strong>Cracking the Password:</strong> I initiated the cracking process using the rockyou.txt wordlist with PyZipper, which successfully cracked the password <strong>softball3</strong>.</li>
    <li><strong>Manually Entering the Password:</strong> I manually entered the cracked password to open the Trybreakingme.zip file and accessed the PDF inside.</li>
    <li><strong>Decoding the Message:</strong> The PDF contained a base64-encoded string: <strong>Rm9yZW5zaWNzIGlzIGZ1bg==</strong>.</li>
    <li><strong>Decoding the Base64 String:</strong> I decoded the base64-encoded string using Python to reveal the message <strong>Forensics is fun</strong>.</li>
</ul>

<h2>Conclusion</h2>
<p>Using PyZipper with the rockyou.txt wordlist, I successfully cracked the password for the Trybreakingme.zip file. After manually entering the password, I accessed the hidden PDF and decoded the base64 message. This process demonstrated the effectiveness of PyZipper and the satisfaction of solving forensic challenges.</p>
