import sys

encodingTable = [
0x00,0xBB,0x9B,0xC4,0x6C,0x4A,0x2E,0x22,0x45,0x33,
0xB8,0xD5,0x06,0x0A,0xBC,0xFA,0x79,0x24,0xE1,0xB2,
0xBF,0x2C,0xAD,0x86,0x60,0xA4,0xB6,0xD8,0x59,0x87,
0x41,0x94,0x77,0xF0,0x4F,0xCB,0x61,0x25,0xC0,0x97,
0x2A,0x5C,0x08,0xC9,0x9F,0x43,0x4E,0xCF,0xF9,0x3E,
0x6F,0x65,0xE7,0xC5,0x39,0xB7,0xEF,0xD0,0xC8,0x2F,
0xAA,0xC7,0x47,0x3C,0x81,0x32,0x49,0xD3,0xA6,0x96,
0x2B,0x58,0x40,0xF1,0x9C,0xEE,0x1A,0x5B,0xC6,0xD6,
0x80,0x2D,0x6D,0x9A,0x3D,0xA7,0x93,0x84,0xE0,0x12,
0x3B,0xB9,0x09,0x69,0xBA,0x99,0x48,0x73,0xB1,0x7C,
0x82,0xBE,0x27,0x9D,0xFB,0x67,0x7E,0xF4,0xB3,0x05,
0xC2,0x5F,0x1B,0x54,0x23,0x71,0x11,0x30,0xD2,0xA5,
0x68,0x9E,0x3F,0xF5,0x7A,0xCE,0x0B,0x0C,0x85,0xDE,
0x63,0x5E,0x8E,0xBD,0xFE,0x6A,0xDA,0x26,0x88,0xE8,
0xAC,0x03,0x62,0xA8,0xF6,0xF7,0x75,0x6B,0xC3,0x46,
0x51,0xE6,0x8F,0x28,0x76,0x5A,0x91,0xEC,0x1F,0x44,
0x52,0x01,0xFC,0x8B,0x3A,0xA1,0xA3,0x16,0x10,0x14,
0x50,0xCA,0x95,0x92,0x4B,0x35,0x0E,0xB5,0x20,0x1D,
0x5D,0xC1,0xE2,0x6E,0x0F,0xED,0x90,0xD4,0xD9,0x42,
0xDD,0x98,0x57,0x37,0x19,0x78,0x56,0xAF,0x74,0xD1,
0x04,0x29,0x55,0xE5,0x4C,0xA0,0xF2,0x89,0xDB,0xE4,
0x38,0x83,0xEA,0x17,0x07,0xDC,0x8C,0x8A,0xB4,0x7B,
0xE9,0xFF,0xEB,0x15,0x0D,0x02,0xA2,0xF3,0x34,0xCC,
0x18,0xF8,0x13,0x8D,0x7F,0xAE,0x21,0xE3,0xCD,0x4D,
0x70,0x53,0xFD,0xAB,0x72,0x64,0x1C,0x66,0xA9,0xB0,
0x1E,0xD7,0xDF,0x36,0x7D,0x31]

def encode(str):
    out = ""
    for s in str:
        out += chr(encodingTable[ord(s)])
    return out

def decode(str):
    out = ""
    for s in str:
        for i in xrange(len(encodingTable)):
            if encodingTable[i] == ord(s):
                out += chr(i)
    return out

def main():
    print decode(reversed(("CE65059923F9279923BE111165B19965237399711B30F4F9F9B399BEB3B1E711F59D73B327").decode('hex')))

if __name__ == '__main__':
    main()
