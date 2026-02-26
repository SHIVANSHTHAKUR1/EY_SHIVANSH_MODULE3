# Lab 4.1 – Face Recognition Evidence

## Screenshot

![Real-time identification](./Screenshot%202026-02-26%20182219.png)

## Terminal Output

```
2026-02-26 18:19:11.025112: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2026-02-26 18:19:12.298668: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
WARNING:tensorflow:From C:\Users\shiva\OneDrive\Desktop\College\EY\.venv_tf\Lib\site-packages\tf_keras\src\losses.py:2976: The name tf.losses.sparse_softmax_cross_entropy is deprecated. Please use tf.compat.v1.losses.sparse_softmax_cross_entropy instead.

26-02-26 18:19:18 - Directory C:\Users\shiva\.deepface has been created
26-02-26 18:19:18 - Directory C:\Users\shiva\.deepface\weights has been created
[INFO] Database folder ready at: C:\Users\shiva\OneDrive\Desktop\College\EY\database
[INFO] Add subfolders with photos: database/person_name/image1.jpg
============================================================
  LAB 4.1 — Face Detection & Recognition
  Module 3 | Chitkara University
============================================================

[INFO] Use the interactive menu to execute each lab milestone.
       Recommended order: capture → verify → identify → live → evaluate


[MENU] Choose a lab step:
  1. Capture photos for new person(s)
  2. Verify two images (same person?)
  3. Identify the person in a single image
  4. Run real-time webcam recognition
  5. Evaluate accuracy on labelled test set
  6. Quit

Enter choice (1-6 or q): 1
Enter comma-separated person names: shivansh thakur
Photos per person (default 5): 5

[INFO] Capturing 5 photos for 'shivansh thakur'
       Press SPACE to capture | ESC to stop early
  ✓ Saved: ./database\shivansh thakur\shivansh thakur1.jpg
  ✓ Saved: ./database\shivansh thakur\shivansh thakur2.jpg
  ✓ Saved: ./database\shivansh thakur\shivansh thakur3.jpg
  ✓ Saved: ./database\shivansh thakur\shivansh thakur4.jpg
  ✓ Saved: ./database\shivansh thakur\shivansh thakur5.jpg
[INFO] Captured 5 photos for 'shivansh thakur'

[MENU] Choose a lab step:
  1. Capture photos for new person(s)
  2. Verify two images (same person?)
  3. Identify the person in a single image
  4. Run real-time webcam recognition
  5. Evaluate accuracy on labelled test set
  6. Quit

Enter choice (1-6 or q): 2
Path to image 1: database\shivansh thakur\shivansh thakur1.jpg
Path to image 2: "C:\Users\shiva\OneDrive\Pictures\Camera Roll\WhatsApp Image 2025-11-26 at 23.57.50_7dceba56.jpg"

[VERIFY] Comparing:
  Image 1: database\shivansh thakur\shivansh thakur1.jpg
  Image 2: C:\Users\shiva\OneDrive\Pictures\Camera Roll\WhatsApp Image 2025-11-26 at 23.57.50_7dceba56.jpg
2026-02-26 18:20:56.701191: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
26-02-26 18:20:57 - 🔗 vgg_face_weights.h5 will be downloaded from https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5 to C:\Users\shiva\.deepface\weights\vgg_face_weights.h5...
Downloading...
From: https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5
To: C:\Users\shiva\.deepface\weights\vgg_face_weights.h5
100%|█████████████████████████████████████████████████████████| 580M/580M [00:34<00:00, 16.8MB/s]
  Same person? ✓ YES
  Distance   : 0.5248  (threshold: 0.6800)
  Model      : VGG-Face

[MENU] Choose a lab step:
  1. Capture photos for new person(s)
  2. Verify two images (same person?)
  3. Identify the person in a single image
  4. Run real-time webcam recognition
  5. Evaluate accuracy on labelled test set
  6. Quit

Enter choice (1-6 or q): 3
Path to query image: "C:\Users\shiva\OneDrive\Pictures\Camera Roll\WhatsApp Image 2025-11-26 at 23.57.50_7dceba56.jpg"

[IDENTIFY] Searching database for: C:\Users\shiva\OneDrive\Pictures\Camera Roll\WhatsApp Image 2025-11-26 at 23.57.50_7dceba56.jpg
  Best match : shivansh thakur
  Distance   : 0.4992

[MENU] Choose a lab step:
  1. Capture photos for new person(s)
  2. Verify two images (same person?)
  3. Identify the person in a single image
  4. Run real-time webcam recognition
  5. Evaluate accuracy on labelled test set
  6. Quit

Enter choice (1-6 or q): 4
[INFO] Launching real-time recognition. Press 'q' to stop in the video window.

[INFO] Real-time recognition started.
       Press 'c' to identify current face | 'q' to quit

[INFO] Identifying face...

[IDENTIFY] Searching database for: C:\Users\shiva\AppData\Local\Temp\tmp88ijv32h.jpg
  Best match : shivansh thakur
  Distance   : 0.1091
[INFO] Recognition session ended.
```
