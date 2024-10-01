# Caesar Cipher Python Program

## Overview

This Python program implements the Caesar Cipher algorithm for encrypting and decrypting text. The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is 'shifted' a certain number of places down or up the alphabet. This repository allows users to input a message and a shift value to perform both encryption and decryption.

## Features

- Encrypt text using a specified shift value.
- Decrypt previously encrypted text using the same shift value.
- Simple command-line interface for user interaction.

## Requirements

- Python 3.x
- No additional libraries required

## Installation

1. Clone the repository to your local machine:
      >bash

       git clone https://github.com/Philiposeluk/PRODIGY_CS_01.git
   
2. Navigate to the project directory:
      >bash 
      
       cd caesar_cipher
## Usage


  
  Run the program using Python:
   >bash

    python caesar_cipher.py

## Input


when prompted, enter the following:

 1.(e)ncrypt or (d)ecrypt and (q to quit)
 
 2.Enter your message
 
 3.Enter the shift value (positive for right, negative for left)

## Example 

    Choose an action (e)ncrypt or (d)ecrypt and (q to quit): e
    Enter your message: Hello, World!  
    Enter shift value: 3
    Encrypted message: Khoor, Zruog!

To decrypt:

    Choose an action (encrypt/decrypt): decrypt
    Enter your message: Khoor, Zruog!
    Enter shift value: 3
    Decrypted message: Hello, World!


## Code Structure
 
 - [caesar_cipher.py]: The main program file containing the encryption and decryption functions.
 
 - [README.md]: This file.



