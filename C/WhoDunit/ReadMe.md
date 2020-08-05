# WhoDunit

![WhoDunit](/Snippets/C/WhoDunit.png)

Welcome to Tudor Mansion. Your host, Mr. John Boddy, has met an untimely end - he’s the victim of foul play. To win this game, you must determine whodunit.

## Background

![Clue](img/clue.bmp)

 Unfortunately for you (though even more unfortunately for Mr. Boddy), the only evidence you have is a 24-bit BMP file called [`clue.bmp`](img/clue.bmp), that Mr. Boddy whipped up on his computer in his final moments. Hidden among this file’s red "noise" is a drawing of whodunit.

## Goal

The goal is to design a program that will take in the clue and reveals the WhoDunit!

![verdict](img/verdict.bmp)

## Usage

 ```bash
 $ ./whodunit clue.bmp verdict.bmp
 $
 ```

Using key knowledge of 24-bit BMP files and bits manipulation, this program solves the mystery.
