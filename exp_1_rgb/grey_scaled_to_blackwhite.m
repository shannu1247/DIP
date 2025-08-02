% Read image
I = imread('lena.jpg');  % Use correct filename!
[m, n, c] = size(I);  % Get size from the RGB image

% If RGB, convert to grayscale manually
if c == 3
    gray_img = zeros(m, n);
    for i = 1:m
        for j = 1:n
            r = double(I(i,j,1));
            g = double(I(i,j,2));
            b = double(I(i,j,3));
            gray_img(i,j) = (r + g + b) / 3;
        end
    end
else
    gray_img = double(I);  % Already grayscale
end

% Compute mean intensity manually
sum_val = 0;
for i = 1:m
    for j = 1:n
        sum_val = sum_val + gray_img(i,j);
    end
end
mean_val = sum_val / (m * n);

% Threshold to black and white
bw_img = zeros(m, n, 'uint8');
for i = 1:m
    for j = 1:n
        if gray_img(i,j) > mean_val
            bw_img(i,j) = 255;
        else
            bw_img(i,j) = 0;
        end
    end
end

% Display result
imshow(bw_img);
title('Black and White Image using Mean Threshold');
