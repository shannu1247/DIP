I=imread('lena.jpg');


Img_red = I;
Img_red(:,:,2) = 0;   
Img_red(:,:,3) = 0;   

Img_green = I;
Img_green(:,:,1) = 0; 
Img_green(:,:,3) = 0; 

Img_blue = I;
Img_blue(:,:,1) = 0;  
Img_blue(:,:,2) = 0;  


figure;

subplot(2,2,1);
imshow(I);
title('Original Image');

subplot(2,2,2);
imshow(Img_red);
title('Red ');

subplot(2,2,3);
imshow(Img_green);
title('Green ');

subplot(2,2,4);
imshow(Img_blue);
title('Blue ');