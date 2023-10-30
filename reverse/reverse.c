#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 3)
    {
        fprintf(stderr, "Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    FILE *input_file = fopen(argv[1], "rb");
    if (input_file == NULL)
    {
        fprintf(stderr, "Could not open input file for reading.\n");
        return 1;
    }

    // Read header
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, input_file);

    // Use check_format to ensure WAV format
    if (!check_format(header))
    {
        fprintf(stderr, "Input file is not in WAV format.\n");
        fclose(input_file);
        return 1;
    }

    // Open output file for writing
    FILE *output_file = fopen(argv[2], "wb");
    if (output_file == NULL)
    {
        fprintf(stderr, "Could not open output file for writing.\n");
        fclose(input_file);
        return 1;
    }

    // Write header to file
    fwrite(&header, sizeof(WAVHEADER), 1, output_file);

    // Use get_block_size to calculate size of block
    int block_size = get_block_size(header);

    // Calculate the total data size
    fseek(input_file, 0, SEEK_END);
    long data_size = ftell(input_file) - sizeof(WAVHEADER);
    fseek(input_file, sizeof(WAVHEADER), SEEK_SET);

    // Allocate memory for audio block
    uint8_t *audio_block = malloc(block_size);
    if (audio_block == NULL)
    {
        fprintf(stderr, "Memory allocation failed.\n");
        fclose(input_file);
        fclose(output_file);
        return 1;
    }

    // Write reversed audio to file
    long num_blocks = data_size / block_size;
    for (long i = num_blocks - 1; i >= 0; i--)
    {
        fseek(input_file, sizeof(WAVHEADER) + i * block_size, SEEK_SET);
        fread(audio_block, 1, block_size, input_file);
        fwrite(audio_block, 1, block_size, output_file);
}


    // Clean up
    fclose(input_file);
    fclose(output_file);
    free(audio_block);

    return 0;
}

int check_format(WAVHEADER header)
{
    if (header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        return 1;
    }
    return 0;
}

int get_block_size(WAVHEADER header)
{
    return header.numChannels * (header.bitsPerSample / 8);
}
