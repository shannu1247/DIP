close all;
clc;
I=imread('lena.jpg');
Ig=rgb2gray(I);

subplot(1,2,1);
imshow(I);
title('Original RGB Image')

subplot(1,2,2);
imshow(Ig)
title('Grayscale Image')