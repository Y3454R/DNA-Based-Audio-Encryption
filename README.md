# DNA-Based Audio Encryption System

A novel audio encryption system that uses DNA sequence mapping and complementary base pairing for secure audio file encryption and decryption.

## Features

- **DNA-based encryption**: Uses biological DNA sequences (A, T, G, C) for encryption
- **Complementary base pairing**: Leverages Watson-Crick base pairing for security
- **Lossless encryption**: Perfect reconstruction of original audio
- **Variable key lengths**: Adaptive key generation based on file size
- **Command-line interface**: Easy-to-use scripts for encryption/decryption
- **Comprehensive testing**: Security and efficiency analysis tools

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Y3454R/DNA-Based-Audio-Encryption.git
cd DNA-Based-Audio-Encryption
```

2. Install dependencies:

```bash
pip install -r requirements_testing.txt
```

## Quick Start

### Encryption

```bash
# Basic encryption
python encryption.py dog.wav

# Custom output and key length
python encryption.py dog.wav -o my_encrypted.wav -k 2000

# With visualization
python encryption.py dog.wav --plot
```

### Decryption

```bash
# Basic decryption
python decryption.py encrypted.wav

# With verification and audio playback
python decryption.py encrypted.wav --verify --play

# Custom output location
python decryption.py encrypted.wav -o my_decrypted.wav
```

## How It Works

### 1. Audio to Binary Conversion

- Audio files are converted to binary representation
- Each audio sample becomes an 8-bit binary string

### 2. Binary to DNA Mapping

- Binary pairs are mapped to DNA bases:
  - `00` → `A` (Adenine)
  - `01` → `G` (Guanine)
  - `10` → `C` (Cytosine)
  - `11` → `T` (Thymine)

### 3. DNA Encryption Process

- A random DNA key is generated
- Complementary base pairing is used for encryption:
  - `A` ↔ `T`
  - `G` ↔ `C`
- Variable increments and position-based transformations add complexity

### 4. Decryption

- Reverse complementary base pairing
- Position information is used to reconstruct the original sequence
- DNA sequence is converted back to binary, then to audio

## File Structure

```
DNA-Based-Audio-Encryption/
├── encryption.py          # Main encryption script
├── decryption.py          # Main decryption script
├── security_tests.py      # Security analysis tools
├── benchmark_comparison.py # Performance benchmarking
├── test_dna_encryption.py  # Comprehensive testing suite
├── requirements_testing.txt # Python dependencies
├── Encryption.ipynb       # Original Jupyter notebook
├── Decryption.ipynb       # Original Jupyter notebook
├── dog.wav                # Sample audio file
└── README.md              # This file
```

## Generated Files

During encryption/decryption, the following files are created:

- `encrypted.wav` - Encrypted audio file
- `key.txt` - DNA encryption key
- `info.txt` - Encryption metadata
- `decrypted.wav` - Decrypted audio file
- `enctime.txt` - Encryption timing data
- `dectime.txt` - Decryption timing data

## Command Line Options

### Encryption (`encryption.py`)

```
usage: encryption.py [-h] [-o OUTPUT] [-k KEY_LENGTH] [--key-file KEY_FILE]
                     [--info-file INFO_FILE] [--plot] [--no-play] input_file

positional arguments:
  input_file            Input audio file path

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output encrypted file path (default: encrypted.wav)
  -k KEY_LENGTH, --key-length KEY_LENGTH
                        DNA key length (default: adaptive based on file size)
  --key-file KEY_FILE   Key file path (default: key.txt)
  --info-file INFO_FILE Info file path (default: info.txt)
  --plot                Generate comparison plot
  --no-play             Skip audio playback
```

### Decryption (`decryption.py`)

```
usage: decryption.py [-h] [-o OUTPUT] [--key-file KEY_FILE]
                     [--info-file INFO_FILE] [--original ORIGINAL]
                     [--plot] [--play] [--verify] encrypted_file

positional arguments:
  encrypted_file        Encrypted audio file path

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output decrypted file path (default: decrypted.wav)
  --key-file KEY_FILE   Key file path (default: key.txt)
  --info-file INFO_FILE Info file path (default: info.txt)
  --original ORIGINAL   Original file for verification
  --plot                Generate comparison plot
  --play                Play decrypted audio
  --verify              Verify decryption quality
```

## Security Testing

### Run Comprehensive Tests

```bash
# Complete security and efficiency analysis
python test_dna_encryption.py

# Detailed security tests
python security_tests.py

# Performance benchmarking vs standard algorithms
python benchmark_comparison.py
```

### Security Metrics

- **Randomness Analysis**: Frequency tests, runs tests, chi-square tests
- **Entropy Analysis**: Shannon entropy calculation
- **Correlation Analysis**: Between original and encrypted data
- **Key Management**: DNA sequence validation and distribution analysis

### Performance Metrics

- **Speed**: Encryption/decryption time
- **Throughput**: MB/s processing rate
- **Memory Usage**: RAM consumption during processing
- **File Size**: Encryption overhead analysis

## Algorithm Strengths

1. **Novel Approach**: Uses biological concepts for cryptography
2. **Complementary Security**: Base pairing adds natural security layer
3. **Variable Transformation**: Position-dependent encryption increments
4. **Lossless**: Perfect audio reconstruction
5. **Scalable**: Adaptive key lengths based on content

## Limitations and Considerations

1. **Performance**: May be slower than traditional algorithms for large files
2. **Key Management**: Requires secure storage of DNA key and info files
3. **Research Stage**: Novel algorithm requiring further cryptanalytic review
4. **Dependencies**: Requires specific Python libraries for audio processing



