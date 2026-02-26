# Lab 4.2 – OCR Evidence

## Command
```
(.venv_tf) PS C:\Users\shiva\OneDrive\Desktop\College\EY> .\.venv_tf\Scripts\python.exe MODULE_3/day4/lab4_2_ocr_tesseract.py
```

## Input Asset
- Invoice image processed: `MODULE_3/day4/sample_invoice.jpg`

## Console Highlights
```
[INFO] Detected Tesseract at: C:\Program Files\Tesseract-OCR\tesseract.exe
[INFO] Tesseract version: 5.5.0.20241111
============================================================
  LAB 4.2 — OCR Pipeline with Tesseract
  Module 3 | Chitkara University
============================================================
[INFO] Created sample_invoice.jpg for testing

[STEP 1] Basic OCR (no preprocessing)
[OCR - Basic] Processing: sample_invoice.jpg
  Extracted 234 characters

[STEP 2] OCR with full preprocessing pipeline
[PREPROCESS] sample_invoice.jpg  (original size: 800×600)
  ✓ Step 1: Grayscale conversion
  ✓ Step 2: Denoising
  ✓ Step 3: Adaptive thresholding
  ✓ Step 4: Deskewing
  ✓ Step 5: Upscaled 2× (new size: 1600×1200)
  → Preprocessed image saved: sample_invoice_preprocessed.jpg

[STEP 3] Regex field extraction
  dates               : ['15/02/2024']
  amounts             : ['Rs. 150.00', 'Rs. 800.00', 'Rs. 1,200.00', 'Rs. 2,150.00']
  total               : 2150.00
  invoice_number      : INV-2024-00123
  emails              : ['customer@example.com']

[STEP 4] Full invoice pipeline
[OCR] Extracted text (235 chars)
[INFO] Result saved to: invoice_result.json
```

## Generated Artefacts
- Raw invoice image: `MODULE_3/day4/sample_invoice.jpg`
- Preprocessed image: `MODULE_3/day4/sample_invoice_preprocessed.jpg`
- Structured output: `MODULE_3/day4/invoice_result.json`
