
# Music Based Encryption with Generative RNN

  

So this is my project for Music Bases Encryption using RNN based generator function and encryption pattern that i formulated.

This project is one of my original work although i got inspiration for using tabla as instrument for music from an old blog by Gaurav Trivedi [Machines Learn to Play Tabla](https://www.trivedigaurav.com/blog/machines-learn-to-play-tabla/).

## Here is output of it working just fine.
#### Index Page
![Here we can enter text to encrypt and decrypt using simple form.](https://github.com/kaustubha-chaturvedi/myMusicSpeaks/blob/master/img/mg2.jpeg)

#### Encrypted String Output
![Here we receive output after encryption.](https://github.com/kaustubha-chaturvedi/myMusicSpeaks/blob/master/img/mg.png)

#### Encrypted String Output
![Here we display output after decryption.](https://github.com/kaustubha-chaturvedi/myMusicSpeaks/blob/master/img/mg1.jpeg)
## Problems

 1. Current this is unable to encrypt special characters.
 2. This use single pattern for encryption .
 3.  This doesn't cares to preserve cases of letters. 
## Solution of problems.
 1. Special character support can be easily added with minimal effort.
 2. Multiple patterns for encryption can be devised and even this process can be accelerated by use of generator function to create pattern.
 3. Letter cases can be preserved using ascii pattern within encryption.
## Future Possibilities
 1. This can (actually should be) converted to api and can be used for encrypted data transfer like some hobby project example music-based encryption for chat.
 2.  More instruments can be added by use of generative algorithm making it sound more natural.
## QnAs
1. *Why didn't I used generative algorithm or even better RNN alternatives like `Attention` and `Transformer` ?*
*Actually this is an hobby project and learning was main goal for it so I decided to reinvent the wheel.*
2. *Will I be developing it further?*
*I don't think that I would be developing it further as this is my `proof of concept`.
and this is what it was intended to be like.*
3. *But it just generates text where is music ?*
*Yes it generates text and this text can be played in [`tabla-js`](https://trivedigaurav.com/exp/tabla-js-master/example.html) by **Gaurav Trivedi** and hence i didn't bothered to recreate my own version of `midi-js`.*
