# Math functions

Math functions are algorithms that act on individual pixels in images during preprocessing. Unlike image convolution, math functions does not account for surrounding pixels which can limit the alteration we can apply to images.

## Inversion

Color inversion is a useful task in preprocessing. For example, we can use the same model on two LPRs with inverted colors.
<img src="../../../Snippets/C++/CV/Math%20functions/inversion.png" height="300" alt="Inversion">

## Step function

The step function is a mean of highlighting a range of values or a specific color.

here's an example on a grey scale image highlighting a range of 100 - 180:

<img src="../../../Snippets/C++/CV/Math%20functions/step.png" height="300" alt="Step function">

## Darken

Using math functions, an image's brightness can be controlled.

<img src="../../../Snippets/C++/CV/Math%20functions/darken.png" height="200" alt="darken function">

<img src="../../../Snippets/C++/CV/Math%20functions/darken_RBG.png" height="200" alt="darken RBG function">
