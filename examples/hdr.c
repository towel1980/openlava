#include<stdio.h>

struct LSFHeader {
    unsigned short refCode;
    unsigned short opCode;
    unsigned int length;
    unsigned short version;
    unsigned short reserved;
    unsigned int reserved0;
};


int
main(int argc, char **argv)
{
    unsigned int word1;
    unsigned int word2;
    unsigned int word3;
    unsigned int word4;
    struct LSFHeader header;
    struct LSFHeader header2;

    header.refCode = 2;
    header.opCode = 15;
    header.length = 1024;
    header.version = 2;
    header.reserved = 3;
    header.reserved0 = 43;

    printf("\
%d %d %d %d %d %d\n", header.refCode, header.opCode,
           header.length, header.version,
           header.reserved0, header.reserved);

    word1 = header.refCode;
    word1 = word1 << 16;
    word1 = word1 | (header.opCode & 0x0000FFFF);
    word2 = header.length;
    word3 = header.version;
    word3 = word3 << 16;
    word3 = word3 | (header.reserved & 0x0000FFFF);
    word4 = header.reserved0;

    header2.refCode = word1 >> 16;
    header2.opCode = word1 & 0xFFFF;
    header2.length = word2;
    header2.version = word3 >> 16;
    header2.reserved = word3 & 0xFFFF;
    header2.reserved0 = word4;

    printf("\
%d %d %d %d %d %d\n", header2.refCode, header2.opCode,
           header2.length, header2.version,
           header2.reserved0, header2.reserved);

    return 0;
}
