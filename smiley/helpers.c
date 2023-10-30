#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Define the color you want to apply to black pixels
    RGBTRIPLE newColor;
    newColor.rgbtRed = 255;   // Red
    newColor.rgbtGreen = 0;   // Green
    newColor.rgbtBlue = 0;    // Blue

    // Iterate through each pixel in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];

            // Check if the pixel is black (R, G, and B values are 0)
            if (pixel.rgbtRed == 0 && pixel.rgbtGreen == 0 && pixel.rgbtBlue == 0)
            {
                // Change the color of the black pixel
                image[i][j] = newColor;
            }
        }
    }
}
